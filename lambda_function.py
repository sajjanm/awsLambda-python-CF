import json
import boto3

def lambda_handler(event,context):
    ecs = boto3.client('ecs')
    domainName = str(event.get('domainName'))
    response = ecs.update_service(
        cluster='NAME_OF_CLUSTER',
        service= "SERVICE_NAME",
        desiredCount=1
    )
    return response