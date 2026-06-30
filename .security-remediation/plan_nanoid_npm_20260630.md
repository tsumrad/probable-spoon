## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 3.3.8`
**Breaking change:** No
**GHSAs:** GHSA-mwcw-c2x4-8c55

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `nanoid` |
| Ecosystem | `npm` |
| Vulnerable range | `< 3.3.8` |
| Patched vulnerable package version | `3.3.8` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 3.3.8` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, vue-fontawesome-icon@1.3.0, vue-fontawesome@0.0.2, vue@2.7.16, postcss@8.4.39 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `nanoid` |
| Vulnerable range | `< 3.3.8` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, vue-fontawesome-icon@1.3.0, vue-fontawesome@0.0.2, vue@2.7.16, postcss@8.4.39 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 3.3.8` |

### Vulnerability summary
- **GHSA-mwcw-c2x4-8c55** (CVSS 4.3) — Predictable results in nanoid generation when given non-integer values

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 3.3.8` manually

### Notes
_Add context, blockers, or migration hints here._
