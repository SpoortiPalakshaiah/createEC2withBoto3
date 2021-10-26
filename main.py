import boto3

def main():
    region = input('Enter the region:')
    ec2_client = boto3.client("ec2", region_name=region)
    keys = ec2_client.describe_key_pairs()
    key_pair_name = input('Enter keypair name:')
    if not any (key['KeyName'] == key_pair_name for key in keys['KeyPairs']):
        print("Key doesn't exists")
        print("Creating key pair........")
        key_pair_name = create_key_pair(region, key_pair_name)
    create_ec2(region, key_pair_name)

if __name__ == '__main__':
    main()
