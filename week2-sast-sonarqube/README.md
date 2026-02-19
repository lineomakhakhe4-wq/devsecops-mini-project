# Week 2 – SAST with SonarQube & Bandit

This task demonstrates Static Application Security Testing (SAST) in a CI/CD pipeline.

## 🎯 Objective

- Deploy SonarQube using Docker
- Integrate SAST into GitHub Actions
- Inject a known SQL Injection vulnerability
- Enforce a Quality Gate policy
- Trigger automated security alerts

---

## 🔍 What I Did

- Introduced a deliberate SQL Injection vulnerability
- Deployed SonarQube locally using Docker
- Integrated SonarScanner into GitHub Actions
- Configured a custom Quality Gate (Fail if Vulnerabilities > 0)
- Integrated **Bandit** to enhance Python security detection
- Imported Bandit JSON reports into SonarQube
- Implemented Slack alert on pipeline failure

---

## 🚨 Security Enforcement

- Bandit detects Python security issues
- SonarQube aggregates results
- Quality Gate fails when vulnerabilities exist
- Slack notification triggered on failure

---

## ✅ Outcome

- SQL Injection vulnerability detected
- Quality Gate failed as expected
- Security policy successfully enforced in CI/CD
