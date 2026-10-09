# AWS Cloud Security Lab

## Overview

This hands-on project demonstrates foundational AWS cloud security practices using Amazon S3, AWS IAM, encryption, versioning, and permission testing.

The goal is to secure cloud storage, apply least-privilege access, and verify that security controls behave as expected.

## Architecture

- **Amazon S3:** Private storage bucket for test objects
- **AWS IAM:** Dedicated role with limited S3 permissions
- **AWS STS:** Temporary credentials used to test role permissions
- **Server-side encryption:** SSE-S3 enabled
- **S3 Versioning:** Enabled to help recover previous object versions

## Security Controls

### 1. Block Public Access
Enabled all S3 Block Public Access settings to help prevent unintended public exposure.

### 2. Object Ownership
Configured Bucket owner enforced, which disables ACLs and centralizes access control through policies.

### 3. Encryption at Rest
Enabled default SSE-S3 encryption. Verified that uploaded objects report AES-256 server-side encryption.

### 4. Versioning
Enabled S3 Versioning to preserve object versions and support recovery from accidental changes or deletions.

### 5. IAM Least Privilege
Created the `CloudSecurityLab-S3-Role` role with an inline policy limited to the lab bucket.

Allowed actions:
- `s3:ListBucket`
- `s3:GetObject`
- `s3:PutObject`

The role does not grant `s3:DeleteObject`.

### 6. Permission Testing
Used AWS STS temporary role credentials and the AWS CLI to test access.

| Test | Expected result | Observed result |
|---|---|---|
| List bucket objects | Allowed | Passed |
| Read an object | Allowed | Passed |
| Upload an object | Allowed | Passed |
| Delete an object | Denied | Passed: AccessDenied |

The denied deletion confirms that the role cannot perform an action that was not granted by its identity-based policy.

## Tools Used

- Amazon Web Services (AWS)
- Amazon S3
- AWS Identity and Access Management (IAM)
- AWS Security Token Service (STS)
- AWS CLI
- Git and GitHub

## Lessons Learned

- How S3 public-access controls reduce exposure risk
- How encryption and versioning support data protection
- How IAM policies limit permissions to specific resources
- How temporary credentials can be used to assume an IAM role
- How to verify security controls through positive and negative permission tests

## Future Improvements

- Add sanitized screenshots of security settings and test results
- Document the IAM policy as a standalone JSON file
- Review and tighten the role trust policy
- Explore additional cloud security monitoring and logging controls

## Disclaimer

This project uses a test bucket and test objects for educational purposes. No production data or credentials should be stored in this repository.
