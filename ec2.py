import boto3, os

class Credentials:
    def create_key_pair(region, key_name):
        ec2_client = boto3.client("ec2", region_name=region)
        key_pair = ec2_client.create_key_pair(KeyName=key_name)
        private_key = key_pair["KeyMaterial"]
        with os.fdopen(os.open("/tmp/"+ key_name+ ".pem", os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
            handle.write(private_key)
        return key_name


class EC2instance:
    def create(region, key, image_id, count, instance_type):
        ec2_client = boto3.client("ec2", region_name=region)
        instances = ec2_client.run_instances(
            ImageId=image_id,
            MinCount=1,
            MaxCount=count,
            InstanceType=instance_type,
            KeyName=key,
        )
