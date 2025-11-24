# 🧩 Serverless CRUD API with AWS Lambda, API Gateway & DynamoDB

A fully serverless **CRUD API** built using:

Technology Used :
- **AWS Lambda (Python 3.12)**
- **Amazon API Gateway**
- **Amazon DynamoDB**
- **IAM Role-based Access**
- **Postman for API testing**
- **Cloudwatch**

This project demonstrates a clean and production-ready serverless architecture suitable for beginners and cloud practitioners.

---

## 🚀 Features

| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/items` | Create a new item |
| **GET** | `/items` | Get all items |
| **GET** | `/items/{id}` | Get a specific item |
| **PUT** | `/items/{id}` | Update an item |
| **DELETE** | `/items/{id}` | Delete an item |

---

## 🏗 Architecture Overview

This serverless system works as follows:

1. **API Gateway** receives the HTTP request  
2. **Lambda** processes the request (Python)  
3. **DynamoDB** stores/retrieves/updates/deletes items  
4. Lambda returns JSON response back to API Gateway  
5. API Gateway returns data to client (Postman / browser)  

🛠 Setup Instructions
1. Create DynamoDB Table
Table Name: ItemsTable
Primary Key: id (String)

2. Create Lambda Function

Runtime: Python 3.12

Add environment permission for DynamoDB

3. Attach IAM Role Permissions

Allow Lambda to read/write DynamoDB:
dynamodb:PutItem
dynamodb:DeleteItem
dynamodb:GetItem
dynamodb:Scan

4. Create API Gateway REST API

Routes:
POST    /items
GET     /items
GET     /items/{id}
PUT     /items/{id}
DELETE  /items/{id}

Integrate each route → Lambda function.

🧪 API Testing (Postman)
Create Item (POST)
POST https://<your-api-endpoint>/prod/items

Body (raw → JSON):
{
  "name": "Keyboard",
  "description": "Mechanical keyboard"
}

Get All Items
GET https://<your-api-endpoint>/prod/items

Get One Item
GET https://<your-api-endpoint>/prod/items/{id}

Replace {id} with actual ID.

Update Item
PUT https://<your-api-endpoint>/prod/items/{id}

Delete Item
DELETE https://<your-api-endpoint>/prod/items/{id}


