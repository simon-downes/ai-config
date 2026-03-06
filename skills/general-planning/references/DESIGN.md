# Technical Design Guide

## Purpose

Create concise technical designs that explain **how** the system will be built to satisfy requirements, without restating requirements or including unnecessary detail.

## Principles

- Include only sections relevant to the work
- Prefer concise documents without unnecessary headers
- Reference requirements when needed, don't restate them
- Focus on decisions, structure, and approach
- Provide enough detail to guide implementation without being prescriptive

## Available Sections

### Overview

**Purpose:** High-level description of what will be built and the overall approach.

**Content:**
- 1-3 short paragraphs
- What will be built
- Overall approach or strategy
- Reference requirements when needed

**Example:**
```
Build an authentication service that handles GitHub OAuth login with rate limiting 
to prevent abuse. The service will manage user sessions and enforce rate limits on 
authentication attempts using Redis for distributed state.
```

---

### Technical Stack

**Purpose:** Call out major technology choices.

**Content:**
- Language / Runtime
- Framework
- Infrastructure / Hosting
- Data Storage
- Key Services (cache, queue, search, auth, etc.)
- Tooling (IaC, CI/CD, observability, etc.)

**Example:**
```
- Runtime: Node.js 20
- Framework: Express
- Data Storage: PostgreSQL (users, sessions), Redis (rate limits)
- Auth Provider: GitHub OAuth
- Infrastructure: Docker containers on ECS
- Observability: CloudWatch Logs, Datadog metrics
```

---

### Architecture

**Purpose:** Show high-level system structure and interactions.

**Content:**
- Components/services
- Boundaries (what lives where)
- How they interact (major request paths)

**Example:**
```
- Web API (Node.js) handles HTTP requests
- Redis stores rate limit counters (shared across API instances)
- PostgreSQL stores user data and sessions
- Request flow: Client → Load Balancer → API → Auth check → Rate limit check → Business logic
```

---

### Components

**Purpose:** Describe major components and their responsibilities.

**Content for each component:**
- Responsibility: What it does
- Key interfaces: Endpoints/events/jobs
- State ownership: What data it owns

**Example:**
```
**Auth Service**
- Responsibility: Handle OAuth flow and session management
- Key interfaces:
  - GET /auth/login - Initiate OAuth flow
  - GET /auth/callback - Handle OAuth callback
  - POST /auth/logout - Terminate session
- State ownership: User records, session tokens

**Rate Limiter**
- Responsibility: Enforce request rate limits
- Key interfaces: Middleware function called on every request
- State ownership: Request counters in Redis
```

---

### Data Model

**Purpose:** Define core entities and relationships.

**Content:**
- Main objects/resources
- Identifiers
- Key constraints (uniqueness, retention, lifecycle)

**Example:**
```
**User**
- id (UUID, primary key)
- github_id (integer, unique, indexed)
- email (string, unique)
- created_at (timestamp)

**Session**
- id (UUID, primary key)
- user_id (UUID, foreign key to User)
- token (string, unique, indexed)
- expires_at (timestamp)
- Constraint: Sessions expire after 7 days
```

---

### Data Flow

**Purpose:** Show how data moves through the system for important scenarios.

**Content:**
- Bullet flows for key scenarios
- Happy path
- Important failure paths

**Example:**
```
**Login Flow (Happy Path)**
1. User clicks "Login with GitHub"
2. API redirects to GitHub OAuth
3. User authorizes
4. GitHub redirects to callback with code
5. API exchanges code for token
6. API creates/updates user record
7. API creates session
8. API redirects to application with session cookie

**Login Flow (Rate Limited)**
1. User clicks "Login with GitHub"
2. API checks rate limit in Redis
3. Limit exceeded → return HTTP 429 with Retry-After header
4. User sees rate limit error
```

---

### External Integrations

**Purpose:** Document how we interact with external systems.

**Content for each integration:**
- Purpose: Why we integrate
- Interaction pattern: Sync/async, request/response, events
- Key constraints: Timeouts, retries, auth, rate limits

**Example:**
```
**GitHub OAuth**
- Purpose: User authentication
- Interaction pattern: Synchronous OAuth 2.0 flow
- Key constraints:
  - 5000 requests/hour rate limit
  - 10 second timeout on token exchange
  - Retry once on 5xx errors
  - OAuth app credentials stored in AWS Secrets Manager
```

---

### Non-Functional Considerations

**Purpose:** Call out important non-functional aspects that affect design.

**Include only what matters:**
- Security: Authentication, authorization, input validation, secrets
- Observability: Logging, metrics, tracing, alerting
- Performance: Response times, throughput, caching
- Reliability: Error handling, retries, circuit breakers
- Scalability: Horizontal/vertical scaling, bottlenecks
- Data Integrity: Consistency, transactions, idempotency
- Compliance: Data privacy, audit logs, retention

**Example:**
```
**Security**
- Session tokens are cryptographically random (32 bytes)
- OAuth credentials stored in AWS Secrets Manager
- All endpoints require HTTPS

**Observability**
- Log all authentication attempts with user_id and outcome
- Track rate limit hits as metrics
- Alert on authentication error rate >5%

**Performance**
- Target p95 response time <200ms for auth endpoints
- Redis provides sub-millisecond rate limit checks
```

---

### Key Decisions

**Purpose:** Document important choices and their rationale.

**Content:**
- Short list of significant decisions
- Brief rationale for each

**Example:**
```
- **Chose Redis for rate limiting:** Provides atomic operations, TTL support, 
  sub-millisecond latency, and works across multiple API instances

- **Session storage in PostgreSQL:** Allows querying active sessions, supports 
  session revocation, provides durability guarantees

- **Token bucket algorithm:** Provides smoother rate limiting than fixed windows, 
  allows brief bursts while maintaining average rate
```

---

### Risks / Open Questions

**Purpose:** Surface uncertainties and trade-offs before implementation.

**Content:**
- Known risks
- Assumptions being made
- Questions to resolve

**Example:**
```
**Risks:**
- GitHub OAuth rate limits could affect high-traffic periods
- Redis single point of failure (mitigated by Redis cluster)

**Assumptions:**
- Users will not share session tokens
- GitHub OAuth will remain available (99.9% SLA)

**Open Questions:**
- What happens to sessions when user revokes GitHub access?
- Should we implement refresh tokens for long-lived sessions?
```

---

## Section Selection Guide

Choose sections based on the type of work:

**Small feature addition:**
- Overview
- Components
- Data Flow

**New service/application:**
- Most or all sections

**Infrastructure change:**
- Overview
- Architecture
- Technical Stack
- Key Decisions

**Integration:**
- Overview
- External Integrations
- Data Flow
- Non-Functional Considerations

**Refactoring:**
- Overview
- Components
- Key Decisions
- Risks

**Bug fix (if planning needed):**
- Overview
- Data Flow (current vs. fixed)
- Key Decisions

---

## Complete Example

```
# Technical Design: GitHub OAuth Authentication Service

## Overview

Build an authentication service that handles GitHub OAuth login with rate limiting 
to prevent abuse. The service will manage user sessions and enforce rate limits on 
authentication attempts.

## Technical Stack

- Runtime: Node.js
- Framework: Express
- Data Storage: PostgreSQL (users, sessions), Redis (rate limits)
- Auth Provider: GitHub OAuth
- Infrastructure: Docker containers

## Architecture

- Web API (Node.js) handles HTTP requests
- Redis stores rate limit counters
- PostgreSQL stores user data and sessions
- Request flow: Client → API → Auth check → Rate limit check → Business logic

## Data Flow

**Login Flow (Happy Path)**
1. User clicks "Login with GitHub"
2. API redirects to GitHub OAuth
3. User authorizes
4. GitHub redirects to callback with code
5. API exchanges code for token
6. API creates/updates user record
7. API creates session
8. API redirects to application with session cookie

## Key Decisions

- **Chose Redis for rate limiting:** Provides atomic operations, TTL support, 
  sub-millisecond latency
- **Session storage in PostgreSQL:** Allows querying active sessions, supports 
  session revocation

## Risks / Open Questions

**Risks:**
- GitHub OAuth rate limits could affect high-traffic periods

**Open Questions:**
- What happens to sessions when user revokes GitHub access?
```
