"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import aws

config = pulumi.Config()
data = config.require_object("data")
machinename = data.get("machine_name")
instancetype = data.get("instance_type")
sg = data.get("vpc_security_group_ids")
subnet = data.get("subnet_id")
ami = data.get("ami")

print (machinename + " : " + instancetype + " : " + sg + " : " + subnet + " : " + ami)

"""
server = aws.ec2.Instance("at-mark4-poc-ec2",
                        instance_type="t1.micro",
                        subnet_id="subnet-0dbe15c3953053f18",
                        tags= { 
                            "Name": "at-mark4-poc-ec2" 
                        },
                        vpc_security_group_ids=["sg-0480d2d292d116594"],
                        #key_name=keypair.id,
                        ami="ami-0cff7528ff583bf9a")

pulumi.export('privateIP', server.private_ip)
pulumi.export('privateDNS', server.private_dns)
"""