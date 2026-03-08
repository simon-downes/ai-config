---
name: general-planning
description: Guide complete planning workflow from vague intent to executable implementation plan through structured requirements gathering, technical design, and milestone breakdown. Use when starting projects that need comprehensive planning before implementation, creating detailed plans for complex features, or turning high-level ideas into actionable work with clear deliverables.
---

# General Planning

## Purpose

Guide the complete planning process from vague intent to detailed execution plan. This skill orchestrates three phases: requirements gathering, technical design, and milestone planning.

## When to Use

- Starting new projects or features that need comprehensive planning
- User provides initial direction but needs structured planning
- Work requires investigation and design before implementation
- Creating plans that will be stored as artifacts for execution

## When Not to Use

- Simple bug fixes or trivial changes
- Work that's already well-defined with clear requirements
- Quick exploratory tasks

## Planning Artifacts

Plans are stored as:
- `~/plans/<project>/<date>-<description>-PLAN.md` - Complete plan document
- `~/plans/<project>/<date>-<description>-LOG.md` - Implementation progress log

## Three-Phase Planning Process

### Phase 1: Objective + Requirements

**Goal:** Transform vague intent into clear, testable requirements.

**Steps:**

1. **Write Objective** - Concise problem description and desired outcome (2-4 sentences)

2. **Analyze Initial Input** - Identify core objective, what's stated, what's implied, obvious gaps

3. **Identify Gaps** - Error handling, edge cases, validation, security, performance expectations

4. **Ask Clarifying Questions** - ONE at a time, target critical gaps first, offer options, iterate

5. **Draft Requirements** - Use RFC 2119 keywords (MUST/SHOULD/MAY), focus on observable behavior, add testable acceptance criteria, group logically

6. **Iterate Until Approved** - Present to user, incorporate feedback, refine until confirmed

**Approval Gate:** "Do the objective and requirements look correct?"

See [requirements guide](references/REQUIREMENTS.md) for detailed format rules and examples.

---

### Phase 2: Technical Design

**Goal:** Explain how the system will be built to satisfy requirements.

**Steps:**

1. **Understand Context** - Review requirements, identify work type

2. **Select Relevant Sections** - Choose from available sections based on work type, skip what doesn't apply

3. **Draft Design** - Write selected sections concisely, focus on decisions and structure, include examples

4. **Review with User** - Present design, iterate based on feedback

**After approval, automatically proceed to Phase 3.**

See [design guide](references/DESIGN.md) for available sections and selection guidance.

---

### Phase 3: Milestones

**Goal:** Break work into incremental, testable deliverables.

**Steps:**

1. **Create Milestones** - Each has exactly ONE testable deliverable, prefer smaller milestones, order by dependency

2. **Format:**
   ```
   1. [Milestone objective]
      - task
      - task
      Deliverable: [testable outcome]
   ```

3. **Present Complete Plan** - Show all three phases together

**Approval Gate:** "Here is the complete plan. Shall we move to Implementation Mode?"

See [milestone guide](references/MILESTONES.md) for detailed rules and examples.

---

## Quick Reference

### Requirement Format

```
- MUST / SHOULD / MAY <clear requirement>
  - AC: <testable acceptance criteria>
  - Why: <optional context>
```

**RFC 2119 Keywords:**
- **MUST** — Mandatory behavior
- **SHOULD** — Strongly recommended
- **MAY** — Optional capability

Default to MUST unless clear reason for SHOULD or MAY.

### Design Section Selection

- **Small feature:** Overview, Components, Data Flow
- **New service:** Most or all sections
- **Infrastructure:** Overview, Architecture, Technical Stack, Key Decisions
- **Integration:** Overview, External Integrations, Data Flow, Non-Functional
- **Refactoring:** Overview, Components, Key Decisions, Risks

### Milestone Rules

- Exactly ONE deliverable per milestone
- Deliverables must be testable
- Prefer smaller over larger
- Order by dependency

---

## Example Workflow

**User Request:** "I need to add rate limiting to our API"

**Phase 1 Output:**
```
Objective: Add rate limiting to the API to prevent abuse and ensure fair usage.

Requirements:
- MUST enforce rate limit of 100 requests per minute per API key
  - AC: Requests exceeding limit return HTTP 429
  - AC: Response includes Retry-After header
- MUST persist rate limit counters across API restarts
  - AC: Counter state survives application restart
- SHOULD include rate limit status in response headers
  - AC: Responses include X-RateLimit-Remaining header
```

**Phase 2 Output:**
```
# Technical Design: API Rate Limiting

## Overview
Implement token bucket rate limiting using Redis for distributed counter storage.

## Technical Stack
- Redis: Rate limit counter storage
- Middleware: Express rate-limit middleware
- Storage: Redis cluster (existing)

## Data Flow
1. Request arrives at API
2. Middleware extracts API key
3. Check Redis for current token count
4. If tokens available: decrement and allow
5. If no tokens: return 429 with Retry-After

## Key Decisions
- Redis chosen for atomic operations and TTL support
- Token bucket algorithm for smooth rate limiting vs fixed window
```

**Phase 3 Output:**
```
Milestones:

1. Set up Redis rate limit storage
   - Add Redis client configuration
   - Create rate limit key schema
   - Add TTL management
   Deliverable: Redis stores and expires rate limit counters correctly

2. Implement rate limiting middleware
   - Create middleware function
   - Add token bucket logic
   - Integrate with existing auth middleware
   Deliverable: API returns 429 when rate limit exceeded

3. Add rate limit response headers
   - Include X-RateLimit-Remaining
   - Include Retry-After on 429
   Deliverable: All responses include rate limit headers
```
