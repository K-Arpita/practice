
# Where Data Meets Intelligence
#  1: Develop a basic text-based game.

# Objective: Implement a simple game using conditional statements for game logic.

# Steps:
# 1.Choose a game type (quiz, guessing game).
# 2.Define the game rules and logic.
# 3. Use conditional statements to manage game flow.
# 4.Test and debug the game for correctness.

def quiz():
    questions =[
        {
            "question": "Which country won the 2022 FIFA World Cup?",
            "options": ["1. Germany", "2. France", "3. Argentina", "4. Brazil"],
            "Answer": 3
        },
        {
            "question": "Who was appointed as the Chief Justice of India in 2022?",
            "options": ["1.N.V. Ramana", "2.U.U. Lalit", "3.D.Y. Chandrachud", "4.Ranjan Gogoi"],
            "Answer": 3
        },
        {
            "question": "What is the name of India’s first indigenously developed vaccine for COVID-19?",
            "options": ["1.Covaxin", "2.Covishield", "3.Sputnik V", "4.ZyCoV-D"],
            "Answer": 1
        },
        {
            "question": "The human skeleton is made up of how many bones?",
            "options": ["1.206", "2.210", "3.215", "4.200"],
            "Answer": 1
        },
        {
            "question": "Largest river of India in pensular region?",
            "options": ["1.Ganga", "2.Narmada", "3.Mahanadi", "4.Godavari"],
            "Answer": 4,
        },
        {
            "question": "Which planet is known as the Red Planet ?",
            "options": ["1.Venus", "2.Mars", "3.Jupiter", "4.Saturn"],
            "Answer": 1,
        },
        {
            "question": "What is the process by which plants make their own food?",
            "options": ["1.Digestion", "2.Respiration", "3.Photosynthesis", "4.Transpiration"],
            "Answer": 3,
        },
        {
            "question": "Which is the largest organ in the human body?",
            "options": ["1.Heart", "2.Liver", "3.Brain", "4.Skin"],
            "Answer": 4,
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["1.Gold", "2.Diamond", "3.Iron", "4.Platinum"],
            "Answer": 2,
        },
        {
            "question": "What is the main function of white blood cells?",
            "options": ["1.Carry oxygen", "2.Fight infection", "3.Transport nutrients", "4.Regulate temperature"],
            "Answer": 2,
        },

    ]
    
    print("Welcome to Quiz Game...!")  
    print(" Instructions :"
        "\n Every question has 4 option choose one "
        "\n for correct answer you will get 4 marks "
        "\n for wrongs answer 1 marks will reduced ")
    
    correct_answer = 0
    wrong_answer =0
    Score=0

    for question in questions :
        print("\n",question['question'] )
        for option in question['options']:
            print(option)
            
        try:
            answer = int(input("enter option number:"))
            if answer == question['Answer']:
                print("Good...! its a correct answer")
                Score += 4
                correct_answer +=1
                print("Your Score is = ",Score)
            else:
                print("wrong answer....")
                Score -=1
                wrong_answer +=1
                print("Your Score is = ",Score)
        except ValueError:
            print("invalid input , input with 1-4 only")
            continue

    print(f"Total Correct Answers: {correct_answer}")
    print(f"Total Wrong Answers: {wrong_answer}")
    print(f"\nYour final score is: {Score}/{len(questions)*4}")
    if Score == len(questions) *4 :
        print("Excellent! You got all questions right.")
    elif Score > len(questions) *4 / 2:
        print("Good job! You answered more than half correctly.")
    else:
        print("Better luck next time!")
quiz()



    