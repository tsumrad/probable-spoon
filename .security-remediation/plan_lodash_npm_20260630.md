## Security remediation — @typescript-eslint/eslint-plugin (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@typescript-eslint/eslint-plugin` to `>= 4.18.0`
**Breaking change:** No
**GHSAs:** GHSA-r5fr-rjxr-66jc, GHSA-f23m-r3pf-42rh, GHSA-xxjr-mmjv-4gpg

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `lodash` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 4.0.0, <= 4.17.23` |
| Patched vulnerable package version | `4.18.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@typescript-eslint/eslint-plugin` |
| Required source version | `>= 4.18.0` |
| Source candidates from dependency graph | @typescript-eslint/eslint-plugin@2.34.0, @typescript-eslint/parser@2.34.0, @vue/cli-plugin-eslint@4.5.19, @vue/cli-service@4.5.19, @vue/eslint-config-typescript@5.1.0, eslint-plugin-vue@6.2.2, eslint@6.8.0, node-sass@7.0.3, save@2.4.0, @typescript-eslint/typescript-estree@2.34.0, async@2.6.3, async@2.6.4, globule@1.3.4, html-webpack-plugin@3.2.0, http-proxy-middleware@0.19.1, inquirer@7.3.3, pretty-error@2.1.2, renderkid@2.0.7, sass-graph@4.0.1, table@5.4.6, vue-eslint-parser@7.11.0, webpack-bundle-analyzer@3.9.0, webpack-merge@4.2.2 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `lodash` |
| Vulnerable range | `>= 4.0.0, <= 4.17.23` |
| Pulled in via | @typescript-eslint/eslint-plugin@2.34.0, @typescript-eslint/parser@2.34.0, @vue/cli-plugin-eslint@4.5.19, @vue/cli-service@4.5.19, @vue/eslint-config-typescript@5.1.0, eslint-plugin-vue@6.2.2, eslint@6.8.0, node-sass@7.0.3, save@2.4.0, @typescript-eslint/typescript-estree@2.34.0, async@2.6.3, async@2.6.4, globule@1.3.4, html-webpack-plugin@3.2.0, http-proxy-middleware@0.19.1, inquirer@7.3.3, pretty-error@2.1.2, renderkid@2.0.7, sass-graph@4.0.1, table@5.4.6, vue-eslint-parser@7.11.0, webpack-bundle-analyzer@3.9.0, webpack-merge@4.2.2 |
| Fix: upgrade source to | `@typescript-eslint/eslint-plugin >= 4.18.0` |

### Vulnerability summary
- **GHSA-r5fr-rjxr-66jc** (CVSS 8.1) — lodash vulnerable to Code Injection via `_.template` imports key names
- **GHSA-f23m-r3pf-42rh** (CVSS 6.5) — lodash vulnerable to Prototype Pollution via array path bypass in `_.unset` and `_.omit`
- **GHSA-xxjr-mmjv-4gpg** (CVSS 6.5) — Lodash has Prototype Pollution Vulnerability in `_.unset` and `_.omit` functions

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@typescript-eslint/eslint-plugin` to `>= 4.18.0` manually

### Notes
_Add context, blockers, or migration hints here._
