import boto3

# Set up AWS credentials
AWS_ACCESS_KEY = "YOUR_ACCESS_KEY"
AWS_SECRET_KEY = "YOUR_SECRET_KEY"
SOURCE_BUCKET = "source-bucket"
DEST_BUCKET = "destination-bucket"
SOURCE_REGION = "us-east-1"
DEST_REGION = "us-west-2"

# S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=SOURCE_REGION
)

# List objects in the source bucket
response = s3.list_objects_v2(Bucket=SOURCE_BUCKET)

if "Contents" in response:
    for obj in response["Contents"]:
        file_key = obj["Key"]
        
        # Check if file is a .jpg
        if file_key.lower().endswith(".jpg"):
            copy_source = {"Bucket": SOURCE_BUCKET, "Key": file_key}
            
            # Copy to destination bucket
            s3.copy_object(
                CopySource=copy_source,
                Bucket=DEST_BUCKET,
                Key=file_key
            )
            print(f"Copied: {file_key}")

print("Transfer complete.")