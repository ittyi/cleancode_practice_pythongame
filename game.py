# data structure
class status:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.power = 0

# 入力, status定義
main_character = status()
main_character.name = "itio"
main_character.hp = 10
main_character.power = 2


enemy = status()
enemy.name = "fnufkin"
enemy.hp = 10
enemy.power = 1


boss = status()
boss.name = "tetsu"
boss.hp = 100
boss.power = 9


# 本処理
# ロジックどうしよ。
# 必要なこと
# 最初にバトルコール！
# 戦闘。
# 戦闘の仕組み考案
# 1，お互いのHPをなにかにコピーする→buttleHP
# 2，ターンを交互させる→無限for?
# 3, 攻撃する buttleHPから”相手の”power分毎ターン引く
# 4，HPがゼロになったら終わる。if文？
# 
# 最後に勝者をコール！
# 
# #######

# バトルコール
def call(oneself, enemy):
    print("{}と{}の戦い".format(oneself, enemy))

# statusバックアップ
oneselfHP = main_character.hp
enemyHP = enemy.hp
# 後回し決定


# ターンを進める仕組み
turn = 0
def turn_progression(current):
    return current + 1

# 3, 攻撃する buttleHPから”相手の”power分毎ターン引く
def buttle(oneself_hp, oneself_power, enemy_hp, enemy_power):
    print("{}の攻撃！".format(enemy.name))
    print("{}に{}のダメージ".format(main_character.name, enemy_power))
    print("{}の攻撃！".format(main_character.name))
    print("{}に{}のダメージ".format(enemy.name, oneself_power))
    main_character.hp = oneself_hp - enemy_power
    enemy.hp = enemy_hp - oneself_power
    print("両者残りHP {} : {}".format(main_character.hp, enemy.hp))

# 4，HPがゼロになったら終わる。
def decision_to_win_or_lose(oneself_hp, enemy_hp):
    if oneself_hp > 0 and enemy_hp > 0:
        return 0
    elif oneself_hp <= 0 and enemy_hp >= 1:
        return 1
    elif oneself_hp >= 1 and enemy_hp <= 0:
        return 2
    else :
        return 4

# ##

# 出力

call(main_character.name, enemy.name)

while (True):
    turn = turn_progression(turn)
    print("ターン{}".format(turn))

    buttle(main_character.hp, main_character.power, enemy.hp, enemy.power)
    check = decision_to_win_or_lose(main_character.hp, enemy.hp)
    if check == 0:
        print("続行！")
        continue
    elif check == 1:
        print("{}の勝ち！".format(enemy.name))
        break
    elif check == 2:
        print("{}の勝ち！".format(main_character.name))
        break
    else :
        print("両者引き分け！")
        break