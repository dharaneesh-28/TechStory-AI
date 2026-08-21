TechStory AI - README.md (DETAILED VERSION)













\# 🤖 TechStory AI - Autonomous Technology Story Generator



\[!\[AWS](https://img.shields.io/badge/AWS-Serverless-orange)](https://aws.amazon.com/)

\[!\[Lambda](https://img.shields.io/badge/Lambda-Python%203.12-blue)](https://aws.amazon.com/lambda/)

\[!\[Status](https://img.shields.io/badge/Agent-Active-brightgreen)](http://techstory-ai-dharaneesh.s3-website-us-east-1.amazonaws.com)



> An always-on creative agent that autonomously generates unique technology stories every day using AWS Lambda + EventBridge + DynamoDB + S3.



\*\*🏆 Built for:\*\* \[AWS Weekend Creative Agent Challenge (August 2026)](https://community.aws/builderscenter)



\*\*🌐 Live Website:\*\* \[http://techstory-ai-dharaneesh.s3-website-us-east-1.amazonaws.com](http://techstory-ai-dharaneesh.s3-website-us-east-1.amazonaws.com)



\*\*📝 Builder Center Article:\*\* \[https://builder.aws.com/content/3IDiDXNiK7JXM1e3i0QM0DNUUsA](https://builder.aws.com/content/3IDiDXNiK7JXM1e3i0QM0DNUUsA/weekend-creative-agent-challenge-techstory-ai-autonomous-technology-story-generator)



\---



\## 📖 About



TechStory AI is a fully autonomous, serverless creative agent that generates unique technology-themed stories every single day without any manual intervention. Every morning at \*\*8:00 AM IST\*\*, the agent wakes up, creates a brand-new story combining characters, technologies, problems, solutions, and locations, then stores it and displays it on a live website.



\*\*Zero human interaction required after deployment.\*\*



\---



\## 🏗️ Architecture

┌─────────────────────────────────────────────────────────────┐ │ TechStory AI Architecture │ ├─────────────────────────────────────────────────────────────┤ │ │ │ ┌──────────────┐ ┌──────────────┐ ┌───────────┐ │ │ │ EventBridge │────▶│ Lambda │────▶│ DynamoDB │ │ │ │ (Scheduler) │ │ (Generator) │ │ (Storage) │ │ │ └──────────────┘ └──────────────┘ └───────────┘ │ │ │ │ │ │ │ Daily 8:00 AM IST │ │ │ │ ▼ │ │ │ ┌───────────┐ │ │ └──────────────────────────────────▶│ S3 │ │ │ │ (Website) │ │ │ └───────────┘ │ │ │ └─────────────────────────────────────────────────────────────┘





\---



\## ⚙️ AWS Services Used



| Service | Purpose | Tier |

|---------|---------|------|

| \*\*AWS Lambda\*\* | Python 3.12 story generation engine (256MB, 30s timeout) | Free Tier |

| \*\*Amazon EventBridge Scheduler\*\* | Daily 8:00 AM IST automatic trigger (cron-based) | Free Tier |

| \*\*Amazon DynamoDB\*\* | Story storage with composite key (date + category) | Free Tier |

| \*\*Amazon S3\*\* | Static website hosting with public access | Free Tier |



\*\*Total Monthly Cost: $0.00\*\* (runs entirely on AWS Free Tier)



\---



\## 🧠 How It Works



\### Story Generation Engine



The Lambda function uses a \*\*combinatorial creativity engine\*\* with:



| Element | Count | Examples |

|---------|-------|----------|

| Characters | 10 | Engineers, Scientists, Farmers, Musicians, Hackers |

| Technologies | 10 | AI+IoT, Robotics+Drones, Quantum+Weather, 5G+Emergency |

| Problems | 10 | Hidden dangers, Mysterious signals, Chain reactions |

| Solutions | 10 | Global adoption, Award-winning, Open-source success |

| Locations | 10 | Cities, Villages, Labs, Hospitals, Arctic stations |



\*\*Total Possible Combinations: 10 × 10 × 10 × 10 × 10 = 100,000+ unique stories\*\*



\### Daily Flow



1\. \*\*8:00 AM IST\*\* — EventBridge triggers Lambda function

2\. \*\*Lambda\*\* uses current date as random seed (ensures reproducibility)

3\. \*\*Randomly selects\*\* one element from each category

4\. \*\*Generates\*\* title + full story narrative

5\. \*\*Saves\*\* to DynamoDB with metadata (date, category, character, technology, timestamp)

6\. \*\*Website\*\* on S3 displays the latest generated story



\---



\## 📖 Sample Output



\### Today's Story (August 21, 2026)



\*\*🏷️ Category:\*\* 5G + Emergency



\*\*📌 Title:\*\* \*When Karthik Discovered the Power of 5G + Emergency\*



> A village farmer named Karthik was working in a small fishing town facing rising sea levels when something extraordinary happened. Using 5G + Emergency - Ultra-fast networks enabling instant emergency response - they accidentally triggered a chain reaction that changed everything. What followed was nothing short of remarkable. Against all odds, a breakthrough emerged. The pilot program was so successful that it expanded to 50 cities within months.

>

> \*\*Technology:\*\* 5G + Emergency

> \*\*Real-world application:\*\* Ultra-fast networks enabling instant emergency response

> \*\*Key insight:\*\* Innovation happens when curiosity meets persistence.



\---



\## 📁 Project Structure



TechStory-AI/ │ ├── lambda\_function.py # AWS Lambda function - Story generation engine │ # Contains: Characters, Technologies, Problems, │ # Solutions, Locations, Title templates │ ├── index.html # S3 static website - Modern dark theme UI │ # Displays: Story title, content, tech info, │ # agent status, date │ └── README.md # Project documentation





\---



\## 🚀 Deployment Guide



\### Prerequisites



\- AWS Account (Free Tier eligible)

\- AWS CLI configured with credentials

\- PowerShell or Terminal



\### Step-by-Step Deployment



```bash

\# 1. Create IAM Role for Lambda

aws iam create-role --role-name TechStoryLambdaRole \\

&#x20; --assume-role-policy-document file://trust-policy.json



aws iam attach-role-policy --role-name TechStoryLambdaRole \\

&#x20; --policy-arn arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess



aws iam attach-role-policy --role-name TechStoryLambdaRole \\

&#x20; --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole



\# 2. Create DynamoDB Table

aws dynamodb create-table --table-name TechStoryCreations \\

&#x20; --attribute-definitions \\

&#x20;   AttributeName=date,AttributeType=S \\

&#x20;   AttributeName=category,AttributeType=S \\

&#x20; --key-schema \\

&#x20;   AttributeName=date,KeyType=HASH \\

&#x20;   AttributeName=category,KeyType=RANGE \\

&#x20; --billing-mode PAY\_PER\_REQUEST



\# 3. Deploy Lambda Function

zip lambda\_function.zip lambda\_function.py



aws lambda create-function --function-name TechStoryAgent \\

&#x20; --runtime python3.12 \\

&#x20; --role arn:aws:iam::ACCOUNT\_ID:role/TechStoryLambdaRole \\

&#x20; --handler lambda\_function.lambda\_handler \\

&#x20; --zip-file fileb://lambda\_function.zip \\

&#x20; --timeout 30 --memory-size 256



\# 4. Create EventBridge Schedule (Daily 8:00 AM IST)

aws scheduler create-schedule --name TechStoryTrigger \\

&#x20; --schedule-expression "cron(30 2 \* \* ? \*)" \\

&#x20; --schedule-expression-timezone "Asia/Kolkata" \\

&#x20; --flexible-time-window '{"Mode":"OFF"}' \\

&#x20; --target '{"Arn":"arn:aws:lambda:us-east-1:ACCOUNT\_ID:function:TechStoryAgent","RoleArn":"arn:aws:iam::ACCOUNT\_ID:role/TechStorySchedulerRole"}'



\# 5. Create S3 Website

aws s3 mb s3://techstory-ai-dharaneesh

aws s3 website s3://techstory-ai-dharaneesh --index-document index.html

aws s3 cp index.html s3://techstory-ai-dharaneesh/ --content-type "text/html"

🔑 Key Features

Table







Feature





Description





🤖 Fully Autonomous	No manual intervention after deployment

📚 100,000+ Unique Stories	Combinatorial creativity engine

☁️ Serverless	No servers to manage or maintain

💰 Cost-Free	Runs entirely on AWS Free Tier

📅 Daily Themes	Different technology focus each day

🔄 Reproducible	Date-seeded randomization ensures consistency

🌐 Live Website	Beautiful dark-themed responsive UI

⏰ Scheduled	Runs precisely at 8:00 AM IST daily

View more

💡 What I Learned

Serverless Event-Driven Architecture — Designing systems that respond to events rather than running continuously

AWS CLI Mastery — Building entire infrastructure programmatically through command line

IAM Least Privilege — Creating minimal-permission roles for security-first design

Combinatorial Creativity — Designing algorithms that produce coherent narratives from randomized components

Cost Optimization — Architecting within Free Tier constraints

Autonomous Systems — Building zero-maintenance, self-running applications

🛠️ Tech Stack

Runtime: Python 3.12

Cloud: AWS (Lambda, EventBridge, DynamoDB, S3)

Frontend: HTML5, CSS3 (Glassmorphism UI)

Deployment: AWS CLI

Scheduling: Cron-based (EventBridge Scheduler)

Database: NoSQL (DynamoDB - Pay per request)

👤 Author

Dharaneesh K



GitHub: @dharaneesh-28

Builder Center: TechStory AI Article

