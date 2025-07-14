print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes/no): ").lower()

if playing != "yes":
    print("Okay, maybe next time!")
    quit()
else:
    print("Great! Let's get started!:)")
    
print(" ")

score = 0
# Quiz questions and answers
print("You will be asked 5 questions about computer hardware. Please answer them correctly to win the game.")
print("Let's begin!")
print(" ")
print("--------Question 1--------")
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Central Processing Unit'.")

print(" ")
print("--------Question 2--------")
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":   
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Graphics Processing Unit'.")

print(" ")
print("--------Question 3--------")
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Random Access Memory'.")

print(" ")
print("--------Question 4--------")
answer = input("What does ROM stand for? ").lower()
if answer == "read only memory": 
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is 'Read Only Memory'.")

print(" ")
print("--------Question 5--------")
answer = input("What does SSD stand for? ").lower()
if answer == "solid state drive":
    print("Correct!")
    score += 1  
else:
    print("Incorrect! The correct answer is 'Solid State Drive'.")

print(" ")
print("--------Quiz Completed--------")
print(f"Your final score is {score} out of 5.")