import json
import boto3
import pytest
from botocore.exceptions import ClientError
from src.counter import lambda_handler

def test_lambda_handler_success(mocker):
    """Test successful visitor count increment"""
    # Mock AWS credentials
    mocker.patch.dict('os.environ', {
        'AWS_ACCESS_KEY_ID': 'testing',
        'AWS_SECRET_ACCESS_KEY': 'testing',
        'AWS_SECURITY_TOKEN': 'testing',
        'AWS_SESSION_TOKEN': 'testing'
    })
    
    # Mock DynamoDB response
    mock_response = {
        'Attributes': {
            'visitor_count': 42
        }
    }
    
    # Create a mock table
    mock_table = mocker.Mock()
    mock_table.update_item.return_value = mock_response
    
    # Create a mock dynamodb resource
    mock_dynamodb = mocker.Mock()
    mock_dynamodb.Table.return_value = mock_table
    
    # Patch boto3.resource to return our mock dynamodb
    mocker.patch('boto3.resource', return_value=mock_dynamodb)
    
    # Test event and context
    event = {}
    context = {}
    
    # Call the lambda handler
    response = lambda_handler(event, context)
    
    # Assert the response structure
    assert response['statusCode'] == 200
    assert 'headers' in response
    assert response['headers']['Access-Control-Allow-Origin'] == '*'
    
    # Parse the response body
    body = json.loads(response['body'])
    assert 'count' in body
    assert body['count'] == 42

def test_lambda_handler_error(mocker):
    """Test error handling in visitor counter"""
    # Mock AWS credentials
    mocker.patch.dict('os.environ', {
        'AWS_ACCESS_KEY_ID': 'testing',
        'AWS_SECRET_ACCESS_KEY': 'testing',
        'AWS_SECURITY_TOKEN': 'testing',
        'AWS_SESSION_TOKEN': 'testing'
    })
    
    # Create a mock table that raises an error
    mock_table = mocker.Mock()
    mock_table.update_item.side_effect = ClientError(
        {'Error': {'Message': 'Test error', 'Code': 'TestException'}},
        'update_item'
    )
    
    # Create a mock dynamodb resource
    mock_dynamodb = mocker.Mock()
    mock_dynamodb.Table.return_value = mock_table
    
    # Patch boto3.resource to return our mock dynamodb
    mocker.patch('boto3.resource', return_value=mock_dynamodb)
    
    # Test event and context
    event = {}
    context = {}
    
    # Call the lambda handler
    response = lambda_handler(event, context)
    
    # Assert error response
    assert response['statusCode'] == 500
    body = json.loads(response['body'])
    assert 'error' in body