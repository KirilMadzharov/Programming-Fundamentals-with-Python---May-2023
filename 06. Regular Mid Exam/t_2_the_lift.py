people = int(input())
wagons = list(map(int, input().split()))

for i in range(len(wagons)):
    while wagons[i] < 4 and people > 0:
        people -= 1
        wagons[i] += 1

        if people == 0:
            break

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*wagons, end=" ")

elif people == 0 and sum(wagons) < len(wagons) * 4:
    print("The lift has empty spots!")
    print(*wagons, end=" ")

else:
    print(*wagons, end=" ")
