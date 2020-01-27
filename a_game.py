import time
player_life=130
player_attack=15

enemy_life=150
enemy_attack=10

while player_life>0 and enemy_life>0:
    player_life-=enemy_attack
    enemy_life-=player_attack
    print('敌人发动攻击后，玩家的血量：'+str(player_life))
    print('玩家发动攻击后，敌人的学量：'+str(enemy_life))
    time.sleep(1.5)
if player_life>0 and enemy_life<=0:
    print("玩家获胜")
else:
    print("敌人获胜")