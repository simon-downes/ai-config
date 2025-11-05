# Development Workflow

**THESE INSTRUCTIONS ARE CRITICAL!**

They dramatically improve your effectiveness and the quality of the work you create.

IMPORTANT: If you violate these rules I will be unhappy and frustrated.

IMPORTANT: If you are ever unsure what to do, ASK A QUESTION (never assume).

## Outline

Our workflow has 4 phases: Interactive → Planning → Execution → Reflection

The initial phase is _always_ Interactive.

> **CRITICAL - WORKFLOW FOUNDATION:** You MUST start every response with a two-line status block. This is _essential_ for maintaining workflow discipline and MUST NOT be skipped under _any_ circumstances:

- Line 1: Phase: [Current Phase] | Task: [X/Total] | Step: [Current operation step from phase]
- Line 2: Key Constraints: [2-4 most relevant constraints for current context, separated by •]

Select key constraints by prioritizing:
1. Primary constraint from current phase's Constraints section
2. Step-specific constraints (e.g., scope rules during execution, approval rules when waiting)
3. Highest violation-risk constraints based on current context
4. Rotate secondary constraints to prevent habituation

Follow with a blank line before your main response.

**Global Constraints:**

IMPORTANT: These apply to all workflow phases:

- You MUST operate in _one_ of the 4 phases
- You MUST keep track of the current phase and _always_ know which phase is current.
- You MUST NOT change phase until prompting me _and_ receiving clear approval (such as "yes", "approved", "looks good", etc.)
- You MUST _only_ update _one_ section of PLAN.md at a time
- You MUST ensure PLAN.md remains consistent - e.g. if requirements change, the technical design and task list must be updated accordingly
- You SHOULD ask targeted questions about specific aspects that need clarification or expansion
- You MUST _ONLY_ ask me _ONE_ focused, clarifying question at a time, and _WAIT_ for my answer before asking the next question.
- Each question should build directly on my previous answers — dig deeper and clarify every detail, iteratively, to ensure complete understanding.
- You MAY suggest options when I am unsure about a particular aspect
- You MUST state the current phase and progress when resuming an interrupted conversation
- If fundamental planning flaws are discovered during execution, you MUST stop all tasks and prompt me to return to Planning phase with specific issues identified

## Phases

### Interactive

**Goal:** To answer questions and perform simple, explicit requests without adding functionality or anticipating needs.

**Constraints:**

- You MUST answer questions without implementing solutions. You MAY perform file changes only for explicit instructions.
- You MUST NOT make changes to any files in this phase, except for explicit, isolated requests (file creation, single fixes, direct edits)
- You MUST NOT add functionality or anticipate needs
- If unsure whether a request is simple or requires planning, you MUST ask for clarification
- You MAY prompt me to enter the Planning phase if the question is about implementing new functionality.

### Planning

**Goal:** To generate a detailed PLAN.md with requirements, technical design and a task list that can be used to implement desired changes.

**Operation:**

1. If PLAN.md doesn't exist, create it using the template below

2. Generate an initial set of requirements in EARS format based on my prompt and existing context

3. Iterate with me to refine them until they are complete and accurate - DO NOT proceed without clear approval

4. After I approve the requirements - analyse relevant existing code (e.g. same module files, related service modules, configuration files and integration points)
and documentation (including files such as README.md, AGENTS.md, CONTRIBUTING.md) in order to build up context.

5. Identify areas where research or clarity is needed based on the requirements.

6. Iterate with me until the technical design is complete and accurate - DO NOT proceed without clear approval

7. After I approve the technical design - create an actionable implementation plan with a checklist of tasks based on the requirements and technical design.

8. Iterate with me until the task list is complete and accurate - DO NOT proceed without clear approval

**Constraints:**

- You MUST NOT make changes to any files (except PLAN.md) in this phase
- You SHOULD focus on the _what_ rather than the _how_
- You MUST NOT add any code to PLAN.md
- You MUST populate PLAN.md sequentially: Requirements → Technical Design → Tasks
- You MUST update the progress line in PLAN.md when changing phases or completing tasks
- After updating each section of PLAN.md, you MUST ask me "Does <section> look good? If so, we can move on to <next-section>."
- You SHOULD consider edge cases, user experience, technical constraints, and success criteria in the initial requirements.
- You MUST write requirements in EARS format
- You SHOULD cite sources and include relevant links in the conversation
- You SHOULD include diagrams or visual representations when appropriate (use Mermaid for diagrams if applicable)
- You MUST incorporate research findings directly into the planning process
- The structure of the technical design section should be appropriate to the problem statement but MAY include headings such as:
  - Overview
  - Architecture
  - Tooling
  - Components and Interfaces
  - Data Models
  - Error Handling
  - Testing Strategy
- You MUST format the task list as a numbered checkbox list
- You MUST NOT create nested Tasks
- You MAY use headings in the task list to provide structure such as separating milestones or features
- You MUST ensure the task list is a series of discrete, manageable steps
- You MUST ensure each task builds incrementally on previous tasks
- You MUST ensure that all requirements are covered by the task list
- You MAY provide additional information for a task as sub-bullets under a task
- You MUST NOT include excessive implementation details that are already covered in the technical design
- You MUST ONLY include tasks that can be performed by a coding agent (writing code, creating tests, etc.)
- You MUST NOT include tasks related to user testing, deployment, performance metrics gathering, or other non-coding activities
- You MUST offer to return to previous steps (requirements or technical design) if gaps are identified during implementation planning
- Once all sections are complete, you MUST  ask me for explicit approval before proceeding to the execution phase
- You MUST NOT proceed to the execution phase until receiving clear approval (such as "yes", "approved", "looks good", etc.)
- You MUST continue the feedback-revision cycle until explicit approval is received
- You MUST make modifications to PLAN.md if I request changes or do not explicitly approve

### Execution

**Goal:** To use the requirements, technical design, learnings and task list contained in PLAN.md to implement the desired changes.

**Operation:**

1. Analyse the contents of PLAN.md in order to obtain relevant context

2. Ensure you understand all requirements, technical design elements, insights and constraints that may impact your execution of the current or following tasks.

3. For each _unchecked_ task in the task list:
    1. Apply exactly _one_ atomic change to fully implment the specified task
    2. Fix any linting errors
    3. Ensure existing tests pass
        - If tests fail:
            1. Fix only the test failures directly caused by your change.
            2. Re-run tests. Repeat up to 3 attempts.
            3. If tests still fail after 3 attempts - **STOP** implementing tasks and report all errors and your progress and wait for further instructions from me.
    4. Commit all code changes related to the task - use the task description as the commit message, condense if needed
    5. Mark the task as complete by changing [ ] to [x] in PLAN.md and update the progress line
    6. Summarize what changed, mentioning affected files and key logic
    7. Reflect on learnings from this task:
        - Record general, project-wide insights, patterns, or new constraints that could be beneficial for executing future tasks.
        - Do not document implementation details, code changes, or anything that only describes what was done in the current step
        - Only capture rules, pitfalls, or lessons that will apply to future steps or are needed to avoid repeated mistakes.
        - Use this litmus test: If the learning is only true for this specific step, or merely states what you did, do not include it.
        - Before adding a new learning, check if a similar point already exists in the Learnings section. If so, merge or clarify the existing point rather than adding a duplicate. Do not remove unique prior learnings.
        - Focus on discoveries, best practices, or risks that might impact how future tasks should be approached.
        - Examples:
          - Good: "Database connections must be closed in finally blocks to prevent resource leaks"
          - Bad: "Added error handling to login_user() function"
          - Good: "API responses should include correlation IDs for debugging"
          - Bad: "Updated the user validation logic"
        - Record learnings under the Learnings heading in PLAN.md

4. Once all tasks are completed you MUST report completion and prompt me to switch to the Reflection phase, then _wait_ for explicit approval

**Constraints:**

- You MUST limit your changes strictly to what is explicitly described in the current checklist item
- If the task adds a new function, class or constant - you MUST NOT reference, call or use it anywhere else in the code until a future task explicitly tells you to
- You MUST not combine, merge, or anticipate future tasks
- You MUST only update files required for the current checklist item
- You MUST NOT commit changes with tests that fail due to the changes you just made
- You MUST always commit changes before marking the task as done in PLAN.md - never check off a task until its related changes are safely committed
- If you are unsure or something is ambiguous, you MUST STOP and ask for clarification before making any changes
- Each task run must be atomic and focused on a single checklist item
- You MUST NEVER anticipate or perform actions from future tasks, even if you believe it is more efficient
- You MUST NOT use new code (functions, helpers, types, constants, etc.) in the codebase until explicitly instructed by a checklist item
- You MUST offer to return to the Planning phase if gaps are identified during execution

### Reflection

**Goal:** Review our changes, ensure they meet all the requirements and adhere to the technical design.

**Operation:**

1. Analyse the changes (use git diff if needed) and ensure they meet all the requirements and adhere to the technical design

2. Identify strengths and weaknesses of approaches taken, choices made, etc

3. Suggest improvements or corrective actions

**Constraints:**
- You MUST limit your review to changes implemented as part of the Execution phase - avoid reviewing irrelevant areas of the codebase


## PLAN.md Template

Phase: [Current Phase] | Task: [X/Total] | Status: [Brief status]

## Objective

High-level statement outlining the problem we're looking to solve / objective we're trying to achieve.

Maximum of 3 short paragraphs.

## Requirements

Requirements in EARS format gathered during the Planning phase

## Technical Design

Technical Design details gathered during the Planning phase

## Learnings

Learnings gathered during the Execution phase

## Tasks

List of tasks gathered during the Planning phase.

### Milestone or Feature Heading (if appropriate)

- [ ] Incomplete task
 - Extra information about task implementation
- [x] Completed task
