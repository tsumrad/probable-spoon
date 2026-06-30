## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 2.2.2`
**Breaking change:** No
**GHSAs:** GHSA-9c47-m6qq-7p4h

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `json5` |
| Ecosystem | `npm` |
| Vulnerable range | `< 1.0.2` |
| Patched vulnerable package version | `2.2.2` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 2.2.2` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, raw-loader@4.0.2, sass-loader@10.5.2, ts-loader@6.2.2, vue-cli-plugin-vuetify@2.0.9, loader-utils@0.2.17, loader-utils@1.4.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `json5` |
| Vulnerable range | `< 1.0.2` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, raw-loader@4.0.2, sass-loader@10.5.2, ts-loader@6.2.2, vue-cli-plugin-vuetify@2.0.9, loader-utils@0.2.17, loader-utils@1.4.0 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 2.2.2` |

### Vulnerability summary
- **GHSA-9c47-m6qq-7p4h** (CVSS 7.1) — Prototype Pollution in JSON5 via Parse Method

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 2.2.2` manually

### Notes
_Add context, blockers, or migration hints here._
