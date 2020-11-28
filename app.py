#!/usr/bin/env python3

from aws_cdk import core

from vpc_cdk.vpc_cdk_stack import VpcCdkStack
from vpc_cdk.ec2 import EC2CdkStack
from vpc_cdk.iam import IAMCdkStack
import os



class NCLOUDS(core.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        vpc_cidr = self.get_vpc_config("cidr")
        max_azs = self.get_vpc_config("max_azs")
        nat_gateways = self.get_vpc_config("nat_gateways")
        cidr_mask = self.get_vpc_config("cidr_mask")
        ingress_rule_sg = self.get_vpc_config("ingress_rule_sg")
        tcp_port = self.get_vpc_config("tcp_port")

        principal = self.get_iam_config("principal")
        actions = self.get_iam_config("actions")

        instance_type = self.get_ec2_config("instance_type")
        key_name = self.get_ec2_config("key_name")





        res = VpcCdkStack(
            self,
            "vpc-cdk-yasir",
            env={'account': os.environ['CDK_DEFAULT_ACCOUNT'], 'region': os.environ['CDK_DEFAULT_REGION']},
            vpc_cidr=vpc_cidr,
            max_azs=max_azs,
            nat_gateways=nat_gateways,
            cidr_mask=cidr_mask,
            ingress_rule_sg=ingress_rule_sg,
            tcp_port=tcp_port
            )
        

        iam = IAMCdkStack(
            self,
            "iam-cdk-yasir",
            env={'account': os.environ['CDK_DEFAULT_ACCOUNT'], 'region': os.environ['CDK_DEFAULT_REGION']},
            principal=principal,
            actions=actions
            )

        
        EC2CdkStack(
            self,
            "ec2-cdk-yasir",
            vpc = res.vpc,
            sg_id = res.sg,
            iam_role = iam.iam_role,
            env={'account': os.environ['CDK_DEFAULT_ACCOUNT'], 'region': os.environ['CDK_DEFAULT_REGION']},
            instance_type=instance_type,
            key_name=key_name
            )




    def get_vpc_config(self, attribute):
        return self.node.try_get_context('VPC').get(attribute)
    def get_iam_config(self, attribute):
        return self.node.try_get_context('IAM').get(attribute)
    def get_ec2_config(self, attribute):
        return self.node.try_get_context('EC2').get(attribute)

NCLOUDS().synth()
