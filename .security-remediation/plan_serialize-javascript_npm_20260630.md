## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 7.0.3`
**Breaking change:** No
**GHSAs:** GHSA-5c6j-r48x-rmvq

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `serialize-javascript` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 7.0.2` |
| Patched vulnerable package version | `7.0.3` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 7.0.3` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, copy-webpack-plugin@5.1.2, terser-webpack-plugin@1.4.5 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `serialize-javascript` |
| Vulnerable range | `<= 7.0.2` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, copy-webpack-plugin@5.1.2, terser-webpack-plugin@1.4.5 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 7.0.3` |

### Vulnerability summary
- **GHSA-5c6j-r48x-rmvq** (CVSS 8.1) — Serialize JavaScript is Vulnerable to RCE via RegExp.flags and Date.prototype.toISOString()

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 7.0.3` manually

### Notes
_Add context, blockers, or migration hints here._
