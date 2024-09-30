# import library.boto3 as boto3
# from django.conf import settings
import requests
from os import environ


def upload_file_to_s3_bucket(customer_id, filename, file):
    resource_id = environ.get('AWS_API_RESOURCE_ID')
    region = environ.get("AWS_REGION")
    api_env = environ.get("AWS_ENVIRONMENT")
    bucket = environ.get("AWS_BUCKET")
    print(resource_id, 'resource_id')
    aws_api_url = 'https://2sdqnvrfi7.execute-api.ap-south-1.amazonaws.com/develop/v1/upload_file'
    params = {"cust_id": customer_id, "filename": filename}
    headers = {"Content-Type": "application/pdf"}
    print(aws_api_url)

    response = requests.post(aws_api_url, file, params=params, headers=headers)
    # print(response.status_code,'status code')
    # print(response.headers,'headers')
    # print(response.content,'body')
    print('response', response)
    return response





# REGION = 'ap-south-1'
# def s3_get_client():
#     return boto3.client(
#         service_name="s3",
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#         region_name=REGION
#     )
# def upload_fileto_s3(file, file_folder_path):
#     bucket_name = 'backend-system'
#     s3 = boto3.resource('s3',
#                         aws_access_key_id='AKIAQ3EGS5H4JBFLJYMW',
#                         aws_secret_access_key='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',
#                         region_name='ap-south-1')
#     for bucket in s3.buckets.all():
#         if bucket.name:
#             client = boto3.client('s3')
#             client.upload_fileobj(file, 'backend-system',
#                                   'alternate_path')
#             url = client.generate_presigned_url(
#                 ClientMethod='get_object',
#                 Params={'Bucket': bucket_name, 'Key': 'StatementOfAccount_6895514661_01062024_215355.pdf'}, ExpiresIn=30)
#             print(url)
