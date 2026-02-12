# Week 1 – Secret Scanning (TruffleHog)

This task demonstrates secret detection in a CI pipeline.

## What I did

- Added a fake AWS access key
- Configured TruffleHog in GitHub Actions
- Pipeline fails when secrets are detected

### Outcome

- ❌ Build fails when secret exists
- ✅ Build passes after removal

This simulates real-world secret leakage prevention.

## Security Gate Policy

- Zero hardcoded secrets allowed
- TruffleHog must block commits locally
- CI must fail if secrets are detected
