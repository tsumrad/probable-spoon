## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-service` to `>= 5.3.4`
**Breaking change:** No
**GHSAs:** GHSA-wr3j-pwj9-hqq6

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `webpack-dev-middleware` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 5.3.3` |
| Patched vulnerable package version | `5.3.4` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 5.3.4` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, webpack-dev-server@3.11.3 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `webpack-dev-middleware` |
| Vulnerable range | `<= 5.3.3` |
| Pulled in via | @vue/cli-service@4.5.19, webpack-dev-server@3.11.3 |
| Fix: upgrade source to | `@vue/cli-service >= 5.3.4` |

### Vulnerability summary
- **GHSA-wr3j-pwj9-hqq6** (CVSS 7.4) — Path traversal in webpack-dev-middleware

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 5.3.4` manually

### Notes
_Add context, blockers, or migration hints here._
