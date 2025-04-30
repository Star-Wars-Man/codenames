def displayWinner(winner):
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    TROPHY = "🏆"
    CONFETTI = "🎉"
    WIDTH = 80
    LINE = "=" * WIDTH

    def center(text):
        return text.center(WIDTH)

    if winner == "red":
        print(f"\n{RED}{LINE}")
        print(center(f"{TROPHY}  RED TEAM WINS!  {TROPHY}"))
        print(center(f"{CONFETTI} Congrats Players 1 and 3! {CONFETTI}"))
        print(f"{LINE}{RESET}\n")
    elif winner == "blue":
        print(f"\n{BLUE}{LINE}")
        print(center(f"{TROPHY}  BLUE TEAM WINS!  {TROPHY}"))
        print(center(f"{CONFETTI} Congrats Players 2 and 4! {CONFETTI}"))
        print(f"{LINE}{RESET}\n")
    else:
        print(center("❗ Invalid winner specified."))