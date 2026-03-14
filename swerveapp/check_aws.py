import boto3

# This uses the same credentials you just set up for Terraform
s3 = boto3.resource('s3')

print("--- My S3 Buckets ---")
for bucket in s3.buckets.all():
    print(f"Found bucket: {bucket.name}")