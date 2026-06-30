## Security remediation — @typescript-eslint/eslint-plugin (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@typescript-eslint/eslint-plugin` to `>= 1.1.13`
**Breaking change:** No
**GHSAs:** GHSA-f886-m6hf-6m8v, GHSA-v6h2-p8h4-qcjw

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `brace-expansion` |
| Ecosystem | `npm` |
| Vulnerable range | `< 1.1.13` |
| Patched vulnerable package version | `1.1.13` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@typescript-eslint/eslint-plugin` |
| Required source version | `>= 1.1.13` |
| Source candidates from dependency graph | @typescript-eslint/eslint-plugin@2.34.0, @typescript-eslint/parser@2.34.0, @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, eslint@6.8.0, jest@30.3.0, node-sass@7.0.3, vue-cli-plugin-vuetify@2.0.9, minimatch@3.0.4 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `brace-expansion` |
| Vulnerable range | `< 1.1.13` |
| Pulled in via | @typescript-eslint/eslint-plugin@2.34.0, @typescript-eslint/parser@2.34.0, @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, eslint@6.8.0, jest@30.3.0, node-sass@7.0.3, vue-cli-plugin-vuetify@2.0.9, minimatch@3.0.4 |
| Fix: upgrade source to | `@typescript-eslint/eslint-plugin >= 1.1.13` |

### Vulnerability summary
- **GHSA-f886-m6hf-6m8v** (CVSS 6.5) — brace-expansion: Zero-step sequence causes process hang and memory exhaustion
- **GHSA-v6h2-p8h4-qcjw** (CVSS 3.1) — brace-expansion Regular Expression Denial of Service vulnerability

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@typescript-eslint/eslint-plugin` to `>= 1.1.13` manually

### Notes
_Add context, blockers, or migration hints here._
