print("=============== QUIZ MASTER ===============")
print("")
play = input("Do you want to play?(Y/N) ")
print("")
print("===========================================")

if play.upper() != 'Y':
    quit()

score = 0

# Question 1
print("")
print("1. The darkest part of the shadow is")
print("a. Umbra")
print("b. Penumbra")
print("c. Hyperumbra")
print("d. None of these")
answer = input("What is your answer? ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 2
print("")
print("2. What does DNA stands for?")
print("a. Ribonucleic acid")
print("b. Deoxyribonulic acid")
print("c. Folic acid")
print("d. None of these")
answer = input("What is your answer? ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 3
print("")
print("3. What is length?")
print("a. The distance between 100 points")
print("b. The distance between 4 points")
print("c. The distance between 1000 points")
print("d. The distance between 2 points")
answer = input("What is your answer? ")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 4
print("")
print("4. The concept of gravity was discovered by which famous physicist?")
print("a. Galileo Galilei")
print("b. Robert Boyle")
print("c. Isaac Newton")
print("d. Leonardo da Vinci")
answer = input("What is your answer? ")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 5
print("")
print("5. You see your reflection in a mirror because?")
print("a. light is absorbed")
print("b. light is diffracted")
print("c. light is reflected")
print("d. light is refracted")
answer = input("What is your answer? ")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 6
print("")
print("6. Which of these have positive charge and are found in the nucleus of an atom")
print("a. Neutrons")
print("b. Protons")
print("c. Electrons")
print("d. Elements")
answer = input("What is your answer? ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 7
print("")
print("7. One complete revolution of earth around the sun is equal to approximately")
print("a. Year")
print("b. Month")
print("c. Week")
print("d. Day")
answer = input("What is your answer? ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 8
print("")
print("8. Which one of these isn't an organ in the human body?")
print("a. Heart")
print("b. Kidney")
print("c. Brain")
print("d. Spatula")
answer = input("What is your answer? ")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 9
print("")
print("9. How many bones are there in an adult human body?")
print("a. 36")
print("b. 98")
print("c. 206")
print("d. 872")
answer = input("What is your answer? ")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

# Question 10
print("")
print("10. What do Venus and Mercury have in common?")
print("a. Their atmospheres are identical")
print("b. They don't have moons")
print("c. They have nothing in common")
print("d. Their surface temperature are exactly the same")
answer = input("What is your answer? ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("")
print("=========================================")

print("You got " + str(score) + " questions correct!")