# DevSecOps Mini Project – End-to-End Secure CI/CD Pipeline

Project Overview

This project demonstrates a complete DevSecOps security implementation integrating:

- Version Control (GitHub)
- CI/CD Pipeline (GitHub Actions – Self Hosted Runner)
- SAST (Bandit)
- DAST (OWASP ZAP)
- Dockerized Staging Environment
- Centralized Vulnerability Management (DefectDojo)
- Automated API-based Report Aggregation

The objective was to build a fully automated secure software delivery pipeline.

## Architecture

- Developer Commit
      ↓
- GitHub CI/CD
      ↓
- SAST – Bandit
      ↓
- Docker Build & Staging Deployment
      ↓
- DAST – OWASP ZAP
      ↓
- Report Generation (JSON/XML)
      ↓
- DefectDojo API Import
      ↓
- Unified Security Dashboard

## Week Breakdown

## Week 1 – Security Gate & CI Setup

- Configured GitHub CI pipeline
- Defined security gate policy
- Implemented pre-commit scanning logic
- Validated pipeline execution

## Week 2 – Static Application Security Testing (SAST)

- Integrated Bandit into CI pipeline
- Injected vulnerable code
- Generated JSON report
- Validated vulnerability detection

## Week 3 – Dynamic Application Security Testing (DAST)

- Containerized Flask application using Docker
- Deployed staging environment
- Introduced XSS vulnerability
- Executed OWASP ZAP full scan
- Generated XML security report

Detected:

- Reflected XSS
- Missing security headers
- Medium and Low risk findings

## Week 4 – Reporting & Aggregation

- Automated upload of SAST + DAST reports to DefectDojo
- Used secure API token authentication
- Linked scans to single engagement
- Created unified vulnerability dashboard
- Generated executive-level security health overview

DefectDojo dashboard now displays:

- High severity vulnerabilities
- Medium severity findings
- Low severity misconfigurations
- Informational issues

## Security Health Summary

The application currently contains exploitable vulnerabilities, including:

- Cross-Site Scripting (XSS)
- Injection risks
- Security header misconfigurations

The integrated pipeline ensures:

- Continuous security validation
- Automated vulnerability detection
- Centralized risk visibility
- Governance and compliance readiness

## Technologies Used

1. Python
2. Flask
3. Docker
4. GitHub Actions (Self-hosted Runner)
5. Bandit
6. OWASP ZAP
7. DefectDojo
8. REST API Integration

## Final Outcome

- Fully automated DevSecOps pipeline
- SAST and DAST integration
- Dockerized staging environment
- Centralized vulnerability aggregation
- Executive-level security reporting

Project successfully demonstrates secure CI/CD orchestration in a real-world DevSecOps workflow.
