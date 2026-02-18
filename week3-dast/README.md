# Week 3 – Dynamic Application Security Testing (DAST)

This task demonstrates runtime vulnerability detection using OWASP ZAP.

## Objective

- Containerize the target application
- Deploy it to a staging environment
- Perform Spider and Active Scan using OWASP ZAP
- Verify detection of intentionally introduced vulnerability

## Implementation

1. Containerized Flask application using Docker
2. Deployed locally on port 5000
3. Introduced reflected XSS vulnerability in /search endpoint
4. Executed OWASP ZAP full scan against staging URL
5. Generated HTML report (zap-report.html)

## Vulnerabilities Detected

- Reflected Cross-Site Scripting (XSS)
- DOM-Based XSS
- Missing Security Headers (CSP, CORS)

## Outcome

ZAP successfully identified the intentionally introduced XSS vulnerability in the staging build, validating DAST implementation.
