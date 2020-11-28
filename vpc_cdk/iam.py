from aws_cdk import core
from aws_cdk import aws_iam as iam

class IAMCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str,principal,actions,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.iam_role = iam.Role(
            self,
            "IAM-ROLE",
            assumed_by=iam.ServicePrincipal(principal),
            description="Role for Ec2 Instance",
            inline_policies=[
                    iam.PolicyDocument(
                        assign_sids=True,
                        statements=[
                            iam.PolicyStatement(
                                effect=iam.Effect('ALLOW'),
                                actions=actions,
                                resources=['*'],
                                sid="AllowS3"
                        )
                            ]
                )
            ],
            role_name="EC2-Role",

        )

        ROLE = core.CfnOutput(self, 'IAM_ROLE_NAME', value=self.iam_role.role_name , description="ROLE Name")
