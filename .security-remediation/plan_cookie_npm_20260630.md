## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** LOW
**Action required:** Bump `@vue/cli-service` to `>= 0.7.0`
**Breaking change:** No
**GHSAs:** GHSA-pxg6-pf52-xh8x

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `cookie` |
| Ecosystem | `npm` |
| Vulnerable range | `< 0.7.0` |
| Patched vulnerable package version | `0.7.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 0.7.0` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, express@4.19.2 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `cookie` |
| Vulnerable range | `< 0.7.0` |
| Pulled in via | @vue/cli-service@4.5.19, express@4.19.2 |
| Fix: upgrade source to | `@vue/cli-service >= 0.7.0` |

### Vulnerability summary
- **GHSA-pxg6-pf52-xh8x** (CVSS 0.0) — cookie accepts cookie name, path, and domain with out of bounds characters

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 0.7.0` manually

### Notes
_Add context, blockers, or migration hints here._
