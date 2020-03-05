# Ec2 Fusebox

![Fusebox](https://bitbucket.org/signetmedia/ec2-fuse-box/raw/85d13078fcf45303162f4880cf32b878dd880c7c/fuse_box.png)

This is an aim to sleep/start ec2 instances in the dev-sandbox account to reduce aws costs.   
Any ec2 that is tagged "sleep":"true" is subjected to stop at Friday 8pm pst - Sunday 6am (pst).   

## Requirements
- IAM with permission to stop/start ec2 instances
- Appropriately tag an ec2 with "sleep":"true"
- AWS SDK (boto3)
- python3

