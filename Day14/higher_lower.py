import art, game_data, random, os

clear = lambda: os.system('cls')

score = 0
lost = False

first_choice = random.choice(game_data.data)

while not lost:
    second_choice = random.choice(game_data.data)

    clear()
    print(art.logo)

    print(f"Current score: {score}")

    print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")

    print(art.vs)

    print(f"Compare B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")

    choice = input("Who has more followers? Type'A' or 'B': ").lower()

    if choice == 'a' and first_choice['follower_count'] > second_choice['follower_count']:
        score += 1
        lost = False
    elif choice == 'b' and second_choice['follower_count'] > first_choice['follower_count']:
        score += 1
        lost = False
    elif first_choice['follower_count'] == second_choice['follower_count']:
        score += 1
        lost = False
    else:
        lost = True

    first_choice = second_choice

clear()
print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")