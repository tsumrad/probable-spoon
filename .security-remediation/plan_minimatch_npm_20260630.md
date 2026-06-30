## Security remediation — @typescript-eslint/eslint-plugin (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@typescript-eslint/eslint-plugin` to `>= 3.1.4`
**Breaking change:** No
**GHSAs:** GHSA-7r86-cg39-jmmj, GHSA-23c5-xmqv-rm74, GHSA-3ppc-4f35-3m26, GHSA-f8q6-p94x-37v3

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `minimatch` |
| Ecosystem | `npm` |
| Vulnerable range | `< 3.1.3` |
| Patched vulnerable package version | `3.1.4` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@typescript-eslint/eslint-plugin` |
| Required source version | `>= 3.1.4` |
| Source candidates from dependency graph | @typescript-eslint/eslint-plugin@2.34.0, @typescript-eslint/parser@2.34.0, @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, eslint@6.8.0, jest@30.3.0, node-sass@7.0.3, vue-cli-plugin-vuetify@2.0.9, copy-webpack-plugin@5.1.2, fork-ts-checker-webpack-plugin@3.1.1, fork-ts-checker-webpack-plugin@5.2.1, glob@7.1.7, glob@7.2.0, globule@1.3.4, test-exclude@6.0.0, tslint@5.20.1 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `minimatch` |
| Vulnerable range | `< 3.1.3` |
| Pulled in via | @typescript-eslint/eslint-plugin@2.34.0, @typescript-eslint/parser@2.34.0, @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, eslint@6.8.0, jest@30.3.0, node-sass@7.0.3, vue-cli-plugin-vuetify@2.0.9, copy-webpack-plugin@5.1.2, fork-ts-checker-webpack-plugin@3.1.1, fork-ts-checker-webpack-plugin@5.2.1, glob@7.1.7, glob@7.2.0, globule@1.3.4, test-exclude@6.0.0, tslint@5.20.1 |
| Fix: upgrade source to | `@typescript-eslint/eslint-plugin >= 3.1.4` |

### Vulnerability summary
- **GHSA-7r86-cg39-jmmj** (CVSS 7.5) — minimatch has ReDoS: matchOne() combinatorial backtracking via multiple non-adjacent GLOBSTAR segments
- **GHSA-23c5-xmqv-rm74** (CVSS 7.5) — minimatch ReDoS: nested *() extglobs generate catastrophically backtracking regular expressions
- **GHSA-3ppc-4f35-3m26** (CVSS 0.0) — minimatch has a ReDoS via repeated wildcards with non-matching literal in pattern
- **GHSA-f8q6-p94x-37v3** (CVSS 7.5) — minimatch ReDoS vulnerability

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@typescript-eslint/eslint-plugin` to `>= 3.1.4` manually

### Notes
_Add context, blockers, or migration hints here._
