## Security remediation — fastapi-sqlalchemy (pip) [transitive]

**Severity:** HIGH
**Action required:** Bump `fastapi-sqlalchemy` to `>= 1.3.1`
**Breaking change:** No
**GHSAs:** GHSA-82w8-qh3p-5jfq, GHSA-jp82-jpqv-5vv3, GHSA-wqp7-x3pw-xc5r, GHSA-x746-7m8f-x49c, GHSA-86qp-5c8j-p5mr

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `starlette` |
| Ecosystem | `pip` |
| Vulnerable range | `>= 0.4.1, < 1.3.1` |
| Patched vulnerable package version | `1.3.1` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `fastapi-sqlalchemy` |
| Required source version | `>= 1.3.1` |
| Source candidates from dependency graph | fastapi-sqlalchemy@0.2.1, fastapi@0.125.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `starlette` |
| Vulnerable range | `>= 0.4.1, < 1.3.1` |
| Pulled in via | fastapi-sqlalchemy@0.2.1, fastapi@0.125.0 |
| Fix: upgrade source to | `fastapi-sqlalchemy >= 1.3.1` |

### Vulnerability summary
- **GHSA-82w8-qh3p-5jfq** (CVSS 7.5) — Starlette: request.form() limits silently ignored for application/x-www-form-urlencoded enable DoS
- **GHSA-jp82-jpqv-5vv3** (CVSS 3.7) — Starlette: Unvalidated request path concatenated into authority poisons request.url.hostname
- **GHSA-wqp7-x3pw-xc5r** (CVSS 7.5) — Starlette: SSRF and NTLM credential theft via UNC paths in StaticFiles on Windows
- **GHSA-x746-7m8f-x49c** (CVSS 5.3) — Starlette: Arbitrary HTTP method dispatched to `HTTPEndpoint` attributes via `getattr`
- **GHSA-86qp-5c8j-p5mr** (CVSS 6.5) — Starlette has missing Host header validation that poisons request.url.path, bypassing path-based security checks

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `fastapi-sqlalchemy` to `>= 1.3.1` manually

### Notes
_Add context, blockers, or migration hints here._
