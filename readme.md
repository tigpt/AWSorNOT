# ☁️ AWS or NOT

![Logo](/logo/logo.jpg)

**AWS or NOT** is a simple, elegant web application that lets you verify if a given URL is hosted on Amazon Web Services. Enter a URL, click a button, and instantly discover whether the underlying infrastructure belongs to AWS — all with a clean, modern interface.

---

## 📚 Index

- [🔍 How It Works](#🔍-how-it-works)
- [📦 Tech Stack](#📦-tech-stack)
- [🧩 Lambda Function Explained](#🧩-lambda-function-explained)
- [🖥 Demo](#🖥-demo)
- [📸 Example Response](#📸-example-response)
- [🤝 Community Initiative](#🤝-community-initiative)

![Screenshot](/doc/screenshot.jpg)
![stepfunction](/doc/stepfunction.png)
---

## 🔍 How It Works

1. User enters a URL in the input field.
2. A request is sent to the backend API (`https://api.awsornot.com/scan`).
3. The API returns a JSON payload with hosting information.
4. The result is beautifully displayed with dynamic color, icons, and feedback.

---

## 📦 Tech Stack

### 🚀 Frontend (Static Website)
- **Amazon S3** – hosts the static HTML/CSS/JS/Images assets
- **Amazon CloudFront** – delivers the content globally with low latency
- **Amazon Route 53** – provides DNS routing for the custom domain

### 🧠 Backend (API + Processing)
- **Amazon API Gateway** – handles the public API endpoint (`/scan`)
- **AWS Step Functions** – orchestrates the logic for checking hosting information
- **AWS Lambda** – serverless functions that perform detection logic
- **Amazon DynamoDB** – stores scan results and metadata
- **Amazon Route 53** – also used for internal routing to backend components

---

## 🧩 Lambda Function Explained

The core of the logic lives inside an AWS Lambda function. Here's a simple breakdown of what it does:

1. Receives the URL input from API Gateway via the Step Function.
2. Extracts the domain and resolves the hosting provider by querying DNS records and metadata.
3. Determines whether the hosting provider is part of AWS infrastructure, comparing the IP with AWS Public List of IPs. 
4. Returns a structured response including the domain, original URL, a descriptive message, and a boolean flag (`aws_hosted`).

The Lambda is written in Python and is designed to be lightweight, stateless, and fast.

---

## 🖥 Demo

Try it live: [awsornot.com](https://awsornot.com)

---

## 📸 Example Response

```json
{
  "domain": "amazon.com",
  "message": "Hosted on AWS (AMAZON)",
  "aws_hosted": true,
  "url": "https://amazon.com"
}
```
---

## 🤝 Community Initiative

This project is an initiative of the [AWS User Group Lisbon](https://lisbon.awsug.site/), collaboratively developed by its members. It serves as a hands-on learning and teaching tool to explore and demonstrate the power of AWS serverless services in a real-world application.
