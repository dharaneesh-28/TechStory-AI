# 🤖 TechStory AI — Autonomous Technology Story Generator

> **An always-on serverless creative agent that automatically generates a fresh technology-themed story every day.**
> 
---

## 📖 About

**TechStory AI** is a fully autonomous, serverless creative agent that generates a unique technology-themed story every day without manual intervention.

The system automatically wakes up at **8:00 AM IST**, generates a new story by combining different characters, technologies, problems, solutions, and locations, stores the result in **Amazon DynamoDB**, and makes the latest story available through a website hosted on **Amazon S3**.

### 🎯 Core Idea

> **"A technology story that never sleeps."**

The project demonstrates how AWS serverless services can be combined to build an **event-driven autonomous creative system** with minimal infrastructure and maintenance.

---

## 🏗️ Architecture

```text
                         ┌──────────────────────────┐
                         │ Amazon EventBridge       │
                         │ Scheduler                │
                         │                          │
                         │ Daily 8:00 AM IST        │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │ AWS Lambda               │
                         │                          │
                         │ Python 3.12              │
                         │ Story Generation Engine  │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │ Amazon DynamoDB          │
                         │                          │
                         │ Story Storage            │
                         │ Date + Category          │
                         └────────────┬─────────────┘
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │ Amazon S3                │
                         │                          │
                         │ Static Website           │
                         │ Latest Story             │
                         └──────────────────────────┘
```

### Architecture Flow

```text
EventBridge
     │
     ▼
Lambda
     │
     ├── Generate Story
     │
     ▼
DynamoDB
     │
     ▼
S3 Website
```

---

## ☁️ AWS Services

| AWS Service                      | Purpose                                       |
| -------------------------------- | --------------------------------------------- |
| **AWS Lambda**                   | Runs the autonomous story-generation logic    |
| **Amazon EventBridge Scheduler** | Automatically triggers Lambda every day       |
| **Amazon DynamoDB**              | Stores generated stories and metadata         |
| **Amazon S3**                    | Hosts the static website                      |
| **AWS IAM**                      | Controls permissions between AWS services     |
| **Amazon CloudWatch**            | Provides Lambda execution logs and monitoring |

### Lambda Configuration

* **Runtime:** Python 3.12
* **Memory:** 256 MB
* **Timeout:** 30 seconds
* **Execution:** Event-driven

### DynamoDB Configuration

* **Table:** `TechStoryCreations`
* **Partition Key:** `date`
* **Sort Key:** `category`
* **Billing Mode:** `PAY_PER_REQUEST`

### Scheduling

The agent runs automatically every day at:

```text
08:00 AM IST
Asia/Kolkata
```

---

## ⚙️ How It Works

### 1. ⏰ Automatic Trigger

Amazon EventBridge Scheduler triggers the Lambda function every day at **8:00 AM IST**.

### 2. 🤖 Lambda Execution

AWS Lambda starts the Python-based story generation engine.

### 3. 🎲 Story Element Selection

The system selects elements from predefined categories:

| Element      | Examples                                             |
| ------------ | ---------------------------------------------------- |
| Characters   | Engineers, Scientists, Farmers, Researchers          |
| Technologies | AI, IoT, Robotics, 5G, Quantum Computing             |
| Problems     | System failures, hidden dangers, mysterious signals  |
| Solutions    | Breakthroughs, automation, open-source solutions     |
| Locations    | Cities, Villages, Labs, Hospitals, Research Stations |

### 4. 📝 Story Generation

The selected elements are combined to create:

* Story title
* Technology description
* Narrative
* Application
* Key insight

### 5. 💾 Data Storage

The generated story and metadata are stored in Amazon DynamoDB.

### 6. 🌐 Website Display

The latest story is displayed through the static website hosted on Amazon S3.

---

## ✨ Key Features

| Feature                           | Description                                         |
| --------------------------------- | --------------------------------------------------- |
| 🤖 **Fully Autonomous**           | No manual intervention after deployment             |
| 📅 **Daily Generation**           | Automatically creates a new story every day         |
| 🎲 **Combinatorial Generation**   | Combines multiple story dimensions                  |
| 📚 **100,000+ Combination Space** | 10 × 10 × 10 × 10 × 10 possible combinations        |
| ☁️ **Serverless**                 | No traditional server infrastructure required       |
| 💾 **Persistent Storage**         | Stories are stored in DynamoDB                      |
| 🌐 **Live Website**               | Latest generated story is publicly accessible       |
| 🔄 **Reproducible**               | Date-based seed can provide deterministic selection |
| ⚡ **Event-Driven**                | EventBridge automatically starts the workflow       |
| 🔐 **IAM Controlled**             | AWS IAM manages service permissions                 |
| 📈 **Scalable Architecture**      | Managed AWS services can scale with demand          |

> **Note:** The 100,000+ figure represents the theoretical combination space, not a guarantee of 100,000 semantically unique stories.

---

## 📁 Project Structure

```text
TechStory-AI/
│
├── lambda_function.py
│   └── AWS Lambda story generation engine
│
├── index.html
│   └── Static website frontend
│
├── trust-policy.json
│   └── IAM trust policy for Lambda
│
└── README.md
    └── Project documentation
```

### Main Files

**`lambda_function.py`**

Contains:

* Story generation logic
* Character definitions
* Technology definitions
* Problem definitions
* Solution definitions
* Location definitions
* Title generation
* DynamoDB storage logic

**`index.html`**

Contains:

* Website interface
* Latest story display
* Technology information
* Agent status
* Date information
* Responsive UI

---

## 🚀 Deployment

### Prerequisites

Install and configure:

* AWS Account
* AWS CLI
* Python 3.12
* PowerShell / Terminal
* ZIP utility

Verify AWS CLI:

```bash
aws --version
```

Verify AWS authentication:

```bash
aws sts get-caller-identity
```

### Step 1 — Create IAM Role

Create `trust-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Create the Lambda role:

```bash
aws iam create-role \
  --role-name TechStoryLambdaRole \
  --assume-role-policy-document file://trust-policy.json
```

Attach the required permissions:

```bash
aws iam attach-role-policy \
  --role-name TechStoryLambdaRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess
```

```bash
aws iam attach-role-policy \
  --role-name TechStoryLambdaRole \
  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

> For production deployment, replace broad managed policies with least-privilege IAM policies.

### Step 2 — Create DynamoDB Table

```bash
aws dynamodb create-table \
  --table-name TechStoryCreations \
  --attribute-definitions \
    AttributeName=date,AttributeType=S \
    AttributeName=category,AttributeType=S \
  --key-schema \
    AttributeName=date,KeyType=HASH \
    AttributeName=category,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST
```

### Step 3 — Package Lambda

```bash
zip lambda_function.zip lambda_function.py
```

### Step 4 — Deploy Lambda

Replace `ACCOUNT_ID` with your AWS account ID:

```bash
aws lambda create-function \
  --function-name TechStoryAgent \
  --runtime python3.12 \
  --role arn:aws:iam::ACCOUNT_ID:role/TechStoryLambdaRole \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://lambda_function.zip \
  --timeout 30 \
  --memory-size 256
```

### Step 5 — Configure EventBridge

The target schedule is:

```text
Every day
08:00 AM
Asia/Kolkata
```

When using the `Asia/Kolkata` timezone, configure the Scheduler with the local-time expression:

```text
cron(0 8 * * ? *)
```

The EventBridge Scheduler execution role must have permission to invoke the Lambda function.

### Step 6 — Deploy S3 Website

Create the bucket:

```bash
aws s3 mb s3://techstory-ai-dharaneesh
```

Upload the website:

```bash
aws s3 cp index.html \
  s3://techstory-ai-dharaneesh/ \
  --content-type "text/html"
```

Configure static website hosting:

```bash
aws s3 website s3://techstory-ai-dharaneesh \
  --index-document index.html
```

> For production use, **Amazon CloudFront + S3** is recommended instead of direct public S3 website hosting.

---

## 🔮 Future Enhancements

### 🧠 AI-Powered Story Generation

Integrate **Amazon Bedrock** to generate richer, more natural, and context-aware technology stories.

### 🖼️ AI Story Illustrations

Automatically generate a visual illustration for every daily story.

### 🔊 Voice Narration

Convert generated stories into audio using text-to-speech technology.

### 🌍 Multi-Language Support

Generate stories in:

* English
* Tamil
* Hindi
* Telugu
* Malayalam
* Other regional languages

### 📱 Mobile Experience

Develop a Progressive Web App for easier access from mobile devices.

### 📊 Analytics Dashboard

Track:

* Number of stories generated
* Popular technologies
* Story categories
* Daily generation history
* User engagement

### 🔔 Notifications

Send daily stories through:

* Email

### 🔎 Story Archive

Allow users to search and explore previously generated stories.

---


## 🔗 Demo / Project Links

🌐 **Live Website:**
[TechStory AI](http://techstory-ai-dharaneesh.s3-website-us-east-1.amazonaws.com)

📝 **AWS Builder Center Article:**
[Read the Project Article](https://builder.aws.com/content/3IDiDXNiK7JXM1e3i0QM0DNUUsA/weekend-creative-agent-challenge-techstory-ai-autonomous-technology-story-generator)

💻 **GitHub:**
[github.com/dharaneesh-28](https://github.com/dharaneesh-28)


---

## 🚀 TechStory AI

**Imagine. Generate. Automate. Every Day.**

Built with  Dharaneesh K using AWS Serverless Technologies.
