## Security remediation — @vue/cli-plugin-typescript (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-plugin-typescript` to `>= 4.0.8`
**Breaking change:** No
**GHSAs:** GHSA-952p-6rrq-rcjv

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `micromatch` |
| Ecosystem | `npm` |
| Vulnerable range | `< 4.0.8` |
| Patched vulnerable package version | `4.0.8` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-typescript` |
| Required source version | `>= 4.0.8` |
| Source candidates from dependency graph | @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, ts-loader@6.2.2, @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, anymatch@2.0.0, fast-glob@2.2.7, fork-ts-checker-webpack-plugin@3.1.1, http-proxy-middleware@0.19.1, readdirp@2.2.1, webpack@4.47.0, http-proxy-middleware@1.3.1 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `micromatch` |
| Vulnerable range | `< 4.0.8` |
| Pulled in via | @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, ts-loader@6.2.2, @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, anymatch@2.0.0, fast-glob@2.2.7, fork-ts-checker-webpack-plugin@3.1.1, http-proxy-middleware@0.19.1, readdirp@2.2.1, webpack@4.47.0, http-proxy-middleware@1.3.1 |
| Fix: upgrade source to | `@vue/cli-plugin-typescript >= 4.0.8` |

### Vulnerability summary
- **GHSA-952p-6rrq-rcjv** (CVSS 5.3) — Regular Expression Denial of Service (ReDoS) in micromatch

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-typescript` to `>= 4.0.8` manually

### Notes
_Add context, blockers, or migration hints here._
