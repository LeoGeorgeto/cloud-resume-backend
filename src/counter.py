import json
import os
import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    """
    Lambda function to handle visitor counter
    """
    try:
        # Initialize DynamoDB client
        dynamodb = boto3.resource('dynamodb')
        table_name = os.environ['DYNAMODB_TABLE']  # Get table name from environment variable
        table = dynamodb.Table(table_name)
        
        print(f"Using DynamoDB table: {table_name}")  # Add logging
        
        # Update visitor count
        response = table.update_item(
            Key={'id': 'visitor_count'},
            UpdateExpression='ADD #count :inc',
            ExpressionAttributeNames={'#count': 'count'},  # Use count as attribute name
            ExpressionAttributeValues={':inc': 1},
            ReturnValues='UPDATED_NEW'
        )
        
        # Get the updated count
        count = response['Attributes']['count']
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'count': count})
        }
    
    except ClientError as e:
        print(f"DynamoDB Error: {str(e)}")  # Enhanced error logging
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': f"Database error: {str(e)}"})
        }
    except Exception as e:
        print(f"Unexpected error: {str(e)}")  # Enhanced error logging
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps({'error': f"Internal server error: {str(e)}"})
        }