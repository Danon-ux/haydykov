class Player:
    def __init__(self):
        self.lives = 3
        self.points = 0
    def guess_number(pc_num):
    for i in range(10):
        if pc_num.count(str(i)) > 0:
            return True
    return False
    def count_points_and_lives(player, pc_num):
    if guess_number(pc_num):
        player.points += 10
    else:
        player.lives -= 1
    print("У вас осталось", player.lives, "жизней")
    player = Player()
while player.lives > 0:
    pc_num = random.randint(1000, 9999)
    guess = int(input("Введите число от 0 до 9: "))
    count_points_and_lives(player, pc_num)

print(f"Вы набрали {player.points} очков.")
print("Рекорд:", max(player.points))
print("Хотите повторить?")
answer = input("Да или нет: ")
