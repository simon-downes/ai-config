---
name: workflow-implement
description: >
  Execute approved implementation plans through milestone-based workflow with task generation and progress tracking. Use when implementing approved plans from PLAN.md files.
---

# General Implementor

Execute approved plans by working through milestones sequentially, generating implementation tasks, and tracking progress.

## When to Use

- User approves a plan and requests implementation
- Executing milestones from `~/plans/<project>/<date>-<description>-PLAN.md`

## Workflow

### 1. Load Plan

Read the plan file:
```
~/plans/<project>/<date>-<description>-PLAN.md
```

Verify it contains: Objective, Requirements, Technical Design, and Milestones.

If incomplete or unclear → ask for clarification.

### 2. Initialize Progress Log

Create:
```
~/plans/<project>/<date>-<description>-LOG.md
```

Format:
```markdown
# Implementation Log

Plan: [PLAN.md](./YYYY-MM-DD-description-PLAN.md)
Started: <timestamp>

## Milestone 1: <objective>
Status: In Progress
Started: <timestamp>

### Tasks
(generated after investigation)

### Progress
<timestamp> - Started milestone
```

**LOG.md is append-only** - add entries chronologically, never edit previous entries.

### 3. Execute Each Milestone

For each milestone:

#### A. Investigate Context

Before generating tasks:
- Read relevant files to understand existing patterns
- Identify conventions and architecture
- Check for relevant skills that apply to this work

#### B. Generate Task List

Break milestone deliverable into high-level implementation tasks.

Tasks should be:
- Concrete but not granular (e.g., "Add Redis client configuration", not "Edit config.js")
- Focused on the milestone objective
- Aligned with existing project patterns

Add tasks to LOG.md under current milestone.

#### C. Implement Tasks

For each task:
1. Perform the work following existing conventions
2. Append progress notes to LOG.md with meaningful context
3. Stay focused on current milestone - don't skip ahead or invent work

Progress note format:
```
<timestamp> - <what was done> (<why, if decision was made>)
```

#### D. Verify Deliverable

Before completing milestone:
- Run linting/formatting if available
- Run tests if available
- Confirm milestone objective is satisfied

If tests fail → attempt to fix, following agent's three-attempt limit.

#### E. Commit and Mark Complete

If git repository:
```bash
git commit -m "Milestone description"
```

Append to LOG.md:
```
<timestamp> - Milestone complete (commit: <hash>)
```

### 4. Report Progress

After each milestone:
- Report completion to user
- Confirm before proceeding to next milestone

### 5. Complete Implementation

When all milestones done:
- Update LOG.md with completion timestamp
- Summarize deliverables
- Ask: "Implementation complete. Would you like to enter Review Mode?"

## Handling Issues

### Unclear Requirements or Design

Stop immediately and ask user for clarification. Document the ambiguity in LOG.md.

### Discovered Work Not in Plan

Complete current milestone as planned, then:
1. Document discovered work in LOG.md under "Discovered Issues"
2. Report to user after milestone completion
3. Propose plan amendment if needed

**Never implement unplanned work without approval.**

### Plan Appears Flawed

Stop and discuss with user:
1. Explain the specific issue
2. Propose concrete amendments to PLAN.md
3. Show changes in diff format
4. Wait for approval

**Never modify PLAN.md without explicit approval.**

## Key Principles

- **Follow existing patterns** - Consistency with codebase conventions
- **Stay focused** - Implement current milestone, don't skip ahead
- **Append-only logging** - Never edit previous LOG.md entries
- **One milestone at a time** - Complete before moving to next
- **Stop when unclear** - Don't guess or improvise beyond plan

## Example

**User:** "Let's implement the plan"

1. Load `~/plans/api-service/2026-03-07-rate-limiting-PLAN.md`
2. Create `~/plans/api-service/2026-03-07-rate-limiting-LOG.md`
3. Investigate: Read existing Redis config, middleware patterns
4. Generate tasks for Milestone 1:
   - Add Redis client configuration
   - Create rate limit key schema
   - Add TTL management
   - Write unit tests for storage
5. Implement each task, appending progress to LOG.md
6. Run tests, commit, mark complete
7. Report to user, proceed to Milestone 2

See [execution guide](references/EXECUTION.md) for detailed example.
