import boto3
from botocore.exceptions import ClientError, NoCredentialsError

BUCKET_NAME = "cloud-security-lab-at-2026"
REGION = "us-east-2"


def check_public_access(s3, bucket):
    """Check the four S3 Block Public Access settings."""

    try:
        response = s3.get_public_access_block(Bucket=bucket)
        settings = response["PublicAccessBlockConfiguration"]

        required_settings = [
            "BlockPublicAcls",
            "IgnorePublicAcls",
            "BlockPublicPolicy",
            "RestrictPublicBuckets"
        ]

        print("\nS3 PUBLIC ACCESS SECURITY CHECK")
        print("-" * 40)

        for setting in required_settings:
            enabled = settings.get(setting, False)
            status = "PASS" if enabled else "FAIL"
            print(f"{status}: {setting} = {enabled}")

    except ClientError as error:
        print(f"ERROR: Unable to check public access: {error.response['Error']['Code']}")

def check_encryption(s3, bucket):
    """Check whether default S3 bucket encryption is configured."""

    print("\nS3 ENCRYPTION SECURITY CHECK")
    print("-" * 40)

    try:
        response = s3.get_bucket_encryption(Bucket=bucket)
        rules = response["ServerSideEncryptionConfiguration"]["Rules"]

        for rule in rules:
            encryption = rule["ApplyServerSideEncryptionByDefault"]
            algorithm = encryption["SSEAlgorithm"]

            print(f"PASS: Default encryption configured ({algorithm})")

    except ClientError as error:
        code = error.response["Error"]["Code"]

        if code == "ServerSideEncryptionConfigurationNotFoundError":
            print("FAIL: No explicit default encryption configuration found.")
        else:
            print(f"ERROR: Unable to check encryption: {code}")


def check_versioning(s3, bucket):
    """Check whether S3 Versioning is enabled."""

    print("\nS3 VERSIONING SECURITY CHECK")
    print("-" * 40)

    try:
        response = s3.get_bucket_versioning(Bucket=bucket)
        status = response.get("Status", "Disabled")

        if status == "Enabled":
            print("PASS: S3 Versioning is enabled.")
        else:
            print(f"FAIL: S3 Versioning status is {status}.")

    except ClientError as error:
        print(f"ERROR: Unable to check versioning: {error.response['Error']['Code']}")
def main():
    print("AWS S3 SECURITY CHECKER")
    print("=" * 40)
    print(f"Bucket: {BUCKET_NAME}")
    print(f"Region: {REGION}")

    try:
        session = boto3.Session(region_name=REGION)
        s3 = session.client("s3")

        check_public_access(s3, BUCKET_NAME)
        check_encryption(s3, BUCKET_NAME)
        check_versioning(s3, BUCKET_NAME)

    except NoCredentialsError:
        print("ERROR: AWS credentials not configured.")


if __name__ == "__main__":
    main()
