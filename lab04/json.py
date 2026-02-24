import json

data = json.loads(input())
print(data["name"])

data = json.loads(input())
print(sum(data.values()))

data = json.loads(input())
data["status"] = "ok"
print(json.dumps(data, separators=(",", ":")))

data = json.loads(input())
print(data["user"]["address"]["city"])

data = json.loads(input())
max_age = max(person["age"] for person in data)
print(max_age)