## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** LOW
**Action required:** Bump `@vue/cli-service` to `>= 1.1.0`
**Breaking change:** No
**GHSAs:** GHSA-76c9-3jph-rj3q

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `on-headers` |
| Ecosystem | `npm` |
| Vulnerable range | `< 1.1.0` |
| Patched vulnerable package version | `1.1.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 1.1.0` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, compression@1.7.4 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `on-headers` |
| Vulnerable range | `< 1.1.0` |
| Pulled in via | @vue/cli-service@4.5.19, compression@1.7.4 |
| Fix: upgrade source to | `@vue/cli-service >= 1.1.0` |

### Vulnerability summary
- **GHSA-76c9-3jph-rj3q** (CVSS 3.4) — on-headers is vulnerable to http response header manipulation

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 1.1.0` manually

### Notes
_Add context, blockers, or migration hints here._
