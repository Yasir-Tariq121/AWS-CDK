from aws_cdk import core
from aws_cdk import aws_ec2 as ec2

class VpcCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, vpc_cidr,max_azs,nat_gateways,cidr_mask,ingress_rule_sg,tcp_port, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(
        self, "MyVpc",
        cidr=vpc_cidr,
        max_azs=max_azs,
        nat_gateways=nat_gateways,
        subnet_configuration=[
            ec2.SubnetConfiguration(name="public", cidr_mask=cidr_mask, subnet_type=ec2.SubnetType.PUBLIC),
            ec2.SubnetConfiguration(name="private", cidr_mask=cidr_mask, subnet_type=ec2.SubnetType.ISOLATED)
        ]
    )

        self.sg = ec2.SecurityGroup(self, "VPC-SG", vpc=self.vpc , allow_all_outbound=True , security_group_name='VPC-sg' )
        self.sg.add_ingress_rule(ec2.Peer.ipv4(ingress_rule_sg), connection=ec2.Port.tcp(tcp_port), description='ingress')
        tag = core.Tags.of(self).add(key='Owner', value='Yasir-VPC')




        VPC_Output = core.CfnOutput(self, 'VPC_OUTPUT', value=self.vpc.vpc_id , description="VPC ID")
        SG_Output = core.CfnOutput(self, 'SG_ID_OUTPUT', value=self.sg.security_group_id , description="SG ID")

