import boto3, click
from ec2 import EC2instance,Credentials

@click.command()
@click.option('--region', default='us-east-2', prompt="Enter region", help='Region')
@click.option('--key_pair_name',prompt='Enter key pair name', help='Key Pair Name')
@click.option('--image_id', default='ami-074cce78125f09d61',prompt='Enter AMI ID', help='AMI ID')
@click.option('--count', default=1, prompt='Enter instance count', help='Number of instances to be created')
@click.option('--instance_type', default='t2.micro', prompt='Enter instance type', help='Instance type')

def main(region, key_pair_name, image_id, count, instance_type):
    ec2_client = boto3.client("ec2", region_name=region)
    keys = ec2_client.describe_key_pairs()
    if not any (key['KeyName'] == key_pair_name for key in keys['KeyPairs']):
        print("Key doesn't exists")
        print("Creating key pair........")
        key_pair_name = Credentials.create_key_pair(region, key_pair_name)
    EC2instance.create(region, key_pair_name, image_id, count, instance_type)

if __name__ == '__main__':
    main()
