## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** LOW
**Action required:** Bump `@vue/cli-service` to `>= 1.16.0`
**Breaking change:** No
**GHSAs:** GHSA-cm22-4g7w-348p

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `serve-static` |
| Ecosystem | `npm` |
| Vulnerable range | `< 1.16.0` |
| Patched vulnerable package version | `1.16.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 1.16.0` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, express@4.19.2 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `serve-static` |
| Vulnerable range | `< 1.16.0` |
| Pulled in via | @vue/cli-service@4.5.19, express@4.19.2 |
| Fix: upgrade source to | `@vue/cli-service >= 1.16.0` |

### Vulnerability summary
- **GHSA-cm22-4g7w-348p** (CVSS 5.0) — serve-static vulnerable to template injection that can lead to XSS

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 1.16.0` manually

### Notes
_Add context, blockers, or migration hints here._
