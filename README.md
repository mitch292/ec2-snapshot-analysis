# ec2-snapshot-analysis
Demo project to manage AWS EC2 instance snapshots

## About 
This app uses boto3 to manage EC2 snapshots
Whl file located here - https://s3.amazonaws.com/ec2-snapshot-analysis/ec2_snapshot_analysis-0.1-py3-none-any.whl

## Configuration
The app uses the configuration file created by the AWS CLI and at this time
required a profile, "shotty"
e.g. `aws configure --profile shotty`

## Running
`pipenv run python shotty/shotty.py <command> <subcommand> <--project=PROJECT>`

*command* - instances, volumes, or snapshots
*subcommand* - depends on command
*project* - optional
