## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 6.15.2`
**Breaking change:** No
**GHSAs:** GHSA-q8mj-m7cp-5q26, GHSA-w7fw-mjwx-w883, GHSA-6rw7-vpxm-498p

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `qs` |
| Ecosystem | `npm` |
| Vulnerable range | `>= 6.11.1, <= 6.15.1` |
| Patched vulnerable package version | `6.15.2` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 6.15.2` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, url@0.11.3 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `qs` |
| Vulnerable range | `>= 6.11.1, <= 6.15.1` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, url@0.11.3 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 6.15.2` |

### Vulnerability summary
- **GHSA-q8mj-m7cp-5q26** (CVSS 5.3) — qs has a remotely triggerable DoS: qs.stringify crashes with TypeError on null/undefined entries in comma-format arrays when encodeValuesOnly is set
- **GHSA-w7fw-mjwx-w883** (CVSS 3.7) — qs's arrayLimit bypass in comma parsing allows denial of service
- **GHSA-6rw7-vpxm-498p** (CVSS 3.7) — qs's arrayLimit bypass in its bracket notation allows DoS via memory exhaustion

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 6.15.2` manually

### Notes
_Add context, blockers, or migration hints here._
