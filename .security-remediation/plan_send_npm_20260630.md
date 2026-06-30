## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** LOW
**Action required:** Bump `@vue/cli-service` to `>= 0.19.0`
**Breaking change:** No
**GHSAs:** GHSA-m6fv-jmcg-4jfg

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `send` |
| Ecosystem | `npm` |
| Vulnerable range | `< 0.19.0` |
| Patched vulnerable package version | `0.19.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 0.19.0` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, express@4.19.2, serve-static@1.15.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `send` |
| Vulnerable range | `< 0.19.0` |
| Pulled in via | @vue/cli-service@4.5.19, express@4.19.2, serve-static@1.15.0 |
| Fix: upgrade source to | `@vue/cli-service >= 0.19.0` |

### Vulnerability summary
- **GHSA-m6fv-jmcg-4jfg** (CVSS 5.0) — send vulnerable to template injection that can lead to XSS

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 0.19.0` manually

### Notes
_Add context, blockers, or migration hints here._
