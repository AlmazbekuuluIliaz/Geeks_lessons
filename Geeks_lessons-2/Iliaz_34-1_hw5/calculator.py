import random
from decouple import config

initial_money = int(config('MY_MONEY'))


def play_casino_game():
    money = initial_money

    while money > 0:
        print(f"Ваш текущий капитал: ${money}")
        bet = int(input("Сделайте ставку: $"))

        if bet > money:
            print("У вас недостаточно средств для этой ставки.")
            continue

        selected_slot = int(input("Выберите слот (от 1 до 30): "))
        winning_slot = random.randint(1, 30)

        print(f"Вы выбрали слот {selected_slot}, выигрышный слот - {winning_slot}")

        if selected_slot == winning_slot:
            print(f"Вы выиграли ${bet * 2}!")
            money += bet
        else:
            print(f"Вы проиграли ${bet}.")
            money -= bet

        play_again = input("Хотите сыграть еще (y/n)? ").lower()
        if play_again != 'да' or 'y':
            break

    print("Игра завершена")
    if money > initial_money:
        print(f"Вы выиграли ${money - initial_money}!")
    elif money < initial_money:
        print(f"Вы проиграли ${initial_money - money}!")


if __name__ == "__main__":
    play_casino_game()