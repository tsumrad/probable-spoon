## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-service` to `>= 2.0.10`
**Breaking change:** No
**GHSAs:** GHSA-64mm-vxmg-q3vj, GHSA-4www-5p9h-95mh

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `http-proxy-middleware` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 0.16.0, < 2.0.10` |
| Patched vulnerable package version | `2.0.10` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 2.0.10` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, webpack-dev-server@3.11.3, @types/webpack-dev-server@3.11.6 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `http-proxy-middleware` |
| Vulnerable range | `>= 0.16.0, < 2.0.10` |
| Pulled in via | @vue/cli-service@4.5.19, webpack-dev-server@3.11.3, @types/webpack-dev-server@3.11.6 |
| Fix: upgrade source to | `@vue/cli-service >= 2.0.10` |

### Vulnerability summary
- **GHSA-64mm-vxmg-q3vj** (CVSS 0.0) — http-proxy-middleware `router` host+path substring matching allows Host-header-driven backend routing bypass
- **GHSA-4www-5p9h-95mh** (CVSS 4.0) — http-proxy-middleware can call writeBody twice because "else if" is not used

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 2.0.10` manually

### Notes
_Add context, blockers, or migration hints here._
