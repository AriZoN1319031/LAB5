result = ""
while True:
    word = input("Введите слово :")
    if word == "stop" :
        break
        result = result + word + " "
        print(result)