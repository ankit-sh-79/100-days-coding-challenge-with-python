import random
import sys


def get_user_choice():
	prompt = "Choose rock, paper, or scissors (or 'q' to quit): "
	while True:
		choice = input(prompt).strip().lower()
		if choice in ("q", "quit", "exit"):
			return None
		if choice in ("r", "rock"):
			return "rock"
		if choice in ("p", "paper"):
			return "paper"
		if choice in ("s", "scissors", "scissor"):
			return "scissors"
		print("Invalid choice — please type rock, paper, or scissors (or 'q' to quit).")


def decide_winner(user, comp):
	if user == comp:
		return "tie"
	wins = {
		"rock": "scissors",
		"scissors": "paper",
		"paper": "rock",
	}
	if wins[user] == comp:
		return "user"
	return "computer"


def main():
	choices = ["rock", "paper", "scissors"]
	score = {"user": 0, "computer": 0, "tie": 0}
	print("Rock, Paper, Scissors — press Enter to start. Type 'q' to quit anytime.")
	input()
	while True:
		user = get_user_choice()
		if user is None:
			print("Thanks for playing!")
			break
		comp = random.choice(choices)
		result = decide_winner(user, comp)
		if result == "user":
			score["user"] += 1
			print(f"You chose {user}. Computer chose {comp}. You win this round!")
		elif result == "computer":
			score["computer"] += 1
			print(f"You chose {user}. Computer chose {comp}. Computer wins this round.")
		else:
			score["tie"] += 1
			print(f"You chose {user}. Computer chose {comp}. It's a tie.")

		print(f"Score — You: {score['user']}  Computer: {score['computer']}  Ties: {score['tie']}")
		print("---")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nInterrupted. Goodbye!")
		sys.exit(0)

