# ☁️ AWS Developer Notes

## 🌍 AWS Regions
- A **Region** is a *data center* located in a specific geographic area.  
- Each region has its **own dashboard**, **services**, and **resource isolation**.  
- Choose regions based on **latency**, **cost**, and **data compliance**.

---

## 🧩 Basic AWS Services

### 🔐 1. IAM (Identity & Access Management)
- Manage **Users**, **Groups**, **Roles**, and **Policies**.  
- Provides **secure and granular access control** across AWS.  
- 🔑 Example: Create a role for EC2 to access S3 securely.

---

### 💻 2. EC2 (Elastic Compute Cloud)
- Launch and manage **virtual servers (instances)**.  
- ⚙️ **Security Groups** → Define inbound/outbound traffic rules.  
- 🌐 **Elastic IPs** → Static public IPs for persistent connections.  
- 🧩 **Key Pairs** → Used for SSH authentication.  
- ⚖️ **Load Balancer** → Distribute traffic across instances.  
- 📈 **Auto Scaling Group (ASG)** → Automatically scale instances up/down.

---

### 📦 3. S3 (Simple Storage Service)
- Scalable **object storage** for files, backups, and media.  
- 🪣 Create **Buckets** (like cloud hard drives).  
- 💰 Pay only for **storage used** and **data transfer**.  

---

### 🐳 4. ECR (Elastic Container Registry)
- Store and manage **Docker images**.  
- Integrates with **ECS** and **EKS**.  
- 💾 Charged based on image storage and data transfer.

---

### 🚀 5. ECS (Elastic Container Service)
- Run and manage **Docker containers** at scale.  
- 🧠 AWS handles **cluster orchestration** and **autoscaling**.  
- Works with **EC2** or **Fargate** (serverless containers).  

---

### ☸️ 6. EKS (Elastic Kubernetes Service)
- Managed **Kubernetes clusters** on AWS.  
- Use **YAML** files for deployments.  
- Simplifies Kubernetes setup, scaling, and upgrades.

---

### 📊 7. CloudWatch
- Centralized **monitoring**, **metrics**, and **logs** for all AWS services.  
- ⏰ Create **alarms** for performance or billing thresholds.  
- 📈 Build **dashboards** for real-time monitoring and alerts.  

---

### 🧾 8. CloudTrail
- Logs all **account activities** (API calls, resource changes, etc.).  
- 🕵️‍♂️ Useful for **auditing** and **security investigations**.  

---

### 🗄️ 9. RDS (Relational Database Service)
- Managed **SQL database** service (MySQL, PostgreSQL, etc.).  
- 🔁 Supports **replication**, **backups**, and **auto-scaling**.  
- 💸 Fully managed but **costly** for large-scale setups.  

---

### 🍃 10. DocumentDB
- Managed **NoSQL database** compatible with **MongoDB API**.  
- Scalable, secure, and easy to maintain.  

---

### ⚡ 11. ElastiCache
- Managed **in-memory caching** using:
  - 🔴 **Redis**
  - 🟢 **Valkey (Memcached replacement)**
- 🚀 Improves performance by caching frequently accessed data.

---

### 📬 12. SQS (Simple Queue Service)
- Reliable **message queuing** service (FIFO or Standard).  
- Enables **asynchronous**, **decoupled communication**.  
- 🎯 Ideal for one-to-one message delivery.

---

### 📣 13. SNS (Simple Notification Service)
- **Pub/Sub messaging** for one-to-many communication.  
- Triggers **Lambda**, **SQS**, or sends **email/SMS** notifications.  

---

### 📧 14. SES (Simple Email Service)
- Scalable **email delivery** service.  
- Supports **SMTP** and **API-based** sending.  

---

## ⚙️ Advanced AWS Services

### 🧱 1. CloudFormation
- **Infrastructure as Code (IaC)** using **YAML** or **JSON**.  
- Automates creation and management of AWS resources.  
- 🔄 AWS-native alternative to **Terraform**.

---

### 🌎 2. CloudFront
- Global **Content Delivery Network (CDN)** for faster content delivery.  
- 📍 Delivers from **edge locations** closest to the user.  
- Ideal for **static websites**, **S3 hosting**, and **media delivery**.  

---

### 🔀 3. API Gateway
- Fully managed **API management** service.  
- Acts like **NGINX** for routing and proxying traffic.  
- Integrates with **Lambda**, **ECS**, and **EC2** backends.  

---

### 🌐 4. Route 53
- **DNS and domain management** service.  
- Supports **routing policies**, **failover**, and **domain registration**.  

---

### ⚡ 5. Lambda (Serverless Functions)
- Run **functions without managing servers**.  
- 🚀 Triggers include:
  - API Gateway  
  - EventBridge (Cron)  
  - SQS / SNS  
  - Custom events  
- 💰 Pay only for **execution time** → extremely cost-efficient.

---

### 🧠 6. Bedrock
- Host and access **LLMs (Large Language Models)** via API.  
- Ideal for **AI/ML** and **GenAI** integrations.  

---

### 🤖 7. Bedrock AgentCore
- Provides **infrastructure for building AI Agents**.  
- Includes:
  - 🧮 **Memory**  
  - 🔧 **Tools / Actions**  
  - 🧩 **Context Management**  
- Simplifies development of **autonomous AI systems** on AWS.

---

## 🧠 Quick Summary Table

| 🧭 Category | 🧰 Service | 💡 Purpose |
|--------------|------------|-------------|
| **Compute** | EC2, Lambda, ECS, EKS | Run applications and containers |
| **Storage** | S3, EBS, EFS | Store data and files |
| **Databases** | RDS, DocumentDB, ElastiCache | Manage SQL & NoSQL data |
| **Networking** | Route 53, CloudFront, VPC | Manage DNS & content delivery |
| **Security** | IAM, CloudTrail, KMS | Access control & auditing |
| **Messaging** | SQS, SNS, SES | Event-driven communication |
| **Monitoring** | CloudWatch | Logs, metrics, and alerts |
| **AI/ML** | Bedrock, AgentCore | LLM hosting & AI infrastructure |

---

### 🧾 Tip
If you're learning AWS as a developer:
- Start with **IAM**, **EC2**, and **S3**.  
- Then move to **Lambda**, **API Gateway**, and **RDS**.  
- Finally explore **ECS/EKS**, **CloudFormation**, and **Bedrock** for advanced use cases.

---
