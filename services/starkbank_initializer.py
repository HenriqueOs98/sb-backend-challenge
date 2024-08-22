import boto3
import json
import starkbank
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name="us-east-1"):
    # Create a Secrets Manager client
    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response["SecretString"]
    return json.loads(secret)

def initialize_starkbank():
    secret_name = "starkbank_credentials"
    region_name = "us-east-1"

    # Fetch the secret
    secret = get_secret(secret_name, region_name)

    # Initialize Stark Bank SDK
    starkbank.user = starkbank.Project(
        environment=secret["environment"],
        id=secret["id"],
        private_key=secret["private_key"]
    )

