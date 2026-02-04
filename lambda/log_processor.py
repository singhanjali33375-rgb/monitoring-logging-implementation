import json

def lambda_handler(event, context):
    for record in event['records']:
        log_data = record['data']
        print("Received log:", log_data)

    return {
        'statusCode': 200,
        'body': json.dumps('Log processed successfully')
    }
