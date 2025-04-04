import random
correct = 0
mistakes = 0
for i in range(10):
    if mistakes >= 3 :
        break
    number1 = random.randint(1,10)
    number2 = random.randint(1,10)
    print(f" {number1} + {number2} = ", end = "")
    answer= int(input())
    if number1 + number2 == answer:
        print("Ответ правильный")
        correct += 1
    else:
        print("Ответ неправильный")
        mistakes += 1
print(f"Игра окончена. Правильных ответов: {correct} " )
