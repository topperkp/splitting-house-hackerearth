import random

# Guess the  count

print("Count betwee 1 to 10")

target = random.randint(1,10)
score = 0
while True:
    score +=1
    user_input = int(input())
    
    if user_input == target:
        print("You found it and your score is" + str(score)) 


