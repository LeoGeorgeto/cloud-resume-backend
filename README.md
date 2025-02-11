# Cloud Resume Backend

## Overview
This repository contains the serverless backend implementation for the **Cloud Resume Challenge**. It provides a visitor counter API using **AWS Lambda**, **API Gateway**, and **DynamoDB**, with automated testing and deployment through **GitHub Actions**.

## Directory Structure

```
cloud-resume-backend/
├── .github/
│   └── workflows/           # GitHub Actions workflows
│       └── backend-deploy.yml
├── src/
│   ├── init.py
│   └── counter.py          # Lambda function implementation
├── tests/
│   └── test_counter.py     # Unit tests
├── requirements.txt        # Python dependencies
└── template.yaml          # SAM template
```

## Features
- **Serverless Architecture**
- **Automated Testing**
- **CI/CD Pipeline**
- **DynamoDB Integration**
- **API Gateway Endpoint**
- **CORS Support**
- **Error Handling**

## Technologies Used
- **Python 3.9**
- **AWS SAM**
- **AWS Lambda**
- **Amazon DynamoDB**
- **Amazon API Gateway**
- **GitHub Actions**
- **pytest**

---

## Local Development

### Prerequisites
- **Python 3.9**
- **AWS SAM CLI**
- **AWS CLI** configured
- **Docker** (for local testing)

### Setup

1. **Clone the repository**:
   ```bash
   git clone [repository-url]
   cd cloud-resume-backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running Tests

```bash
python -m pytest tests/
```

### Local API Testing

```bash
sam local start-api
```

---

## Deployment

The backend is automatically deployed when changes are pushed to the **main** branch.

### Prerequisites
Ensure the following secrets are configured in **GitHub**:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`

### Automated Deployment
The deployment process includes:

1. **Push to main branch**, which triggers:
   - Unit tests
   - SAM build
   - SAM deploy

### Manual Deployment

```bash
# Build
sam build

# Deploy
sam deploy --guided
```

---

## API Specification

### Endpoint

- **Path**: `/count`
- **Method**: `GET`
- **Response Format**: JSON

#### Example Response
```json
{
    "count": 42
}
```

#### Error Response
```json
{
    "error": "Error message"
}
```

---

## Architecture

### Components
- **Lambda Function** (Python)
- **DynamoDB Table**
- **API Gateway**
- **IAM Roles & Policies**
- **CloudWatch Logs**

### Data Flow
1. **Client** requests counter.
2. **API Gateway** triggers the **Lambda** function.
3. **Lambda** updates **DynamoDB**.
4. **Response** is returned to the client.

---

## Testing

### Unit Tests
- Lambda function testing
- DynamoDB mocking
- Error handling coverage

### Integration Tests
- API endpoint testing
- Database operations
- CORS verification

---

## Monitoring

- **CloudWatch Logs**
- **Lambda metrics**
- **API Gateway metrics**
- **DynamoDB metrics**

---

## Security

- **IAM least privilege**
- **API Gateway throttling**
- **DynamoDB encryption**
- **CORS configuration**

---

## Best Practices

- **Infrastructure as Code**
- **Automated testing**
- **Error handling**
- **Logging**
- **CI/CD pipeline**
- **Code documentation**

---

## Performance

- **Lambda optimization**
- **DynamoDB capacity**
- **API Gateway caching**
- **Error handling**

