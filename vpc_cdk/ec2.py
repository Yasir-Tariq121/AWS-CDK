from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from vpc_cdk_stack import VpcCdkStack
from iam import IAMCdkStack
from aws_cdk import aws_iam as iam


class EC2CdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, vpc, sg_id, iam_role, instance_type, key_name,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = vpc
        ec2_instance = ec2.Instance(
        self, "EC2",
        instance_type=ec2.InstanceType(instance_type),
        vpc=vpc,
        machine_image= ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
            ),
        instance_name= "Yasir-test-EC2",
        security_group= sg_id,
        key_name=key_name,
        role=iam_role,
        vpc_subnets= ec2.SubnetSelection(subnets=vpc.public_subnets)
    )

