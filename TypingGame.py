import time
import random

def generate_paragraph():
    paragraphs = ["Python is a popular programming language.",
                  "Artificial intelligence is changing the world.",
                  "Data science is a growing field with many opportunities.",
                  "Web development is an essential skill for modern businesses.",
                  "Machine learning is revolutionizing many industries The quick brown fox jumps over the lazy dog.",
                  "Jackdaws love my big sphinx of quartz.",
                  ]
    return random.choice(paragraphs)

def typing_game():
    print("Welcome to the typing game!")
    name = input("Enter your name: ")
    time_limit = input("Enter the time limit in minutes (1, 2, or 5): ")
    if time_limit not in ["1", "2", "5"]:
        print("Invalid time limit. Please enter 1, 2, or 5.")
        return
    time_limit_seconds = int(time_limit) * 60
    print("You have {} seconds to type as many words as possible. Good luck, {}!".format(
        time_limit_seconds, name))
    time.sleep(1)
    print("Get ready...")
    time.sleep(1)
    print("Go!")
    time.sleep(1)

    words_typed = 0
    start_time = time.time()

    while time.time() - start_time < time_limit_seconds:
        paragraph = generate_paragraph()
        print("Type the following paragraph as quickly and accurately as possible:")
        time.sleep(1)
        print(paragraph)
        user_input = input()
        if user_input.strip() == paragraph:
            words_typed += 1

    score = words_typed / int(time_limit)
    print("Time's up! You typed {} words in {} minutes. Your score is {:.2f}.".format(
        words_typed, time_limit, score))

    with open("scoreboard.txt", "a") as f:
        f.write("{}\t{}\n".format(name, score))

    print("Thank you for playing!")