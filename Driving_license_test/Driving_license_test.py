# Define the questions and answer choices
questions = [
    "What should you do if your brakes fail?",
    "What is the speed limit in a residential area?",
    "What does a yellow traffic light mean?",
    "What is the maximum blood alcohol content (BAC) allowed for drivers?",
    "What should you do if you see a pedestrian crossing the road?"
]

multiple_choices = [
    ["A. Steer to the side of the road and stop", "B. Keep driving and hope for the best",
        "C. Try to slow down the vehicle using the gears and handbrake, and steer to the side of the road"],
    ["A. 20 mph", "B. 30 mph", "C. 40 mph"],
    ["A. Stop", "B. Slow down and prepare to stop",
        "C. Speed up and get through the intersection before the light turns red"],
    ["A. 0.05%", "B. 0.08%", "C. 0.10%"],
    ["A. Keep driving and hope the pedestrian moves out of the way",
        "B. Speed up and pass the pedestrian quickly", "C. Stop and give way to the pedestrian"]
]

correct_answers = [
    "C",
    "B",
    "B",
    "B",
    "C"
]

# Define a function to administer the exam


def administer_exam():
    # Request the user's name and age
    name = input("What is your name? ")
    while True:
        try:
            age = int(input("What is your age? "))
            break
        except ValueError:
            print("Please enter a valid age.")

    # Check if the user is under 18 years old
    if age < 18:
        print(
            f"Sorry {name}, you must be at least 18 years old to take the driving test.")
        # Return to the main state with looping
        return True

    # Initialize the score to zero
    score = 0

    # Ask the user each question in turn
    for i in range(len(questions)):
        print(f"Question {i+1}: {questions[i]}")
        for j in range(len(multiple_choices[i])):
            print(multiple_choices[i][j])
        user_answer = input("Your answer: ")

        # Check if the answer is correct
        if user_answer.lower() == correct_answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answers[i]}")

        print()

    # Print the final score and pass/fail status
    print(f"{name}.You scored {score} out of {len(questions)} on your driving test.")
    if score >= 3:
        print("You passed the exam!")
    else:
        print("Sorry, you failed the exam.")

    # Return to the main state without looping
    return False


# Main state loop
while True:
    # Call the function to administer the exam
    loop = administer_exam()
    # If the user is under 18, continue looping
    if loop:
        continue
    # If the user is 18 or older, break the loop and end the program
    else:
        break
