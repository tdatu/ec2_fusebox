import boto3, json, sys


def ec2_list(c,tagname,tagvalue):

	res = c.describe_instances(
		Filters=[
			{
				'Name': 'tag:' + tagname,
				'Values' : [tagvalue]
			}
		]
	)

	return res

def stop_instances(c, instance_ids):
	res = c.stop_instances(
		InstanceIds = instance_ids
	)
	
	return res

def start_instances(c, instance_ids):
	
	res = c.start_instances(
		InstanceIds = instance_ids
	)

	return res

if __name__ == "__main__":

	command = sys.argv[1]
	instance_ids = []
	client = boto3.client('ec2')

	if(command == "sleep"):

		#Get the list of ec2 based on tag
		ec2s = ec2_list(client, "sleep", "true")
		for i in range(len(ec2s["Reservations"])):
			for ec2 in ec2s["Reservations"][i]["Instances"]:
				instance_ids.append(ec2["InstanceId"])

		print("instance_ids: ", instance_ids)
		res = stop_instances(client, instance_ids)
		print(res)

	elif(command == "start"):

		# Get the list of ec2s based on tag
		ec2s = ec2_list(client, "sleep", "true")
		for i in range(len(ec2s["Reservations"])):
			for ec2 in ec2s["Reservations"][i]["Instances"]:
				instance_ids.append(ec2["InstanceId"])

		res = start_instances(client, instance_ids)
		print(res)

	else:
		print("Command is invalid: {}".format(command))
