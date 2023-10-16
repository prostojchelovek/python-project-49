#!/usr/bin/env python3
import brain_games.dialogue


ATTEMPTS = 3


def main():
    name = brain_games.dialogue.welcome_user()
    brain_games.dialogue.start_even_game()
    for _ in range(ATTEMPTS):
        if not brain_games.dialogue.checking_answer(name):
            break
        else:
            print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
