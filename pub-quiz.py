# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "answer": "B"
    },
    {
        "question": "Which country has won the most FIFA World Cup titles?",
        "options": ["A) France,", "B) Itlay", "c) Argentina", "D) England"],
        "answer": "C"
    }
    # Learners can add more questions here following the same structure
]

score=0

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
        score= score + 1
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print(f"Congrats for taking part . Your total score is  {score}")
print("Thanks for playing the Pub Quiz!")
