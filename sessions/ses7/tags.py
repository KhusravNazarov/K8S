import boto3
import pprint as pp
# Get the service resource
# sqs = boto3.resource('sqs')

# # Create the queue. This returns an SQS.Queue instance
# queue = sqs.create_queue(QueueName='test', Attributes={'DelaySeconds': '5'})

# # You can now access identifiers and attributes
# print(queue.url)
# print(queue.attributes.get('DelaySeconds'))


# create ec2 cliente
def tag_image(ami_name, tags):
    ec2_client = boto3.client('ec2')
    response_list = ec2_client.describe_images(ExecutableUsers=['self'])
    list_of_imgs = (response_list['Images'])
    for images in list_of_imgs:
        if images['Name'] == ami_name:
            ami_id = (images['ImageId'])
        else:
            print("image not found")
    response_tag = ec2_client.create_tags(
            Resources=[ami_id],
            Tags=tags
        )
tags = [
        {'Key': 'Environment', 'Value': 'Development'},
        {'Key': 'Project', 'Value': 'project10'}
    ]
ami_name = 'dev-packer-image-20241010195112'
tag_image(ami_name, tags)






   
   







