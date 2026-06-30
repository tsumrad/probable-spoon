## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** LOW
**Action required:** Bump `@vue/cli-service` to `>= 4.20.0`
**Breaking change:** No
**GHSAs:** GHSA-qw6h-vgh9-j6wx

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `express` |
| Ecosystem | `npm` |
| Vulnerable range | `< 4.20.0` |
| Patched vulnerable package version | `4.20.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 4.20.0` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, webpack-bundle-analyzer@3.9.0, webpack-dev-server@3.11.3 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `express` |
| Vulnerable range | `< 4.20.0` |
| Pulled in via | @vue/cli-service@4.5.19, webpack-bundle-analyzer@3.9.0, webpack-dev-server@3.11.3 |
| Fix: upgrade source to | `@vue/cli-service >= 4.20.0` |

### Vulnerability summary
- **GHSA-qw6h-vgh9-j6wx** (CVSS 5.0) — express vulnerable to XSS via response.redirect()

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 4.20.0` manually

### Notes
_Add context, blockers, or migration hints here._
