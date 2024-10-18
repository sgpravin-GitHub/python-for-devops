import boto3
client = boto3.client('s3')

# this code will create a bucket with name - 'gaddi.s3.31cross'
# response = client.create_bucket(
#     Bucket='gaddi.s3.31cross',
# )

#This code will give the information about ACL
response = client.get_bucket_acl(
    Bucket='gaddi.s3.31cross',
)

print(response)

#this code will print the details
print("RequestId is : ", response["ResponseMetadata"]["RequestId"])
print("HostId is : ", response["ResponseMetadata"]["HostId"])

#############
