#!/usr/bin/python3

def start_quiz(questions):
	score = 0
	for question in questions:
		print(question["prompt"])	
		for option in question["options"]:
			print(option)
		
		answer = input("Enter your answer please: ").upper()
		if answer == question["answer"]:
			print("Correct!\n")
			score += 1
		else:
			print(f"Sorry wrong answer, the correct answer was", question["answer"], "\n")

	print(f"Your score was {score} out of {len(questions)} questions correct")			


questions = [
	{
		"prompt": "What is the capital of France?",
        	"options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        	"answer": "A"
	},
	{	"prompt": "What is the magic number??",
        	"options": ["A. 1", "B. 2", "C. 3", "D. 4"],
	        "answer": "C"
	},
	{	"prompt": "What is danger 5?",
        	"options": ["A. Stupid", "B. Awesome", "C. Very Australian", "D. All three"],
	        "answer": "D"
	}	        
]

start_quiz(questions)
