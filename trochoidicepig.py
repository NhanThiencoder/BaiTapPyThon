import random
from tkinter.font import names


def dice():
    dice1 = random.randint(1,6)
    print(f"Dice 1: {dice1}")
    dice2 = random.randint(1,6)
    print(f"Dice 2: {dice2}")
    tong = dice1 + dice2
    if tong > 5:
        print(f"Summary of two dices: {tong}: Tài")
        return "tai"
    else:
        if tong == 5:
            print(f"Summary of two dices: {tong} Xiu")
            return 5; "xiu"
        else:
            print(f"Summary of two dices: {tong}: Xỉu")
            return "xiu";
def choose():
        while True:
            player_choice = input(f"Chon 1 (nếu chơi tài, xỉu) hoặc 2 nếu nghĩ tổng số xúc xắc bằng 5: ")
            if player_choice == "1":
                level1 = input("Mời bạn chọn Tai hoac Xiu:").lower()
                if level1 == "tai":
                        print("Bạn chọn Tài")
                        return "tai"
                elif level1 == "xiu":
                    print("Bạn chọn Xỉu")
                    return "xiu"
                else:
                   player_choice= input("Mời bạn chọn lại Tài hoặc Xỉu:").lower()
            elif player_choice == "2":
                return "2"
            else: print("Mời bạn chọn lại")
def game_play(mon):
    wins = 0
    while True:
        bet = int(input("Mời bạn chọn mức cược:"))
        if bet < mon:
            current_choice = choose()
            if current_choice == "2":
                if dice() == 5:
                    wins += 1
                    mon += bet * 3
                    print("Ban da chon dung, so tien ban cuoc duoc x3")
                    print(f"So tien hien tai: {mon}")
                else:
                    mon -= bet
                    print("Ban da chon sai")
                    print(f"So tien hien tai: {mon}")
            else:
                if current_choice== dice():
                        wins += 1
                        mon += bet
                        print("Ban da chon dung")
                        print(f"So tien hien tai: {mon}")
                else:
                        mon -= bet
                        print("Ban da chon sai")
                        print(f"So tien hien tai: {mon}")
            if mon <=0:
                print("Ban het tien")
                print(f"Số trận thắng: {wins}")
                break
            reponse = input("Would you like to play again? (y/n): ")
            if reponse == "n":
                print(f"Số trận thắng: {wins}")
                print(f"Tổng số tiền bạn có:{mon}")
                break

if __name__ == '__main__':
    player_money = 10000
    game_play(player_money)



