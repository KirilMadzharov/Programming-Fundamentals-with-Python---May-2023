resource = input()

total_resource = dict()
while resource != "stop":
    quantity = int(input())
    total_resource[resource] = total_resource.get(resource, 0)
    total_resource[resource] += quantity
    resource = input()

for key, value in total_resource.items():
    print(f"{key} -> {value}")

