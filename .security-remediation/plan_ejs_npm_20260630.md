## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** CRITICAL
**Action required:** Bump `@vue/cli-service` to `>= 3.1.10`
**Breaking change:** No
**GHSAs:** GHSA-ghr5-ch3p-vcr6, GHSA-phwq-j96m-2c2q

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `ejs` |
| Ecosystem | `npm` |
| Vulnerable range | `< 3.1.10` |
| Patched vulnerable package version | `3.1.10` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 3.1.10` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, webpack-bundle-analyzer@3.9.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `ejs` |
| Vulnerable range | `< 3.1.10` |
| Pulled in via | @vue/cli-service@4.5.19, webpack-bundle-analyzer@3.9.0 |
| Fix: upgrade source to | `@vue/cli-service >= 3.1.10` |

### Vulnerability summary
- **GHSA-ghr5-ch3p-vcr6** (CVSS 4.0) — ejs lacks certain pollution protection
- **GHSA-phwq-j96m-2c2q** (CVSS 9.8) — ejs template injection vulnerability

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 3.1.10` manually

### Notes
_Add context, blockers, or migration hints here._
