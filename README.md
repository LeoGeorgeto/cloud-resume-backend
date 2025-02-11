# **Cloud Resume Challenge - Backend**

A serverless backend for the Cloud Resume Challenge, built with **AWS Lambda**, **DynamoDB**, and **API Gateway**, deployed using **AWS SAM** and **GitHub Actions**. This backend efficiently tracks and updates visitor counts while ensuring scalability, security, and automation.

---

## 🚀 **Features**

- **Serverless Architecture**: Utilizes **AWS Lambda** for compute, **DynamoDB** for storage, and **API Gateway** for API management.
- **Automated Deployment**: Uses **GitHub Actions** to test and deploy via **AWS SAM**.
- **Efficient Visitor Counting**: Implements **atomic counter updates** in DynamoDB.
- **CORS Configuration**: Ensures cross-origin requests are handled correctly.
- **Error Handling**: Implements structured error responses for **database failures** and **unexpected issues**.

---

## 📂 **Project Structure**

```
cloud-resume-backend/
│
├── .github/workflows/               # GitHub Actions workflows
│   ├── backend-deploy.yml            # CI/CD pipeline for backend deployment
│
├── src/                              # Source code for Lambda function
│   ├── __init__.py                   # Package initialization
│   ├── counter.py                     # Visitor counter Lambda function
│
├── tests/                            # Unit tests
│   ├── test_counter.py                # Pytest-based tests for Lambda function
│
├── template.yaml                      # AWS SAM template defining backend infrastructure
├── requirements.txt                    # Python dependencies
├── README.md                          # Project documentation
```

---

## 🛠 **Technologies Used**

### **AWS Services**
- **AWS Lambda** – Executes visitor count updates.
- **Amazon DynamoDB** – Stores and retrieves visitor counts.
- **Amazon API Gateway** – Exposes the `/count` API endpoint.
- **AWS SAM** – Infrastructure-as-Code (IaC) for managing backend resources.
- **AWS IAM** – Manages permissions for secure access.

### **Development & Testing**
- **Python 3.9** – Backend language for Lambda function.
- **boto3 & botocore** – AWS SDK for Python.
- **Pytest & Pytest-Mock** – Unit testing framework.
- **GitHub Actions** – CI/CD automation.

---

## 🔧 **Setup and Deployment**

### **Prerequisites**
Ensure you have the following installed:
- **Python 3.9+** – Required for Lambda function.
- **AWS CLI** – For managing AWS resources.
- **AWS SAM CLI** – Required for serverless deployment.
- **Terraform** – If integrating with infrastructure provisioning.
- **Git** – Version control system.

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd cloud-resume-backend
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Run Tests**
```bash
pytest tests/
```

### **4. Configure AWS Credentials**
```bash
aws configure
```

### **5. Build and Deploy using AWS SAM**
```bash
sam build
sam deploy --stack-name cloud-resume-backend --capabilities CAPABILITY_IAM --resolve-s3 --parameter-overrides TableName=visitor-counter
```

### **6. Verify Deployment**
After deployment, retrieve the API Gateway URL:
```bash
echo $(aws cloudformation describe-stacks --stack-name cloud-resume-backend --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" --output text)
```

---

## 📦 **Available AWS Resources**

| Resource        | Description                                       |
|----------------|---------------------------------------------------|
| `AWS::Serverless::Function` | Lambda function for visitor counting. |
| `AWS::DynamoDB::Table`  | Stores visitor count data.                  |
| `AWS::ApiGateway::RestApi` | Exposes `/count` API endpoint.         |
| `AWS::IAM::Role` | Grants Lambda access to DynamoDB.               |

---

## 🚨 **Troubleshooting**

### **Common Issues & Fixes**
| Issue | Solution |
|--------|----------|
| `sam deploy` fails | Ensure AWS credentials are configured (`aws configure`). |
| Lambda function not updating | Run `sam build` before `sam deploy`. |
| API Gateway not responding | Retrieve API URL using `aws cloudformation describe-stacks`. |

---

## 📝 **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🙌 **Acknowledgments**

- Inspired by the **Cloud Resume Challenge** by Forrest Brazeal.
- Built using **AWS Serverless Technologies** for hands-on cloud experience.

---

## 👨‍💻 **Author**

**Leonardo Georgeto**  
[LinkedIn](https://linkedin.com/in/georgetol) | [GitHub](https://github.com/LeoGeorgeto) | [Resume](https://leogeo-cloudresume.com/) | [Portfolio](https://leogeorgeto.com/)
