import pygame
import random
import time

# initialize pygame
pygame.init()

# set window size
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# set font and font size
FONT = pygame.font.SysFont('Arial', 30)

# set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# set game variables
TIME_LIMITS = [60, 120, 300] # in seconds
SCORE_PER_WORD = 10
SCORE_PER_SECOND = 1
PARAGRAPHS = [
    "The quick brown fox jumps over the lazy dog.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
    "Python is a popular programming language.",
    "Artificial intelligence is the future.",
    "A picture is worth a thousand words.",
    "Life is like a box of chocolates.",
    "To be or not to be, that is the question.",
    "Education is the key to success.",
    "Actions speak louder than words.",
    "All's well that ends well."
]
SCOREBOARD_FILE = "scoreboard.txt"

# define functions
def get_paragraph():
    # randomly select a paragraph
    return random.choice(PARAGRAPHS)

def calculate_score(text, time_elapsed):
    # calculate score based on the number of correct words and time elapsed
    words = text.split()
    correct_words = 0
    for word in words:
        if word in paragraph:
            correct_words += 1
    score = correct_words * SCORE_PER_WORD + (time_limit - time_elapsed) * SCORE_PER_SECOND
    return score

def show_scoreboard():
    # read scoreboard from file and display it on screen
    scores = []
    with open(SCOREBOARD_FILE, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            scores.append((name, int(score)))
    scores.sort(key=lambda x: x[1], reverse=True)
    text = "SCOREBOARD\n"
    for i, score in enumerate(scores):
        text += f"{i+1}. {score[0]}: {score[1]}\n"
    text_surface = FONT.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    WIN.blit(text_surface, text_rect)
    pygame.display.update()

def save_score(name, score):
    # append name and score to scoreboard file
    with open(SCOREBOARD_FILE, 'a') as file:
        file.write(f"{name},{score}\n")

# set up game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:
    # initialize game variables
    name = ""
    time_limit = 0
    paragraph = ""
    input_text = ""
    time_elapsed = 0
    score = 0

    # display start screen and get player name
    WIN.fill(BLACK)
    text_surface = FONT.render("WELCOME TO TYPING GAME", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//4))
    WIN.blit(text_surface, text_rect)
    text_surface = FONT.render("Enter your name:", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    WIN.blit(text_surface, text_rect)
    pygame.display.update()

    # get player name
pygame.display.update()
name_input = ""
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                name = name_input
                break
            elif event.key == pygame.K_BACKSPACE:
                name_input = name_input[:-1]
            else:
                name_input += event.unicode
    if name:
        break
    WIN.fill(BLACK)
    text_surface = FONT.render("WELCOME TO TYPING GAME", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//4))
    WIN.blit(text_surface, text_rect)
    text_surface = FONT.render("Enter your name:", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    WIN.blit(text_surface, text_rect)
    name_surface = FONT.render(name_input, True, WHITE)
    name_rect = name_surface.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
    WIN.blit(name_surface, name_rect)
    pygame.display.update()

    if game_over:
        break

# display time limit options and get time limit
WIN.fill(BLACK)
text_surface = FONT.render("SELECT TIME LIMIT", True, WHITE)
text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//4))
WIN.blit(text_surface, text_rect)
y = HEIGHT//2
for i, time_limit_option in enumerate(TIME_LIMITS):
    text_surface = FONT.render(f"{i+1} minute{'s' if time_limit_option > 60 else ''}", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, y))
    WIN.blit(text_surface, text_rect)
    y += 50
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if y >= HEIGHT//2 - 25 and y <= HEIGHT//2 + 25:
                    if x >= WIDTH//2 - 150 and x <= WIDTH//2 + 150:
                        time_limit = TIME_LIMITS[(y - HEIGHT//2 + 25) // 50]
                        break
    if time_limit:
        break

    if game_over:
        break

# start game loop with selected time limit
paragraph_surface = None
start_time = time.time()
while time_elapsed < time_limit:
    # display paragraph and input box
    if not paragraph:
        paragraph = get_paragraph()
        paragraph_surface = FONT.render(paragraph, True, WHITE)
    WIN.fill(BLACK)
    WIN.blit(paragraph_surface, (WIDTH//2 - paragraph_surface.get_width()//2, HEIGHT//4))
    input_surface = FONT.render(input_text, True, WHITE)
    input_rect = input_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    pygame.draw.rect(WIN, GRAY, input_rect, 2)
    WIN.blit(input_surface, input_rect)

    # display score and time remaining
    score_surface = FONT.render(f"Score: {score}", True, WHITE)
    score_rect = score_surface.get_rect(topright=(WIDTH - 10, 10))
    WIN.blit(score_surface, score_rect)
    time_elapsed = time.time() - start_time
    time_remaining = max(time_limit - time_elapsed, 0)
    time_remaining_surface = FONT.render(f"Time: {int(time_remaining)}s", True, WHITE)
    time_remaining_rect = time_remaining_surface.get_rect(topleft=(10, 10))
    WIN.blit(time_remaining_surface, time_remaining_rect)

    pygame.display.update()

# handle player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if input_text == paragraph:
                    score += 1
                    input_text = ""
                    paragraph = ""
                else:
                    score = max(0, score - 1)
                    input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

        if game_over:
            break

    # game over screen
    WIN.fill(BLACK)
    text_surface = FONT.render("GAME OVER", True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//4))
    WIN.blit(text_surface, text_rect)
    score_surface = FONT.render(f"Your score is: {score}", True, WHITE)
    score_rect = score_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    WIN.blit(score_surface, score_rect)
    pygame.display.update()

    # save score to file
    with open("scoreboard.txt", "a") as f:
        f.write(f"{name}: {score}\n")

    # wait for player to close window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

