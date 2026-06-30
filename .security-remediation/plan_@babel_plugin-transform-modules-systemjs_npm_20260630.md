## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 7.29.4`
**Breaking change:** No
**GHSAs:** GHSA-fv7c-fp4j-7gwp

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `@babel/plugin-transform-modules-systemjs` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 7.12.0, <= 7.29.3` |
| Patched vulnerable package version | `7.29.4` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 7.29.4` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @babel/preset-env@7.24.8 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `@babel/plugin-transform-modules-systemjs` |
| Vulnerable range | `>= 7.12.0, <= 7.29.3` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @babel/preset-env@7.24.8 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 7.29.4` |

### Vulnerability summary
- **GHSA-fv7c-fp4j-7gwp** (CVSS 8.2) — @babel/plugin-transform-modules-systemjs generates arbitrary code when compiling malicious input

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 7.29.4` manually

### Notes
_Add context, blockers, or migration hints here._
