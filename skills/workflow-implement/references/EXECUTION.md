# Execution Guide

Complete walkthrough of implementing a rate limiting feature.

## Initial Setup

Plan exists at:
```
~/plans/api-service/2026-03-07-rate-limiting-PLAN.md
```

Contains: Objective, Requirements, Technical Design, 3 Milestones

## Step 1: Initialize LOG.md

Create `~/plans/api-service/2026-03-07-rate-limiting-LOG.md`:

```markdown
# Implementation Log

Plan: [2026-03-07-rate-limiting-PLAN.md](./2026-03-07-rate-limiting-PLAN.md)
Started: 2026-03-07 10:00

## Milestone 1: Set up Redis rate limit storage
Status: In Progress
Started: 2026-03-07 10:00

### Tasks
(to be generated after investigation)

### Progress
2026-03-07 10:00 - Started milestone
```

## Step 2: Investigate Context

Read existing code to understand patterns:
- `config/redis.js` - existing Redis configuration
- `src/middleware/` - middleware patterns
- `tests/` - testing conventions

Identify: Project uses separate Redis DBs for different concerns, follows module-per-feature structure.

## Step 3: Generate Tasks

Based on milestone objective and existing patterns, generate high-level tasks:

Update LOG.md:
```markdown
### Tasks
- Add Redis client configuration for rate limiting
- Create rate limit key schema (rate:limit:{apiKey})
- Add TTL management (60 second expiration)
- Write unit tests for storage operations
```

## Step 4: Implement Tasks

**Task 1: Add Redis client configuration**

Create `src/rate-limit/redis-client.js` following existing Redis pattern:
```javascript
const redis = require('redis');

const rateLimitClient = redis.createClient({
  host: process.env.REDIS_HOST,
  port: process.env.REDIS_PORT,
  db: 2
});

module.exports = rateLimitClient;
```

Append to LOG.md:
```markdown
2026-03-07 10:15 - Created Redis client for rate limiting (separate DB)
```

**Task 2: Create key schema**

Add `src/rate-limit/storage.js`:
```javascript
const KEY_PREFIX = 'rate:limit:';
const TTL_SECONDS = 60;

function getRateLimitKey(apiKey) {
  return `${KEY_PREFIX}${apiKey}`;
}
```

Append to LOG.md:
```markdown
2026-03-07 10:30 - Implemented key schema with rate:limit: prefix
```

**Task 3: Add TTL management**

Complete `src/rate-limit/storage.js`:
```javascript
async function incrementCounter(apiKey) {
  const key = getRateLimitKey(apiKey);
  const count = await client.incr(key);
  
  if (count === 1) {
    await client.expire(key, TTL_SECONDS);
  }
  
  return count;
}
```

Append to LOG.md:
```markdown
2026-03-07 10:45 - Added TTL management with 60s expiration
```

**Task 4: Write tests**

Create `tests/rate-limit/storage.test.js` following project test patterns:
```javascript
describe('Rate Limit Storage', () => {
  it('should expire counters after 60 seconds', async () => {
    // test implementation
  });
});
```

Append to LOG.md:
```markdown
2026-03-07 11:00 - Added unit tests for storage operations
```

## Step 5: Verify and Complete

Run tests:
```bash
npm test tests/rate-limit/
```

All pass ✓

Commit:
```bash
git commit -m "Set up Redis rate limit storage"
```

Append to LOG.md:
```markdown
2026-03-07 11:15 - Milestone complete (commit: a1b2c3d)
```

## Step 6: Report Progress

```
Milestone 1 complete: Redis rate limit storage is set up and tested.

Next: Milestone 2 - Implement rate limiting middleware

Proceed?
```

## Step 7: Continue Remaining Milestones

Repeat for Milestones 2 and 3.

## Step 8: Complete Implementation

Final LOG.md:
```markdown
# Implementation Log

Plan: [2026-03-07-rate-limiting-PLAN.md](./2026-03-07-rate-limiting-PLAN.md)
Started: 2026-03-07 10:00
Completed: 2026-03-07 14:30

## Summary

All 3 milestones completed:
1. Redis rate limit storage - a1b2c3d
2. Rate limiting middleware - b2c3d4e
3. Response headers - c3d4e5f

## Milestone 1: Set up Redis rate limit storage
[... details ...]

## Milestone 2: Implement rate limiting middleware
[... details ...]

## Milestone 3: Add rate limit response headers
[... details ...]
```

Report:
```
Implementation complete. All milestones delivered:

✓ Redis rate limit storage with TTL
✓ Middleware enforcing 100 req/min limit
✓ Response headers (X-RateLimit-Remaining, Retry-After)

Would you like to enter Review Mode?
```

---

## Task Granularity

**Too coarse:**
```
- Implement rate limiting
```

**Too fine:**
```
- Import redis module
- Create client variable
- Set host property
```

**Appropriate:**
```
- Add Redis client configuration for rate limiting
- Create rate limit key schema
- Implement counter increment with TTL
```

---

## Progress Note Quality

**Poor:**
```
2026-03-07 10:15 - Did some work
```

**Better:**
```
2026-03-07 10:15 - Created Redis client
```

**Best:**
```
2026-03-07 10:15 - Created Redis client for rate limiting (separate DB to isolate from cache)
```

Include what was done and why (if decision was made).

---

## Handling Discovered Work

During Milestone 2, discover API has GraphQL endpoint not mentioned in plan.

**Don't:**
- Implement rate limiting for GraphQL without approval
- Ignore GraphQL
- Assume GraphQL should work the same way

**Do:**

Add to LOG.md after Milestone 2 tasks:
```markdown
### Discovered Issues
- API has GraphQL endpoint not in requirements
- GraphQL uses different auth mechanism
- May need separate rate limiting strategy
```

After completing milestone, report:
```
Milestone 2 complete.

Discovered issue: API includes GraphQL endpoint not addressed in plan. 
GraphQL uses different auth and may need separate rate limiting approach.

Options:
A) Apply same rate limiting to GraphQL
B) Create separate plan for GraphQL rate limiting
C) Exclude GraphQL from this implementation

Which approach?
```
