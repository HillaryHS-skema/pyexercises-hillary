# Survive the Quarter - Croissant Rocket (Scenario A)
# Name: Hillary HARI SOEJONO
# Group letter: A
# Group number: CL05
#
# 1. WHAT GOES IN?
# The file scenarios_A.csv uses commas and contains 14 columns.
# ID identifies a scenario; Scenario is the story; OptionA/B/C are the choices.
# BudgetA/B/C and ReputationA/B/C are whole-number changes (some negative).
# FeedbackA/B/C tell the player what happened. The player also enters a name and choice.
#
# 2. WHAT HAPPENS DURING ONE DAY?
# First, display the day, current gauges, story and three choices.
# Next, ask for A, B or C and repeat the question for an invalid answer.
# Then, apply the selected budget/reputation changes and show the feedback.
# Finally, record the move and check whether a gauge reached zero.
# If the player survives, also check whether they earned the streak bonus.
#
# 3. WHAT COMES OUT?
# The player sees either a fired message or a final title, plus their gauges.
# They also see their best and worst moves. Each game adds one line to results.csv.
# The saved columns are name, budget, reputation, title and date.
#
# 4. WHAT COULD GO WRONG?
# An invalid choice: ask again until it is A, B or C.
# Reputation over 100: stop it at 100.
# Budget or reputation at zero or below: stop the game immediately.
# A missing or badly formatted CSV: explain the problem instead of crashing.
#
# MY EXTRA FEATURE: A - Streak bonus.
# Three actual reputation gains in a row earn 500 EUR for the company.
# I chose it because it rewards consistency and practices if statements and counters.

import csv
import random
from datetime import date
from pathlib import Path

FOLDER = Path(__file__).parent
SCENARIO_FILE = FOLDER / "scenarios_A.csv"
RESULTS_FILE = FOLDER / "results.csv"


# This function reads each CSV row and turns A, B and C into option tuples.
def load_scenarios():
    scenarios = []
    with open(SCENARIO_FILE, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            options = {}
            for letter in "ABC":
                options[letter] = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter]
                )
            scenarios.append((row["Scenario"], options))
    return scenarios


# This function keeps asking until the player enters a valid letter.
def ask_choice():
    while True:
        answer = input("Your choice (A, B or C): ").strip().upper()
        if answer in ("A", "B", "C"):
            return answer
        print("Please type A, B or C.")


# This function returns two new gauge values as a tuple.
def apply_choice(budget, reputation, option):
    option_text, budget_change, reputation_change, feedback = option
    budget = budget + budget_change
    reputation = min(100, reputation + reputation_change)
    return budget, reputation


# This function gives a title based on the score in the brief.
def get_title(budget, reputation):
    score = reputation + budget // 200
    if score < 95:
        title = "Eternal Intern"
    elif score < 120:
        title = "Growth Hacker"
    elif score < 140:
        title = "CMO Material"
    else:
        title = "Viral Legend"
    return score, title


# This function appends one result, and creates a header only if needed.
def save_result(name, budget, reputation, title):
    needs_header = not RESULTS_FILE.exists() or RESULTS_FILE.stat().st_size == 0
    with open(RESULTS_FILE, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if needs_header:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, date.today().isoformat()])


# This function manages the ten days, the bonus, and the game-ending rules.
def play_game():
    print("=== SURVIVE THE QUARTER: CROISSANT ROCKET ===")
    name = input("What is your name? ").strip() or "Anonymous"

    try:
        scenarios = load_scenarios()
    except (FileNotFoundError, KeyError, ValueError, csv.Error) as error:
        print("Could not load scenarios_A.csv:", error)
        return

    if len(scenarios) < 10:
        print("The scenario file needs at least 10 scenarios.")
        return

    random.shuffle(scenarios)
    budget = 10000
    reputation = 50
    streak = 0
    history = []              # Each tuple: (real reputation change, day, choice text)
    final_title = ""

    for day in range(1, 11):
        story, options = scenarios[day - 1]
        print(f"\n--- Day {day} ---")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(story)
        for letter in "ABC":
            print(f"  {letter}: {options[letter][0]}")

        choice = ask_choice()
        option_text, budget_change, reputation_change, feedback = options[choice]
        old_reputation = reputation
        budget, reputation = apply_choice(budget, reputation, options[choice])
        real_change = reputation - old_reputation
        history.append((real_change, day, option_text))

        print(feedback)
        print(f"Budget {budget_change:+d} EUR | Reputation {real_change:+d}")

        # Losing either gauge ends the game before any possible bonus.
        if budget <= 0 or reputation <= 0:
            if budget <= 0 and reputation <= 0:
                reason = "both budget and reputation reached zero or less"
            elif budget <= 0:
                reason = "the budget reached zero or less"
            else:
                reason = "reputation reached zero or less"
            final_title = "Fired"
            print(f"\nGAME OVER: You are fired because {reason}.")
            break

        # Only a real gain counts; reaching the 100-point cap is not a gain.
        if real_change > 0:
            streak += 1
        else:
            streak = 0
        if streak == 3:
            budget += 500
            streak = 0
            print("STREAK BONUS! Three reputation gains: +500 EUR!")

    # Surviving all ten days gives a score and title.
    if final_title != "Fired":
        score, final_title = get_title(budget, reputation)
        print("\nQUARTER SURVIVED!")
        print(f"Final score: {score}")
        print(f"{name}, your title is: {final_title}")

    print(f"Final budget: {budget} EUR | Final reputation: {reputation}/100")
    if history:
        best = max(history)
        worst = min(history)
        print(f"Best move: day {best[1]}, '{best[2]}' ({best[0]:+d})")
        print(f"Worst move: day {worst[1]}, '{worst[2]}' ({worst[0]:+d})")

    try:
        save_result(name, budget, reputation, final_title)
        print("Saved in results.csv")
    except OSError as error:
        print("Could not save results.csv:", error)



# This starts the game when I run the Python file.
if __name__ == "__main__":
    try:
        play_game()
    except Exception as error:
        print("Something went wrong:", error)