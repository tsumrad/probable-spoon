## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** CRITICAL
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 2.0.3`
**Breaking change:** No
**GHSAs:** GHSA-3rfm-jhwj-7488, GHSA-hhq3-ff78-jv3g, GHSA-76p3-8jx3-jpfq

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `loader-utils` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 1.0.0, < 1.4.2` |
| Patched vulnerable package version | `2.0.3` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 2.0.3` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, ts-loader@6.2.2, vue-cli-plugin-vuetify@2.0.9, cache-loader@4.1.0, copy-webpack-plugin@5.1.2, css-loader@3.6.0, eslint-loader@2.2.1, file-loader@4.3.0, mini-css-extract-plugin@0.9.0, null-loader@3.0.0, postcss-loader@3.0.0, thread-loader@2.1.3, url-loader@2.3.0, vue-loader@15.11.1, vue-style-loader@4.1.3, webpack@4.47.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `loader-utils` |
| Vulnerable range | `>= 1.0.0, < 1.4.2` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, ts-loader@6.2.2, vue-cli-plugin-vuetify@2.0.9, cache-loader@4.1.0, copy-webpack-plugin@5.1.2, css-loader@3.6.0, eslint-loader@2.2.1, file-loader@4.3.0, mini-css-extract-plugin@0.9.0, null-loader@3.0.0, postcss-loader@3.0.0, thread-loader@2.1.3, url-loader@2.3.0, vue-loader@15.11.1, vue-style-loader@4.1.3, webpack@4.47.0 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 2.0.3` |

### Vulnerability summary
- **GHSA-3rfm-jhwj-7488** (CVSS 7.5) — loader-utils is vulnerable to Regular Expression Denial of Service (ReDoS) via url variable
- **GHSA-hhq3-ff78-jv3g** (CVSS 7.5) — loader-utils is vulnerable to Regular Expression Denial of Service (ReDoS)
- **GHSA-76p3-8jx3-jpfq** (CVSS 9.8) — Prototype pollution in webpack loader-utils

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 2.0.3` manually

### Notes
_Add context, blockers, or migration hints here._
