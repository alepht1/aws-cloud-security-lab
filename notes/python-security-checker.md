# Python AWS S3 Security Checker

## Overview

This project extends the AWS Cloud Security Lab with a Python script that uses boto3 to inspect S3 bucket security configurations.

The script performs read-only checks and prints a human-readable report.

## Security Checks

1. **Block Public Access:** Checks all four bucket-level S3 Block Public Access settings.
2. **Encryption:** Checks whether an explicit default bucket encryption configuration exists.
3. **Versioning:** Checks whether S3 Versioning is enabled.

## Tools

- Python
- boto3
- AWS CloudShell
- Amazon S3
- Git and GitHub

## Testing Environment

- AWS Region: us-east-2
- Test bucket: cloud-security-lab-at-2026
- Execution environment: AWS CloudShell
- Authentication: AWS temporary role credentials provided by CloudShell

## Testing Procedure

1. Created the Python script locally on macOS.
2. Validated Python syntax using `python -m py_compile`.
3. Uploaded the script to AWS CloudShell.
4. Verified AWS authentication and S3 bucket access.
5. Executed the script against the existing S3 bucket.
6. Saved the output to `s3-security-report.txt`.

## Observed Results

| Security Check | Result |
|---|---|
| BlockPublicAcls | PASS |
| IgnorePublicAcls | PASS |
| BlockPublicPolicy | PASS |
| RestrictPublicBuckets | PASS |
| Default encryption (AES256) | PASS |
| S3 Versioning | PASS |

All six inspected settings passed during the live test on October 19, 2026.

## Limitations

- The script checks only one predefined S3 bucket.
- It checks bucket-level Block Public Access settings, not account-level settings.
- It does not analyze bucket policies, IAM policies, access points, or cross-account permissions.
- It checks default encryption configuration, not the encryption state of every stored object.
- It does not inspect CloudTrail logging, access logging, or threat detection.
- API permission errors may prevent checks from completing.
- A PASS result does not guarantee that a bucket is completely secure.
- The script does not currently generate JSON reports or an overall summary.

## Future Improvements

- Accept bucket names as command-line arguments.
- Add JSON report export.
- Support scanning multiple buckets.
- Add automated unit tests using mocked AWS API responses.
- Improve error handling and exit codes.
