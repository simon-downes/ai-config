---
name: workflow-review
description: >
  Systematically evaluate completed work to ensure it meets requirements and maintains quality standards. Use when reviewing code changes, assessing implementations, verifying requirements are met, checking code quality, evaluating system designs, or conducting quality assessments before deployment.
---

# Purpose

Systematically evaluate completed work to ensure it meets requirements and maintains quality standards.

# When to use

- Reviewing code changes or pull requests
- Assessing completed implementations
- Verifying requirements are satisfied
- Checking code quality before deployment
- Evaluating system designs or architectures
- Conducting quality assessments

# When not to use

- Gathering requirements (use general-requirements-gathering)
- Creating technical designs (use skill-technical-design)
- Learning coding standards (those are in lang-* skills)

# Workflow

1. **Identify what to review**
   - Clarify the scope (specific files, changes, system, etc.)
   - Understand the original requirements or objectives

2. **Requirements Verification**
   - Check deliverables against requirements
   - Verify acceptance criteria are met
   - Identify gaps or deviations

3. **Quality Assessment**
   - Evaluate against quality dimensions
   - Document findings for each dimension
   - Provide specific recommendations

4. **Summarize findings**
   - Present overall assessment
   - Prioritize issues by severity
   - Suggest next steps

# Requirements Verification

## What to Check

- **Deliverable Completeness**: Does each deliverable exist and function as described?
- **Acceptance Criteria**: Are all acceptance criteria satisfied?
- **Requirement Coverage**: Were all MUST requirements implemented? All SHOULD requirements addressed or deferred?
- **Gaps**: Are there missing features or behaviors specified in requirements?
- **Deviations**: Were any requirements modified during implementation?

## Output Format

For each requirement:
- ✅ Met - Acceptance criteria satisfied
- ⚠️ Partially met - Some criteria not satisfied, note what's missing
- ❌ Not met - Requirement not implemented, note why
- 🔄 Modified - Requirement changed during implementation

# Quality Assessment

## Coding Standards

**Check:**
- Does code follow coding rules and guidelines in context?
- Are naming conventions consistent?
- Is code structure appropriate (SOLID, DRY, KISS)?
- Is formatting consistent?

**Look for:**
- Violations of language-specific standards
- Inconsistent patterns compared to existing codebase
- Overly complex or unclear code

## Documentation

**Check:**
- Are functions and classes documented with docstrings?
- Are complex logic sections explained with comments?
- Is README updated if user-facing changes were made?
- Are configuration changes documented?
- Is API documentation updated if endpoints changed?

**Look for:**
- Missing docstrings on public interfaces
- Outdated comments that don't match code
- Undocumented breaking changes
- Missing setup or deployment instructions

## Security

**Check:**
- Are all external inputs validated?
- Are secrets and credentials properly managed (not hardcoded)?
- Are authentication and authorization implemented correctly?
- Are error messages appropriate (not leaking sensitive info)?
- Are dependencies up to date and free of known vulnerabilities?

**Look for:**
- SQL injection, XSS, or other injection vulnerabilities
- Hardcoded passwords, API keys, or tokens
- Overly permissive access controls
- Sensitive data in logs
- Insecure defaults

## Test Coverage

**Check:**
- Are important business logic paths tested?
- Are edge cases and error conditions tested?
- Do tests actually verify behavior (not just exercise code)?
- Are tests maintainable and clear?

**Look for:**
- Critical paths without tests
- Tests that don't assert meaningful outcomes
- Brittle tests that will break with minor changes
- Missing negative test cases

## Error Handling

**Check:**
- Are expected errors handled gracefully?
- Are unexpected errors caught and logged appropriately?
- Do error messages help users/operators understand what happened?
- Are resources cleaned up properly in error paths?

**Look for:**
- Bare except/catch blocks that hide errors
- Errors that crash the application unnecessarily
- Missing error handling in critical paths
- Resource leaks (unclosed files, connections, etc.)

## Performance

**Check:**
- Are there obvious inefficiencies (N+1 queries, unnecessary loops)?
- Are expensive operations cached when appropriate?
- Are database queries optimized?
- Are large datasets handled efficiently?

**Look for:**
- Algorithms with poor time complexity
- Missing indexes on frequently queried fields
- Unnecessary data loading or processing
- Blocking operations that could be async

## Technical Debt

**Check:**
- What shortcuts were taken? Are they documented?
- What refactoring would improve the code?
- Are there TODOs or FIXMEs? Are they tracked?
- Is the debt acceptable given project constraints?

**Look for:**
- Duplicated code that should be abstracted
- Temporary workarounds that became permanent
- Overly complex solutions to simple problems
- Missing abstractions that would improve maintainability

# Assessment Output Format

For each quality dimension, provide:

**Status**: ✅ Good | ⚠️ Concerns | ❌ Issues

**Findings**: Brief description of what was found

**Recommendations**: Specific actions to address concerns or issues (if any)

## Example

**Security**: ⚠️ Concerns
- **Findings**: API keys stored in environment variables (good), but error messages include full request details which may leak sensitive data
- **Recommendations**: Sanitize error responses to exclude sensitive headers and parameters

**Test Coverage**: ✅ Good
- **Findings**: All critical paths tested, edge cases covered, tests are clear and maintainable

# Summary Format

```
# Review Summary

## Requirements Verification
[Status for each requirement]

## Quality Assessment
[Status for each dimension with findings]

## Overall Assessment
[Brief summary of readiness]

## Recommended Actions
1. [Priority issues to address]
2. [Secondary improvements]
```
