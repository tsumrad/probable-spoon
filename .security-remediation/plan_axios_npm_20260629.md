## Security remediation — axios (npm)

**Severity:** HIGH
**Current range:** <= 0.31.1
**Target version:** 0.32.0
**Breaking change:** No
**GHSAs:** GHSA-hfxv-24rg-xrqf, GHSA-p92q-9vqr-4j8v, GHSA-j5f8-grm9-p9fc, GHSA-3g43-6gmg-66jw, GHSA-pjwm-pj3p-43mv, GHSA-898c-q2cr-xwhg, GHSA-m7pr-hjqh-92cm, GHSA-62hf-57xw-28j9, GHSA-5c9x-8gcm-mpgx, GHSA-vf2m-468p-8v99, GHSA-pf86-5x62-jrwf, GHSA-6chq-wfr3-2hj9, GHSA-xx6v-rp6x-q39c, GHSA-w9j2-pvgh-6h63, GHSA-pmwg-cvhr-8vh7, GHSA-xhjh-pmcv-23jw, GHSA-3p68-rc4w-qgx5, GHSA-fvcv-3m26-pcqx, GHSA-43fc-jf86-j433, GHSA-4hjh-wcwx-xvwj, GHSA-jr5f-v2jv-69x6

### Vulnerability summary
- **GHSA-hfxv-24rg-xrqf** (CVSS 7.5) — Axios: Regular Expression Denial of Service (ReDoS) via Cookie Name Injection
- **GHSA-p92q-9vqr-4j8v** (CVSS 0.0) — Axios: Proxy-Authorization Credential Leak to Origin Server Across HTTP-to-HTTPS Redirect in Axios Node.js HTTP Adapter
- **GHSA-j5f8-grm9-p9fc** (CVSS 7.5) — Axios: Proxy-Authorization header leaks to redirect target when proxy is re-evaluated to direct connection
- **GHSA-3g43-6gmg-66jw** (CVSS 7.0) — axios Vulnerable to Credential Theft and Response Hijacking via Prototype Pollution Gadget in Config Merge
- **GHSA-pjwm-pj3p-43mv** (CVSS 8.6) — axios's shouldBypassProxy does not recognize IPv4-mapped IPv6 addresses, allowing NO_PROXY bypass (incomplete fix for CVE-2025-62718)
- **GHSA-898c-q2cr-xwhg** (CVSS 4.8) — axios has DoS & Header Injection via Prototype Pollution Read-Side Gadgets in axios merge functions
- **GHSA-m7pr-hjqh-92cm** (CVSS 6.8) — Axios: no_proxy bypass via IP alias allows SSRF
- **GHSA-62hf-57xw-28j9** (CVSS 7.5) — Axios: unbounded recursion in toFormData causes DoS via deeply nested request data
- **GHSA-5c9x-8gcm-mpgx** (CVSS 5.3) — Axios' HTTP adapter-streamed uploads bypass maxBodyLength when maxRedirects: 0
- **GHSA-vf2m-468p-8v99** (CVSS 5.3) — Axios: HTTP adapter streamed responses bypass maxContentLength
- **GHSA-pf86-5x62-jrwf** (CVSS 7.4) — Axios: Prototype Pollution Gadgets - Response Tampering, Data Exfiltration, and Request Hijacking
- **GHSA-6chq-wfr3-2hj9** (CVSS 7.4) — Axios: Header Injection via Prototype Pollution
- **GHSA-xx6v-rp6x-q39c** (CVSS 5.4) — Axios: XSRF Token Cross-Origin Leakage via Prototype Pollution Gadget in `withXSRFToken` Boolean Coercion
- **GHSA-w9j2-pvgh-6h63** (CVSS 4.8) — Axios: Authentication Bypass via Prototype Pollution Gadget in `validateStatus` Merge Strategy
- **GHSA-pmwg-cvhr-8vh7** (CVSS 7.2) — Axios: Incomplete Fix for CVE-2025-62718 — NO_PROXY Protection Bypassed via RFC 1122 Loopback Subnet (127.0.0.0/8) in Axios 1.15.0
- **GHSA-xhjh-pmcv-23jw** (CVSS 3.7) — Axios: Null Byte Injection via Reverse-Encoding in AxiosURLSearchParams
- **GHSA-3p68-rc4w-qgx5** (CVSS 4.8) — Axios has a NO_PROXY Hostname Normalization Bypass that Leads to SSRF
- **GHSA-fvcv-3m26-pcqx** (CVSS 4.8) — Axios has Unrestricted Cloud Metadata Exfiltration via Header Injection Chain
- **GHSA-43fc-jf86-j433** (CVSS 7.5) — Axios is Vulnerable to Denial of Service via __proto__ Key in mergeConfig
- **GHSA-4hjh-wcwx-xvwj** (CVSS 7.5) — Axios is vulnerable to DoS attack through lack of data size check
- **GHSA-jr5f-v2jv-69x6** (CVSS 0.0) — axios Requests Vulnerable To Possible SSRF and Credential Leakage via Absolute URL

### Resolution options
- [ ] Assign to coding agent (Copilot / LLM) to author the fix PR
- [ ] Self-resolve — implement migration manually

### Notes
_Add context, blockers, or migration hints here._
