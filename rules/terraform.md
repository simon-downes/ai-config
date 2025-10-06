# Terraform Coding Rules

Standards for writing maintainable and well-structured Terraform infrastructure code.

## Toolchain
*Required tools and commands for Terraform development.*

- You MUST use `tofu` command instead of `terraform` for all operations

## File Organization
*Standards for structuring Terraform projects and files.*

### Directory Structure
- You MAY use a single `main.tf` file for applications with few resources
- You SHOULD split large files by logical grouping when `main.tf` becomes unwieldy
- You SHOULD move a large number of `data` blocks to `data.tf`
- You SHOULD move large `locals` blocks to `locals.tf`
- You SHOULD group resources by service (e.g., `dynamodb.tf`, `postgres.tf`, `eventbridge.tf`)
- You SHOULD place IAM policies and roles in the same file as the resources they support
- You SHOULD prefix related service files with the service name (e.g., `lambda-my-function.tf`)
- You MAY isolate specific items or concepts into separate files

### File Naming and Formatting
- You MUST name all Terraform files (`*.tf`) in kebab-case
- You MUST format all Terraform files using `terraform fmt`
- You MUST format YAML/Markdown files using prettier
- You MUST name OPA policy files (`*.rego`) in kebab-case
- You MUST format OPA files using `opa fmt -w .`

### Required Files
- You MUST place `terraform` and `provider` blocks in `providers.tf`
- You MUST place all `variable` blocks in `variables.tf` (variables file MUST contain only variable blocks)
- You MUST place all `output` blocks in `outputs.tf` (outputs file MUST contain only output blocks)
- You MUST include a `README.md` file for all modules

### File-Specific Rules
- `data.tf` MUST contain only `data` blocks and optionally one `locals` block
- `locals.tf` MUST contain only a single `locals` block
- `variables.tf` MUST be used only for externally provided variables when outside modules
- You MUST use variable blocks outside modules only for variables provided by environment (`TF_VAR_`) or tfvars files
- You SHOULD use `locals` for internal variables that aren't varied by external inputs

## Code Structure
*Standards for organizing blocks and arguments within files.*

### Block Ordering
- You MUST place `locals` blocks first in any file
- You MUST include only one `locals` block per file
- You MUST order variable block attributes: `description`, `type`, `default`, `validation`
- You MUST include `type` and `description` attributes for all variables
- You MUST include `description` attribute for all outputs

### Meta-Arguments
- You MUST place `count` or `for_each` as the first argument, separated by newline
- You MUST place meta-arguments after all real arguments in this order: `depends_on`, `lifecycle`, `provider`
- You SHOULD place `tags` argument as the last real argument before meta-arguments

## Naming Conventions
*Standards for naming resources and variables.*

### Resource Names
- You SHOULD follow the format: `<application>-<environment>-<resource-name>`
- You SHOULD use kebab-case for resource names
- You MAY use shorter alternatives when length restrictions apply

### Variables and Locals
- You MUST use snake_case for variable and local names
- You SHOULD use descriptive names that clearly indicate purpose

## Best Practices
*Implementation guidelines for maintainable Terraform code.*

### Resource Tagging
- You MUST tag all resources according to organizational tagging policy
- You SHOULD be aware that missing tags may cause access control issues
