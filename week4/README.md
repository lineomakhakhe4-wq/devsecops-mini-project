# Week 4 – Reporting & Aggregation

This task demonstrates centralized vulnerability management by aggregating SAST and DAST findings into DefectDojo via API.

## Objective

-Feed all security logs (SAST + DAST findings) into DefectDojo
-Use API-based automated import during CI/CD
-Create a unified vulnerability dashboard
-Provide an executive-level "Security Health" overview

## Implementation

-Generated Bandit JSON report during CI pipeline
-Generated OWASP ZAP XML report during DAST stage
-Used DefectDojo API endpoint /api/v2/import-scan/
-Imported:
  Bandit Scan (SAST findings)
  ZAP Scan (DAST findings)
-Linked both scans to a single CI/CD Engagement
Verified findings appear on DefectDojo dashboard

## Findings Aggregated

-High severity vulnerabilities (XSS detected by ZAP)
-Medium severity security issues
-Low severity configuration weaknesses
-Informational findings
-All findings were consolidated into a single engagement for centralized tracking and reporting.

## Executive Security Health Summary

The integrated dashboard provides:
-Severity distribution overview
-Historical vulnerability trends
-Risk visibility for management
-Centralized tracking of remediation status

This enables security governance and supports compliance, audit readiness, and executive reporting.

## Outcome

Security findings from both SAST and DAST were successfully aggregated into DefectDojo via API, producing a unified vulnerability management dashboard and completing the DevSecOps security orchestration workflow.