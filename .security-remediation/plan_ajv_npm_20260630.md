## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 6.14.0`
**Breaking change:** No
**GHSAs:** GHSA-2g4f-4pwh-qvx6

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `ajv` |
| Ecosystem | `npm` |
| Vulnerable range | `< 6.14.0` |
| Patched vulnerable package version | `6.14.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 6.14.0` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, eslint@6.8.0, node-sass@7.0.3, raw-loader@4.0.2, sass-loader@10.5.2, vue-cli-plugin-vuetify@2.0.9, har-validator@5.1.5, schema-utils@1.0.0, schema-utils@2.7.0, schema-utils@2.7.1, schema-utils@3.1.1, schema-utils@3.3.0, table@5.4.6, webpack@4.47.0 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `ajv` |
| Vulnerable range | `< 6.14.0` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-router@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, eslint@6.8.0, node-sass@7.0.3, raw-loader@4.0.2, sass-loader@10.5.2, vue-cli-plugin-vuetify@2.0.9, har-validator@5.1.5, schema-utils@1.0.0, schema-utils@2.7.0, schema-utils@2.7.1, schema-utils@3.1.1, schema-utils@3.3.0, table@5.4.6, webpack@4.47.0 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 6.14.0` |

### Vulnerability summary
- **GHSA-2g4f-4pwh-qvx6** (CVSS 0.0) — ajv has ReDoS when using `$data` option

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 6.14.0` manually

### Notes
_Add context, blockers, or migration hints here._
