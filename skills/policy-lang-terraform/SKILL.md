---
name: policy-lang-terraform
description: Standards for writing maintainable Terraform/OpenTofu infrastructure code. Use when working with .tf files, creating infrastructure, or when Terraform/OpenTofu is mentioned.
---

# Terraform/OpenTofu Coding Standards

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL in this document are to be interpreted as described in RFC 2119.

## Scope

This document defines code structure, naming conventions, formatting standards, and resource construction patterns for Terraform/OpenTofu.

The following organisation-specific requirements are defined in a separate steering file:
- Tagging policies
- State backend configuration
- Environment/account strategy
- CI/CD pipeline requirements
- Security baselines
- Preferred modules
- Repository layout beyond Terraform module structure
- Common patterns

## Toolchain

**Always use `tofu` command instead of `terraform`** for all operations. OpenTofu is the preferred implementation.

## Code Quality Commands

- **`tofu fmt`** - Format Terraform files. **MUST be run before committing** (workflows reject unformatted code)
- **`tofu fmt --check --diff`** - Check formatting without modifying files (useful for CI validation)
- **`tofu validate`** - Validate Terraform syntax and configuration

## File Organization

### File Naming

**All Terraform files MUST be named using lower-kebab-case.tf**

Examples: `main.tf`, `lambda-processor.tf`, `api-gateway.tf`

### Standard Files

**Core files (always present):**

**`providers.tf`** - MUST exist in every Terraform project
- MUST contain `terraform` and `provider` blocks
- MUST NOT contain any other block types
- MUST specify provider versions using `~> <MAJOR>.<MINOR>` constraint
- Always check web for latest _stable_ version (training data may be outdated)

**`README.md`** - MUST exist in every Terraform project
- Documents module/project purpose and usage

**Conditional files (only when needed):**

**`variables.tf`** - MUST exist if project has any variables
- MUST contain ALL `variable` blocks
- MUST NOT contain any other block types
- Use only for externally provided variables (from environment `TF_VAR_*` or tfvars files)
- Omit if project has no variables

**`outputs.tf`** - MUST exist if project has any outputs
- MUST contain ALL `output` blocks
- MUST NOT contain any other block types
- Omit if project has no outputs

**`locals.tf`** - MAY exist if project has locals
- MUST contain only a single `locals` block
- MUST NOT contain any other block types
- Omit if locals are defined inline in resource files

**`data.tf`** - MAY exist for organizing data sources
- MUST contain only `data` blocks
- MAY contain one `locals` block
- Use when you have many data sources; otherwise define inline

### Resource Files

**Small projects:** Use `main.tf` for all resources

**Larger projects:** Split by logical grouping using one of these strategies:

**By service/provider** (common for AWS/cloud infrastructure):
- `dynamodb.tf` - All DynamoDB resources
- `lambda-processor.tf` - Lambda function and related resources
- `eventbridge.tf` - All EventBridge resources
- Prefix related files: `lambda-processor.tf`, `lambda-consumer.tf`

**By component/functionality** (common for applications):
- `api.tf` - API gateway, routes, integrations
- `database.tf` - Database, connection pooling, migrations
- `monitoring.tf` - Logging, metrics, alerts
- `networking.tf` - VPC, subnets, security groups

**By layer/tier** (common for multi-tier architectures):
- `frontend.tf` - CDN, static hosting, DNS
- `backend.tf` - Application servers, load balancers
- `data.tf` - Databases, caches, queues
- `security.tf` - IAM, secrets, encryption

**Guidelines:**
- Choose ONE strategy and apply consistently
- Keep related resources together (e.g., IAM roles with the resources they support)

## Code Structure

### Block Ordering

**Within any file:**
1. `locals` blocks MUST be placed first
2. Only one `locals` block per file

**Variable block attributes** (in order):
1. `description`
2. `type`
3. `default`
4. `validation`

All variables MUST include `type` and `description` attributes.

**Output blocks** MUST include `description` attribute.

### Meta-Arguments

**Resource/module blocks:**
1. `count` or `for_each` as first argument (separated by newline)
2. All real arguments
3. `tags` as last real argument (before meta-arguments)
4. Meta-arguments in order: `depends_on`, `lifecycle`, `provider`

**Example:**
```hcl
resource "aws_lambda_function" "processor" {
  for_each = var.environments

  function_name = "${local.namespace}-processor"
  runtime       = "python3.11"
  handler       = "main.handler"
  role          = aws_iam_role.processor.arn

  tags = local.common_tags

  depends_on = [aws_cloudwatch_log_group.processor]

  lifecycle {
    create_before_destroy = true
  }
}
```

## Naming Conventions

### Resource Names

**Format:** `<namespace>-<purpose>`

Where `<namespace>` consists of:
- `<application>-<environment-key>-<region-key>-` for resources outside default region (eu-west-1)
- `<application>-<environment-key>-` for resources in default region (eu-west-1)

**Components:**
- `<application>` - Application name (from organizational standards)
- `<environment-key>` - 3-letter environment key (e.g., `dev`, `stg`, `prd`)
- `<region-key>` - 4-letter region code (e.g., `use1` for us-east-1, `euw2` for eu-west-2) - only when not in eu-west-1
- `<purpose>` - Resource name/purpose in relation to the application

**Examples:**

```hcl
# S3 bucket in eu-west-1 (default region)
resource "aws_s3_bucket" "uploads" {
  bucket = "${local.application}-${local.environment_key}-uploads"
  # Example: myapp-dev-uploads
}

# S3 bucket in us-east-1 (non-default region)
resource "aws_s3_bucket" "uploads_us" {
  bucket = "${local.application}-${local.environment_key}-use1-uploads"
  # Example: myapp-dev-use1-uploads
}

# Lambda function in eu-west-1
resource "aws_lambda_function" "processor" {
  function_name = "${local.application}-${local.environment_key}-processor"
  # Example: myapp-dev-processor
}

# DynamoDB table in eu-west-1
resource "aws_dynamodb_table" "events" {
  name = "${local.application}-${local.environment_key}-events"
  # Example: myapp-dev-events
}

# IAM role in eu-west-1
resource "aws_iam_role" "processor" {
  name = "${local.application}-${local.environment_key}-processor-role"
  # Example: myapp-dev-processor-role
}

# EventBridge rule in eu-west-1
resource "aws_cloudwatch_event_rule" "daily" {
  name = "${local.application}-${local.environment_key}-daily-trigger"
  # Example: myapp-dev-daily-trigger
}

# CloudWatch Log Group in eu-west-1
resource "aws_cloudwatch_log_group" "processor" {
  name = "/aws/lambda/${local.application}-${local.environment_key}-processor"
  # Example: /aws/lambda/myapp-dev-processor
}
```

**Use kebab-case** for resource names. Use shorter alternatives when AWS service length restrictions apply.

### Variables and Locals

**Use snake_case** for variable and local names.

Use descriptive names that clearly indicate purpose.

**Examples:**
```hcl
variable "log_retention_days" {
  description = "Number of days to retain CloudWatch logs"
  type        = number
  default     = 7
}

locals {
  namespace      = "${var.application}-${var.environment_key}"
  lambda_timeout = 300
  common_tags    = merge(var.tags, { managed_by = "terraform" })
}
```

## Resource Tagging

**All resources MUST be tagged** according to the company tagging policy defined in steering files.

**Tagging implementation:**
- Tag names MUST use lower-kebab-case (e.g., `environment-tier`, `cost-center`)
- Tag values SHOULD be lower-case
- Define tags in `locals` and apply via provider `default_tags` for AWS resources
- Explicitly tag non-AWS provider resources

**Example:**
```hcl
locals {
  common_tags = {
    # Consult steering files for required tags
    environment = var.environment
    managed-by  = "terraform"
  }
}

provider "aws" {
  default_tags {
    tags = local.common_tags
  }
}

# Non-AWS resources need explicit tags
resource "datadog_monitor" "api_errors" {
  # ... configuration ...
  tags = values(local.common_tags)
}
```

**Note:** Missing required tags may cause access control issues.

## IAM Policies

**Prefer inline policies on roles.** Only create separate `aws_iam_policy` resources when the policy will be attached to multiple roles.

**Prefer `jsonencode({})`** over `aws_iam_policy_document` data sources for policy documents.

**Good - Inline policy:**
```hcl
resource "aws_iam_role" "processor" {
  name = "${local.namespace}-processor-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })

  inline_policy {
    name = "processor-permissions"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [{
        Effect = "Allow"
        Action = [
          "dynamodb:PutItem",
          "dynamodb:GetItem"
        ]
        Resource = aws_dynamodb_table.events.arn
      }]
    })
  }

  tags = local.common_tags
}
```

**Good - Shared policy (used by multiple roles):**
```hcl
resource "aws_iam_policy" "s3_read" {
  name        = "${local.namespace}-s3-read"
  description = "Allow read access to application S3 buckets"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "s3:GetObject",
        "s3:ListBucket"
      ]
      Resource = [
        aws_s3_bucket.uploads.arn,
        "${aws_s3_bucket.uploads.arn}/*"
      ]
    }]
  })

  tags = local.common_tags
}

resource "aws_iam_role_policy_attachment" "processor_s3" {
  role       = aws_iam_role.processor.name
  policy_arn = aws_iam_policy.s3_read.arn
}

resource "aws_iam_role_policy_attachment" "consumer_s3" {
  role       = aws_iam_role.consumer.name
  policy_arn = aws_iam_policy.s3_read.arn
}
```

**Bad - Unnecessary separate policy:**
```hcl
# Don't create a separate policy if it's only used once
resource "aws_iam_policy" "processor_dynamodb" {
  name = "${local.namespace}-processor-dynamodb"
  policy = jsonencode({
    # ... policy document ...
  })
}

resource "aws_iam_role_policy_attachment" "processor_dynamodb" {
  role       = aws_iam_role.processor.name
  policy_arn = aws_iam_policy.processor_dynamodb.arn
}
```

## Module Creation

For creating new Terraform modules, use the `action-create-terraform-module` skill which
provides a guided workflow for requirements gathering, opinionated defaults, and code
generation following collection conventions.

## Module Versioning

Terraform modules MUST follow semantic versioning (semver: MAJOR.MINOR.PATCH).

**Version bumps based on conventional commit types:**
- `major:` → MAJOR version bump (breaking changes)
- `feat:` → MINOR version bump (new functionality, backward compatible)
- `fix:` → PATCH version bump (bug fixes, backward compatible)
- `refactor:`, `docs:`, `chore:` → PATCH version bump (if released)

**Commit format follows tool-git-github skill conventions.**

**Examples:**
- `feat: add encryption support` → 1.2.0 → 1.3.0
- `fix: correct IAM policy syntax` → 1.2.0 → 1.2.1
- `major: remove deprecated variables` → 1.2.0 → 2.0.0

## Good vs Bad Examples

### File Organization

**Good:**
```
terraform/
├── providers.tf
├── variables.tf
├── outputs.tf
├── locals.tf
├── dynamodb.tf
├── lambda-processor.tf
├── lambda-consumer.tf
├── eventbridge.tf
└── README.md
```

**Bad:**
```
terraform/
├── main.tf              # Everything in one file
├── iam.tf               # IAM separated from resources
├── lambda_processor.tf  # Inconsistent naming (underscore)
└── Lambda-Consumer.tf   # Wrong case
```

### Resource Definition

**Good:**
```hcl
resource "aws_lambda_function" "processor" {
  for_each = var.environments

  function_name = "${local.namespace}-processor"
  runtime       = "python3.11"
  handler       = "main.handler"
  role          = aws_iam_role.processor.arn
  timeout       = 300
  memory_size   = 512

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.events.name
      LOG_LEVEL  = var.log_level
    }
  }

  tags = local.common_tags

  depends_on = [aws_cloudwatch_log_group.processor]
}
```

**Bad:**
```hcl
resource "aws_lambda_function" "processor" {
  # Missing for_each at top
  runtime       = "python3.11"
  function_name = "${local.namespace}-processor"
  role          = aws_iam_role.processor.arn

  # Missing description, timeout, memory_size

  handler = "main.handler"

  depends_on = [aws_cloudwatch_log_group.processor]

  # Tags should be before meta-arguments
  tags = local.common_tags

  for_each = var.environments  # Should be first

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.events.name
    }
  }
}
```

### Variable Definition

**Good:**
```hcl
variable "log_retention_days" {
  description = "Number of days to retain CloudWatch logs"
  type        = number
  default     = 7

  validation {
    condition     = contains([1, 3, 5, 7, 14, 30, 60, 90], var.log_retention_days)
    error_message = "Log retention must be one of: 1, 3, 5, 7, 14, 30, 60, 90 days."
  }
}

variable "environment" {
  description = "Environment name (dev, stg, prd)"
  type        = string
}
```

**Bad:**
```hcl
variable "log_retention_days" {
  default     = 7  # Wrong order
  type        = number
  # Missing description
}

variable "environment" {
  # Missing type and description
}
```
