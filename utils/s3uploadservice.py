import library.boto3 as boto3
from django.conf import settings


REGION = 'ap-south-1'


# def s3_get_client():
#     return boto3.client(
#         service_name="s3",
#         aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#         aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
#         region_name=REGION
#     )

def upload_fileto_s3(file,file_folder_path):
    
    s3 = boto3.resource('s3',
                        aws_access_key_id='AKIAQ3EGS5H4JBFLJYMW',
                        aws_secret_access_key='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',
                        region_name='ap-south-1')
    
    for bucket in s3.buckets.all():
        if bucket.name:
            client = boto3.client('s3')
            client.upload_fileobj(file, 'backend-system', file_folder_path+'/'+'file')
    
    
        
    

