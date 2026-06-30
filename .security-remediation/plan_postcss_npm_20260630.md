## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 8.5.10`
**Breaking change:** No
**GHSAs:** GHSA-qx2v-qp2m-jg93, GHSA-7fh5-64p2-3v2j

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `postcss` |
| Ecosystem | `npm` |
| Vulnerable range | `< 8.5.10` |
| Patched vulnerable package version | `8.5.10` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 8.5.10` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, vue-fontawesome-icon@1.3.0, vue-fontawesome@0.0.2, vue@2.7.16, @vue/cli-service@4.5.19, @intervolga/optimize-cssnano-plugin@1.0.6, @vue/component-compiler-utils@3.3.0, autoprefixer@9.8.8, css-declaration-sorter@4.0.1, css-loader@3.6.0, cssnano-preset-default@4.0.8, cssnano-util-raw-cache@4.0.1, cssnano@4.1.11, icss-utils@4.1.1, postcss-calc@7.0.5, postcss-colormin@4.0.3, postcss-convert-values@4.0.1, postcss-discard-comments@4.0.2, postcss-discard-duplicates@4.0.2, postcss-discard-empty@4.0.1, postcss-discard-overridden@4.0.1, postcss-loader@3.0.0, postcss-merge-longhand@4.0.11, postcss-merge-rules@4.0.3, postcss-minify-font-values@4.0.2, postcss-minify-gradients@4.0.2, postcss-minify-params@4.0.2, postcss-minify-selectors@4.0.2, postcss-modules-extract-imports@2.0.0, postcss-modules-local-by-default@3.0.3, postcss-modules-scope@2.2.0, postcss-modules-values@3.0.0, postcss-normalize-charset@4.0.1, postcss-normalize-display-values@4.0.2, postcss-normalize-positions@4.0.2, postcss-normalize-repeat-style@4.0.2, postcss-normalize-string@4.0.2, postcss-normalize-timing-functions@4.0.2, postcss-normalize-unicode@4.0.1, postcss-normalize-url@4.0.1, postcss-normalize-whitespace@4.0.2, postcss-ordered-values@4.1.2, postcss-reduce-initial@4.0.3, postcss-reduce-transforms@4.0.2, postcss-svgo@4.0.3, postcss-unique-selectors@4.0.1, stylehacks@4.0.3, @vue/compiler-sfc@2.7.16, @vue/compiler-sfc@3.4.33 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `postcss` |
| Vulnerable range | `< 8.5.10` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, vue-fontawesome-icon@1.3.0, vue-fontawesome@0.0.2, vue@2.7.16, @vue/cli-service@4.5.19, @intervolga/optimize-cssnano-plugin@1.0.6, @vue/component-compiler-utils@3.3.0, autoprefixer@9.8.8, css-declaration-sorter@4.0.1, css-loader@3.6.0, cssnano-preset-default@4.0.8, cssnano-util-raw-cache@4.0.1, cssnano@4.1.11, icss-utils@4.1.1, postcss-calc@7.0.5, postcss-colormin@4.0.3, postcss-convert-values@4.0.1, postcss-discard-comments@4.0.2, postcss-discard-duplicates@4.0.2, postcss-discard-empty@4.0.1, postcss-discard-overridden@4.0.1, postcss-loader@3.0.0, postcss-merge-longhand@4.0.11, postcss-merge-rules@4.0.3, postcss-minify-font-values@4.0.2, postcss-minify-gradients@4.0.2, postcss-minify-params@4.0.2, postcss-minify-selectors@4.0.2, postcss-modules-extract-imports@2.0.0, postcss-modules-local-by-default@3.0.3, postcss-modules-scope@2.2.0, postcss-modules-values@3.0.0, postcss-normalize-charset@4.0.1, postcss-normalize-display-values@4.0.2, postcss-normalize-positions@4.0.2, postcss-normalize-repeat-style@4.0.2, postcss-normalize-string@4.0.2, postcss-normalize-timing-functions@4.0.2, postcss-normalize-unicode@4.0.1, postcss-normalize-url@4.0.1, postcss-normalize-whitespace@4.0.2, postcss-ordered-values@4.1.2, postcss-reduce-initial@4.0.3, postcss-reduce-transforms@4.0.2, postcss-svgo@4.0.3, postcss-unique-selectors@4.0.1, stylehacks@4.0.3, @vue/compiler-sfc@2.7.16, @vue/compiler-sfc@3.4.33 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 8.5.10` |

### Vulnerability summary
- **GHSA-qx2v-qp2m-jg93** (CVSS 6.1) — PostCSS has XSS via Unescaped </style> in its CSS Stringify Output
- **GHSA-7fh5-64p2-3v2j** (CVSS 5.3) — PostCSS line return parsing error

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 8.5.10` manually

### Notes
_Add context, blockers, or migration hints here._
