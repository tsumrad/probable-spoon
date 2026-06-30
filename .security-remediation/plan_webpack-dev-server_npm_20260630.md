## Security remediation — @vue/cli-service (npm) [transitive]

**Severity:** MEDIUM
**Action required:** Bump `@vue/cli-service` to `>= 5.2.5`
**Breaking change:** No
**GHSAs:** GHSA-mx8g-39q3-5c79, GHSA-79cf-xcqc-c78w, GHSA-9jgg-88mc-972h, GHSA-4v9v-hfq4-rm2v

### Issue details

| Field | Value |
|---|---|
| Vulnerable package | `webpack-dev-server` |
| Ecosystem | `npm` |
| Vulnerable range | `< 5.2.5` |
| Patched vulnerable package version | `5.2.5` |
| Relationship | `transitive` |

### Source details

| Field | Value |
|---|---|
| Source package to update | `@vue/cli-service` |
| Required source version | `>= 5.2.5` |
| Source candidates from dependency graph | @vue/cli-service@4.5.19 |

### Transitive vulnerability chain

| Field | Value |
|---|---|
| Vulnerable package | `webpack-dev-server` |
| Vulnerable range | `< 5.2.5` |
| Pulled in via | @vue/cli-service@4.5.19 |
| Fix: upgrade source to | `@vue/cli-service >= 5.2.5` |

### Vulnerability summary
- **GHSA-mx8g-39q3-5c79** (CVSS 5.3) — webpack-dev-server vulnerable to HMR WebSocket interception via permissive user proxies
- **GHSA-79cf-xcqc-c78w** (CVSS 5.3) — webpack-dev-server vulnerable to cross-origin source code exposure on non-HTTPS origins
- **GHSA-9jgg-88mc-972h** (CVSS 6.5) — webpack-dev-server users' source code may be stolen when they access a malicious web site with non-Chromium based browser
- **GHSA-4v9v-hfq4-rm2v** (CVSS 5.3) — webpack-dev-server users' source code may be stolen when they access a malicious web site

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — bump `@vue/cli-service` to `>= 5.2.5` manually

### Notes
_Add context, blockers, or migration hints here._
