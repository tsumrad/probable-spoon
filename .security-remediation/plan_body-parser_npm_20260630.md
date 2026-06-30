## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-service` to `>= 1.20.3`
**Breaking change:** No
**GHSAs:** GHSA-qwcr-r2fm-qrc7

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `body-parser` |
| Ecosystem | `npm` |
| Vulnerable range | `< 1.20.3` |
| Patched vulnerable package version | `1.20.3` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 1.20.3` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, express@4.19.2 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `body-parser` |
| Vulnerable range | `< 1.20.3` |
| Pulled in via | @vue/cli-service@4.5.19, express@4.19.2 |
| Fix: upgrade source to | `@vue/cli-service >= 1.20.3` |

### Vulnerability summary
- **GHSA-qwcr-r2fm-qrc7** (CVSS 7.5) — body-parser vulnerable to denial of service when url encoding is enabled

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 1.20.3` manually

### Notes
_Add context, blockers, or migration hints here._
