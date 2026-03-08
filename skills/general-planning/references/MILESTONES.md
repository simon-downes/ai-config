# Milestone Planning Guide

## Purpose

Break work into incremental, testable deliverables that can be implemented and verified independently.

## Rules

1. **Each milestone has exactly ONE deliverable**
   - Deliverables must be testable and measurable
   - Avoid compound deliverables ("X works AND Y works")

2. **Prefer smaller milestones over large ones**
   - Each milestone should feel achievable in a single session
   - Better to have 5 small milestones than 2 large ones

3. **Order by dependency**
   - Foundational work before dependent work
   - Infrastructure before features
   - Core functionality before enhancements

4. **Tasks should be concrete and actionable**
   - Avoid vague tasks like "implement everything"
   - Be specific about what needs to be done

5. **Deliverables should be demonstrable**
   - You should be able to show or test the deliverable
   - Avoid deliverables like "code is written"

## Format

```
1. [Milestone objective - what we're building]
   - [Concrete task]
   - [Concrete task]
   - [Concrete task]
   Deliverable: [Single testable outcome]

2. [Next milestone objective]
   - [Concrete task]
   - [Concrete task]
   Deliverable: [Single testable outcome]
```

## Good Examples

### Example 1: Authentication Feature

```
1. Set up project structure and dependencies
   - Initialize repository with standard structure
   - Configure build tooling
   - Add core dependencies (Express, PostgreSQL client, Redis client)
   Deliverable: Project builds successfully with no errors

2. Implement database schema and migrations
   - Create users table with GitHub ID and email
   - Create sessions table with token and expiry
   - Add migration tooling
   Deliverable: Database schema is created and migrations run successfully

3. Implement GitHub OAuth flow
   - Create OAuth redirect endpoint
   - Implement callback handler
   - Exchange authorization code for access token
   Deliverable: Users can authorize via GitHub and API receives access token

4. Implement session management
   - Create session on successful OAuth
   - Store session in PostgreSQL
   - Return session cookie to client
   Deliverable: Users receive session cookie after successful login

5. Add authentication middleware
   - Create middleware to validate session token
   - Protect endpoints with authentication check
   - Return 401 for invalid/missing tokens
   Deliverable: Protected endpoints require valid session token
```

*Why good: Each milestone has a single, testable deliverable. Milestones are ordered by dependency. Tasks are concrete and actionable.*

---

### Example 2: Rate Limiting Feature

```
1. Set up Redis rate limit storage
   - Add Redis client configuration
   - Create rate limit key schema (api_key:timestamp)
   - Add TTL management for automatic cleanup
   Deliverable: Redis stores and expires rate limit counters correctly

2. Implement rate limiting middleware
   - Create middleware function
   - Add token bucket logic
   - Integrate with existing auth middleware
   Deliverable: API returns 429 when rate limit exceeded

3. Add rate limit response headers
   - Include X-RateLimit-Remaining in all responses
   - Include Retry-After header on 429 responses
   - Document header format
   Deliverable: All responses include rate limit headers
```

*Why good: Small, focused milestones. Each deliverable is independently testable. Clear progression from infrastructure to feature to enhancement.*

---

### Example 3: Data Migration

```
1. Create migration script structure
   - Set up migration framework
   - Add rollback capability
   - Create dry-run mode
   Deliverable: Migration script runs in dry-run mode without errors

2. Implement data extraction
   - Query source database
   - Transform data to target schema
   - Handle missing or invalid data
   Deliverable: Script extracts and transforms all records successfully

3. Implement data loading with validation
   - Load transformed data to target database
   - Validate data integrity after load
   - Log any validation failures
   Deliverable: Data loads successfully with validation passing

4. Add monitoring and rollback
   - Track migration progress
   - Implement rollback on failure
   - Add completion verification
   Deliverable: Migration completes with verification or rolls back on error
```

*Why good: Incremental approach with safety measures. Each milestone builds on the previous. Deliverables are measurable.*

---

## Bad Examples

### Bad Example 1: Too Large

```
1. Build the entire authentication system
   - Everything related to auth
   Deliverable: Auth works
```

*Why bad: Too large, vague tasks, untestable deliverable. Should be broken into 5-10 smaller milestones.*

---

### Bad Example 2: Multiple Deliverables

```
1. Implement authentication and rate limiting
   - Create OAuth flow
   - Add session management
   - Implement rate limiter
   - Add response headers
   Deliverable: Users can log in AND rate limiting works
```

*Why bad: Multiple deliverables in one milestone. Should be split into separate milestones for auth and rate limiting.*

---

### Bad Example 3: Non-Testable Deliverable

```
1. Write authentication code
   - Write the code
   - Make it good
   Deliverable: Code is written
```

*Why bad: Deliverable is not testable or measurable. What does "code is written" mean? How do you verify it?*

**Better:**
```
1. Implement OAuth callback handler
   - Create callback endpoint
   - Exchange authorization code for token
   - Handle OAuth errors
   Deliverable: Callback endpoint successfully exchanges codes for tokens
```

---

### Bad Example 4: Wrong Order

```
1. Add authentication middleware
   - Create middleware to validate tokens
   Deliverable: Middleware validates tokens

2. Implement session creation
   - Create sessions on login
   Deliverable: Sessions are created
```

*Why bad: Milestone 1 depends on milestone 2 (can't validate tokens that don't exist yet). Order should be reversed.*

---

## Tips

### Breaking Down Large Work

If a milestone feels too large, ask:
- Can this be split into infrastructure + implementation?
- Can this be split into core functionality + enhancements?
- Can this be split into happy path + error handling?
- Can this be split by component or layer?

### Writing Good Deliverables

Good deliverables answer:
- What can I test or demonstrate?
- What observable behavior changes?
- What new capability exists?

Avoid deliverables like:
- "Code is written"
- "Feature is complete"
- "Everything works"

Prefer deliverables like:
- "API returns 429 when rate limit exceeded"
- "Users can log in via GitHub"
- "Database schema is created"

### Ordering Milestones

Think about:
- What needs to exist before this can work?
- What's the minimal foundation?
- What can be tested independently?
- What provides the most value earliest?

### Task Granularity

Tasks should be:
- Specific enough to guide implementation
- Not so detailed that they prescribe exact code
- Focused on what needs to be done, not how

Good task: "Create OAuth redirect endpoint"
Bad task: "Create a function called handleOAuthRedirect that takes req and res parameters and..."
