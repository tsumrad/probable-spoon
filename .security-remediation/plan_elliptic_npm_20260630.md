## Security remediation — @vue/cli-plugin-babel (npm) [transitive]

**Severity:** CRITICAL
**Action required:** Bump `@vue/cli-plugin-babel` to `>= 6.6.1`
**Breaking change:** No
**GHSAs:** GHSA-848j-6mx2-7j84, GHSA-vjh7-7g9h-fjfh, GHSA-fc9h-whq2-v747, GHSA-49q7-c7j4-3p7m, GHSA-977x-g7h5-7qgw, GHSA-f7q4-pwc6-w24p

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `elliptic` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 6.6.1` |
| Patched vulnerable package version | `6.6.1` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-plugin-babel` |
| Required source version | `>= 6.6.1` |
| Source candidates from dependency graph | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, browserify-sign@4.2.3, create-ecdh@4.0.4 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `elliptic` |
| Vulnerable range | `<= 6.6.1` |
| Pulled in via | @vue/cli-plugin-babel@4.5.19, @vue/cli-plugin-eslint@4.5.19, @vue/cli-plugin-typescript@4.5.19, @vue/cli-service@4.5.19, browserify-sign@4.2.3, create-ecdh@4.0.4 |
| Fix: upgrade source to | `@vue/cli-plugin-babel >= 6.6.1` |

### Vulnerability summary
- **GHSA-848j-6mx2-7j84** (CVSS 5.6) — Elliptic Uses a Cryptographic Primitive with a Risky Implementation
- **GHSA-vjh7-7g9h-fjfh** (CVSS 0.0) — Elliptic's private key extraction in ECDSA upon signing a malformed input (e.g. a string)
- **GHSA-fc9h-whq2-v747** (CVSS 4.8) — Valid ECDSA signatures erroneously rejected in Elliptic
- **GHSA-49q7-c7j4-3p7m** (CVSS 5.3) — Elliptic allows BER-encoded signatures
- **GHSA-977x-g7h5-7qgw** (CVSS 5.3) — Elliptic's ECDSA missing check for whether leading bit of r and s is zero
- **GHSA-f7q4-pwc6-w24p** (CVSS 5.3) — Elliptic's EDDSA missing signature length check

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-plugin-babel` to `>= 6.6.1` manually

### Notes
_Add context, blockers, or migration hints here._
