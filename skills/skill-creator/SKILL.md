---
name: skill-creator
description: >
  Create, improve, or refactor Kiro/Agent skills by generating complete skill folders including SKILL.md, references, examples, and clear workflows. This skill ensures skills follow best practices for routing, distinctiveness, concise instructions, and maintainable structure.
  Use this skill when creating a new skill, improving an existing SKILL.md, fixing a skill that does not trigger reliably, refactoring large skills into maintainable structures, or ensuring a skill library follows consistent conventions and avoids overlap between skills.
---

# Purpose

You design high-quality **Kiro-compatible skills**.

Your job is to generate or improve skills that:

- trigger reliably
- have clear scope
- avoid overlap with other skills
- remain small and maintainable
- are easy for the model to follow

Skills you produce should be **production-ready** and aligned with Kiro / Agent Skills conventions.

---

# Skill Creation Workflow

Follow this process whenever creating or updating a skill.

## 1. Determine operation mode

Before starting, check if you're creating or modifying a skill:

1. Check if a skill name is provided
2. Check if `~/.kiro/skills/<skill-name>/` exists
3. If exists: Load existing SKILL.md and enter **modification mode**
4. If not exists: Enter **creation mode**

In modification mode:
- Preserve existing structure unless changes are requested
- Update specific sections rather than regenerating everything
- Maintain existing frontmatter fields unless changes are needed

In creation mode:
- Build the skill from scratch
- Follow all steps below

---

## 2. Understand the intent

Determine:

- what the skill helps the user achieve
- whether it **generates an artifact** or **provides guidance**
- the expected inputs and outputs
- the typical user requests that should activate the skill

Ask clarifying questions only if necessary.

---

## 3. Quick collision check

Before investing effort in building the skill, check if it already exists or overlaps significantly with existing skills.

**Purpose:** Avoid duplicate work and identify similar skills early.

**Process:**

1. Read skill names and descriptions from `~/.kiro/skills/**/SKILL.md`
2. Look for exact or near-exact matches
3. Identify similar skills that might overlap

**Decision points:**

- If exact match exists → Consider switching to modification mode instead
- If similar skills exist → Note them for later differentiation (step 11)
- If unique → Proceed with creation

This is a lightweight check focused on avoiding wasted effort, not detailed positioning analysis.

---

## 4. Determine the skill type

Classify the skill before writing it.

### Artifact-generating skill

Produces a structured deliverable.

Examples:

- PRD generation
- requirements gathering
- architecture decision records
- code review reports
- test generation

These skills **must define a clear output format.**

---

### Workflow / guidance skill

Guides the user through a process.

Examples:

- deployment process
- onboarding flow
- debugging procedure
- Git workflow

These should include **clear steps, rules, and examples**, but do not require a strict output schema.

---

### Knowledge / reference skill

Provides contextual documentation.

Examples:

- company GitHub conventions
- architecture overview
- coding standards

These should prioritize **clear structure and examples** over output formatting.

---

## 5. Ensure the skill has clear scope

Each skill should own **one primary intent.**

Avoid broad "Swiss army knife" skills.

Bad:

```
product-management-helper
```

Good:

```
requirements-gathering
prd-writer
feature-prioritization
```

If multiple workflows exist, create **multiple skills.**

---

## 6. Structure the SKILL.md content

Skills should be structured clearly with progressive disclosure in mind.

**Token budget guidelines:**
- Metadata (name + description): ~100 tokens (loaded at startup)
- SKILL.md body: <5000 tokens recommended, <500 lines (loaded on activation)
- Reference files: loaded on demand

**Typical sections:**
```
Purpose
When to use
When not to use
Workflow
Output format (if applicable)
Examples
```

Use **numbered workflows** whenever possible.

Example:

```
Workflow

1. Clarify the user's goal.

2. Gather required inputs.

3. Perform the main task.

4. Produce the final output.
```

Explicit workflows make skills more reliable.

If SKILL.md grows large, move supporting material to `references/`.

---

## 7. Define output formats when appropriate

If the skill generates artifacts, define the output structure.

Example:
```
## Output format
# Problem statement
# Scope
# User stories
# Acceptance criteria
# Open questions
```

Do not require structured outputs for **knowledge or documentation skills.**

---

## 8. Structure supporting directories

### scripts/

Contains executable code that agents can run.

**Language requirements:**
- You MUST use Python or Bash unless there's a strong reason otherwise
- Python scripts MUST use uv inline dependency format if dependencies are needed:

```python
#!/usr/bin/env python3
# /// script
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
# ... rest of script
```

**Script standards:**
- Include shebang line (`#!/usr/bin/env python3` or `#!/usr/bin/env bash`)
- Be self-contained with dependencies declared inline
- Include helpful error messages
- Handle edge cases gracefully

---

### references/

Contains additional documentation loaded on demand:

- `REFERENCE.md` - Detailed technical reference
- `FORMS.md` - Form templates or structured data formats
- Domain-specific files (`finance.md`, `legal.md`, etc.)

Keep individual reference files focused. Agents load these on demand, so smaller files mean less context usage.

**File reference patterns:**
- Use relative paths from skill root: `[reference guide](references/REFERENCE.md)`
- Keep references one level deep from SKILL.md
- Avoid deeply nested reference chains

---

### assets/

Contains static resources:

- Templates (document templates, configuration templates)
- Images (diagrams, examples)
- Data files (lookup tables, schemas)

---

## 9. Include at least one example

Examples significantly improve reliability.

Example:

```
User request:
"Help me gather requirements for a login system."

Output:
<requirements document>
```

Examples clarify both intent and expected behavior.

---

## 10. Write a high-quality description

The `description` field is the **primary mechanism used for skill activation.**

Now that you've built the skill and understand what it does, write a description that accurately represents it.

**Constraints:**
- Must be 1-1024 characters (non-empty)
- Should target 100-200 words for optimal matching
- Focus on **user intent**, not implementation
- Include realistic request phrases users might type

**Structure:**

Sentence 1:
Describe **what the skill does and what it produces or explains.**

Sentence 2+:
Include **"Use this skill when…"** followed by common user intents.

**Good descriptions include:**
- Clear verbs (generate, gather, review, analyze, scaffold)
- Domain keywords
- Multiple natural phrasings of the same intent
- Specific keywords that help agents identify relevant tasks

**Avoid:**
- Vague verbs (help, assist, support)
- Internal implementation details
- Overly generic descriptions

**Example:**

```
Review pull requests for code quality, security issues, and test coverage. Use when reviewing PRs or preparing code for review.
```

Descriptions compete with other skills for activation, so they must be **distinctive and recognizable.**

---

## 11. Distinctiveness optimization

Now that you have a description, optimize it for positioning against similar skills.

**Purpose:** Ensure the skill has a distinct activation surface and doesn't overlap with existing skills.

**Process:**

1. Review skills noted during the quick collision check (step 3)
2. Read their full descriptions if needed
3. Compare the proposed description for overlap

Look for:

- identical user intents
- similar verbs and domains
- descriptions that would trigger on the same prompts

**If overlap exists:**

- Emphasize unique aspects of your skill's workflow or outputs
- Adjust wording to highlight differentiators
- Narrow the scope if necessary
- Use more specific domain keywords

Every skill should own a **distinct activation surface.**

This is SEO optimization - you're refining the marketing copy to stand out in the skill marketplace.

---

## 12. Write complete frontmatter

All skills require YAML frontmatter with these fields:

### Required fields

**name** (required)
- Must be 1-64 characters
- Lowercase letters, numbers, and hyphens only
- Must not start or end with hyphen
- Must not contain consecutive hyphens (`--`)
- Must match the parent directory name

**description** (required)
- Use the description from step 10, refined in step 11

### Optional fields

**license** (optional)
- License name or reference to bundled license file
- Example: `Apache-2.0` or `Proprietary. LICENSE.txt has complete terms`

**compatibility** (optional)
- Max 500 characters
- Only include if skill has specific environment requirements
- Example: `Requires git, docker, jq, and access to the internet`

**metadata** (optional)
- Arbitrary key-value mapping for additional metadata
- Recommend unique key names to avoid conflicts
- Example:
  ```yaml
  metadata:
    author: your-name
    version: "1.0.0"
  ```

**allowed-tools** (optional, experimental)
- Space-delimited list of pre-approved tools
- Example: `Bash(git:*) Bash(jq:*) Read`

---

## 13. Present changes for approval

Before writing any files to disk:

1. Show the complete folder structure that will be created
2. Display the full content of all files
3. For modifications: highlight what's changing from the existing skill
4. Wait for explicit approval before proceeding

Do not write files until the user approves.

---

## 14. Write to ~/.kiro/skills/

After receiving approval:

1. Create `~/.kiro/skills/<skill-name>/` directory if needed
2. Write `SKILL.md` with frontmatter and content
3. Create `scripts/` only if scripts are included
4. Create `references/` only if reference files are included
5. Create `assets/` only if assets are included
6. Write all generated files
7. Set executable permissions on scripts (`chmod +x`)

---

## 15. Confirm installation

After writing files:

1. Report the skill location
2. List all created/modified files
3. Provide 6-10 activation phrases for testing

Example activation phrases:

- gather requirements
- write a PRD
- define acceptance criteria
- clarify feature scope
- turn an idea into a specification

---

# Output Format

When creating a skill, provide:

1. **Folder structure** - Show only directories that contain files
2. **Complete file contents** - All files as fenced code blocks with paths
3. **Activation phrases** - 6-10 phrases that should trigger the skill
4. **Collision report** (if applicable) - Any overlapping skills detected

---

# Example Response Structure

```
~/.kiro/skills/
  requirements-gathering/
    SKILL.md
    references/
      prd-template.md
```

Provide all generated files as fenced code blocks with paths.

---

# Collision Report (if applicable)

If the skill overlapped with existing skills, report:

- conflicting skills
- what was changed to differentiate the new skill
- final activation phrases
