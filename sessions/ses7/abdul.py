import os, sys
import boto3, json
from botocore.exceptions import NoCredentialsError

# AWS region
region_name = 'us-east-1'
env = sys.argv[1]

session = boto3.Session(profile_name=f"sts-{env}")
# Dictionary of key/value pairs (environmental variable key/secret ID)
secrets_dict = {
    f"sm-us-east-1-cloudinary-{dev}-project9": "NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY",
    f"sm-us-east-1-stripe-api-key-{dev}-project9": "CLERK_SECRET_KEY",
    f"sm-us-east-1-resend-api-key-{dev}-project9": "NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME",
    f"sm-us-east-1-frontend-store-url-{dev}-project9": "NEXT_PUBLIC_CLOUDINARY_UPLOAD_PRESENT",
    f"sm-us-east-1-cloudinary-present-{dev}-project9": "FRONTEND_STORE_URL",
    f"sm-us-east-1-clerk-secret-{dev}-project9": "STRIPE_API_KEY",
    f"sm-us-east-1-clerk-key-{dev}-project9": "RESEND_API_KEY"
}

def db_setup():
    try:
        os.environ
        db_cred_id = f"sm-us-east-1-rds-{env}-project9"
        client = session.client('secretsmanager', region_name=region_name)

        # Retrieve secret value from Secrets Manager
        response = client.get_secret_value(SecretId=db_cred_id)
        secret_data = json.loads(response['SecretString'])
        envFile = open('.env', 'w')
        dbCred = f'DATABASE_URL="postgresql://{secret_data["username"]}:{secret_data["password"]}@{secret_data["endpoint"]}/{secret_data["database"]}"\n'
        envFile.write(dbCred)
        envFile.close()

    except NoCredentialsError:
        print(f"Credentials not available -- {db_cred_id}")
        return None
        
def retrieve_secret(secret_id):
    try:
        # Create a Secrets Manager client
        client = client = session.client('secretsmanager', region_name=region_name)

        # Retrieve secret value from Secrets Manager
        response = client.get_secret_value(SecretId=secret_id)
        secret_data = response['SecretString']

        # Parse the JSON string within the secret value
        secret_values = json.loads(secret_data)
        return secret_values

    except NoCredentialsError:
        print(f"Credentials not available -- {secret_id}")
        return None

def main():
    envFile = open('.env', 'a')
    for secret_id, env_var_key in secrets_dict.items():
        # print(env_var_key, secret_id)
        # Retrieve secret values for each secret ID
        secret_values = retrieve_secret(secret_id)
        # print(secret_values)

        if secret_values:
            # Set environmental variables
            for key, value in secret_values.items():
                # os.environ[key] = str(value)
                envFile.write(f'{key}="{str(value)}"\n')
                # print(f"Set environmental variable {key} with value {value}")

if __name__ == "__main__":
    db_setup()
    main()