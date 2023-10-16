#!/usr/bin/env python3
import brain_games.games.dialogue


ATTEMPTS = 3


def main():
    name = brain_games.games.dialogue.welcome_user()
    brain_games.games.dialogue.start_even_game()
    for i in range(ATTEMPTS):
        if not brain_games.games.dialogue.checking_answer(name):
            break
        if i == 2:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
