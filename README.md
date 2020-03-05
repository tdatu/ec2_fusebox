# Ec2 Fusebox

![Fusebox]()

This is an aim to sleep/start ec2 instances in the dev-sandbox account to reduce aws costs. <br/> 
Any ec2 that is tagged "sleep":"true" is subjected to stop at Friday 8pm pst - Sunday 6am (pst). <br />

## Requirements
- IAM with permission to stop/start ec2 instances
- Appropriately tag an ec2 with "sleep":"true"
- AWS SDK (boto3)
- python3

