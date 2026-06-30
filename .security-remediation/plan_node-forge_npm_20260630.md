## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** HIGH
**Action required:** Bump `@vue/cli-service` to `>= 1.4.0`
**Breaking change:** No
**GHSAs:** GHSA-2328-f5f3-gj25, GHSA-q67f-28xg-22rw, GHSA-ppp5-5v6c-4jwp, GHSA-65ch-62r8-g69g, GHSA-5gfm-wpxj-wjgq, GHSA-2r2c-g63r-vccr, GHSA-x4jg-mjrx-434g, GHSA-cfm4-qjh2-4765, GHSA-8fr3-hfg3-gpgp, GHSA-5rrq-pxf6-6jx5, GHSA-gf8q-jrpm-jvxq

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `node-forge` |
| Ecosystem | `npm` |
| Vulnerable range | `<= 1.3.3` |
| Patched vulnerable package version | `1.4.0` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 1.4.0` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19, selfsigned@1.10.14 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `node-forge` |
| Vulnerable range | `<= 1.3.3` |
| Pulled in via | @vue/cli-service@4.5.19, selfsigned@1.10.14 |
| Fix: upgrade source to | `@vue/cli-service >= 1.4.0` |

### Vulnerability summary
- **GHSA-2328-f5f3-gj25** (CVSS 7.4) — Forge has a basicConstraints bypass in its certificate chain verification (RFC 5280 violation)
- **GHSA-q67f-28xg-22rw** (CVSS 7.5) — Forge has signature forgery in Ed25519 due to missing S > L check
- **GHSA-ppp5-5v6c-4jwp** (CVSS 7.5) — Forge has signature forgery in RSA-PKCS due to ASN.1 extra field  
- **GHSA-65ch-62r8-g69g** (CVSS 0.0) — node-forge is vulnerable to ASN.1 OID Integer Truncation
- **GHSA-5gfm-wpxj-wjgq** (CVSS 8.6) — node-forge has an Interpretation Conflict vulnerability via its ASN.1 Validator Desynchronization
- **GHSA-2r2c-g63r-vccr** (CVSS 5.3) — Improper Verification of Cryptographic Signature in `node-forge`
- **GHSA-x4jg-mjrx-434g** (CVSS 7.5) — Improper Verification of Cryptographic Signature in node-forge
- **GHSA-cfm4-qjh2-4765** (CVSS 7.5) — Improper Verification of Cryptographic Signature in node-forge
- **GHSA-8fr3-hfg3-gpgp** (CVSS 6.1) — Open Redirect in node-forge
- **GHSA-5rrq-pxf6-6jx5** (CVSS 0.0) — Prototype Pollution in node-forge debug API.
- **GHSA-gf8q-jrpm-jvxq** (CVSS 0.0) — URL parsing in node-forge could lead to undesired behavior.

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 1.4.0` manually

### Notes
_Add context, blockers, or migration hints here._
