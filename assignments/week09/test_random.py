import random

def test_random():
    random_number = random.randint(1, 10)  #สุ่มเลข 1-10 เก็บใน ramdom_number
    print(random_number)

    guess_number = int(input("What is your guess number?: ")) 

    if random_number == guess_number:
        print("Wp")

    elif random_number < guess_number:
        print("Too much")

    else:
        print("Too low")

test_random()
