import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ItemsTable")

def lambda_handler(event, context):
    method = event.get("httpMethod")
    path = event.get("path")
    body = json.loads(event.get("body", "{}"))

    # CREATE (POST /items)
    if method == "POST" and path == "/items":
        item_id = str(uuid.uuid4())
        item = {
            "id": item_id,
            "name": body.get("name"),
            "description": body.get("description")
        }
        table.put_item(Item=item)
        return response(200, {"message": "Item created", "item": item})

    # READ ALL (GET /items)
    if method == "GET" and path == "/items":
        items = table.scan().get("Items", [])
        return response(200, items)

    # READ ONE (GET /items/{id})
    if method == "GET" and path.startswith("/items/"):
        item_id = path.split("/")[-1]
        result = table.get_item(Key={"id": item_id})
        return response(200, result.get("Item", {}))

    # UPDATE (PUT /items/{id})
    if method == "PUT" and path.startswith("/items/"):
        item_id = path.split("/")[-1]
        updated_item = {
            "id": item_id,
            "name": body.get("name"),
            "description": body.get("description")
        }
        table.put_item(Item=updated_item)
        return response(200, {"message": "Item updated", "item": updated_item})

    # DELETE (DELETE /items/{id})
    if method == "DELETE" and path.startswith("/items/"):
        item_id = path.split("/")[-1]
        table.delete_item(Key={"id": item_id})
        return response(200, {"message": "Item deleted", "id": item_id})

    return response(400, {"error": "Bad request"})

def response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
