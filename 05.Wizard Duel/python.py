import random

min_health = 0
max_health = 20
player_health = max_health
bot_health = max_health
# spell = [spell_name, damage, healing]
spells = [['fireball', 10, 0], ['metabolism', 0 , 8], ['silence', 0 ,0]]
name = 0
damage = 1
heal = 2

# Print to console
print('''
==========================================
================ OPTIONS =================
Spell Damage Healing''')

i = 1
for row in spells:
    print(f'\n{[i]}', end = '-')
    i +=1
    for elem in row:
        print('\t', elem, end = "")

print(f'''
=========================================
============== WIZARD DUEL ==============
PLAYER vs BOT
{player_health} {bot_health}
=========================================''')     

# Img to ASCII
new_round = '''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||..||||||||||||||||||||||||||||||
|||||||^-||||||||||||||||||||.&!&-.|..||||||||||...-!^^^.|||||
|-||!%@@@$!||||||||||...||||.^^&&&!&!.|||||||.$##@$$@@@$!!-.!.
|&$@$&!--&!||||||||||-&!&--^-!%%^&^-..!!.|||||.&%%&%!%$%!.-@@&
||%@^--!..&|.-^&^^^^^%%%%%&&%%%%^^&^&&^&&--&%^^&&!&!!&@$@##%.|
||||.!$@$@@@$$@$!.||.-&%!-.!^&%^&--!&&&&!.|-&&@$$$$@@@#####^||
|||!#@%!@##$^$$#!|||||-&-.&--!%^&!-...!...||||||-%@@@@#^.!&.||
|||^##@!#@#@^||..||||||||..|.!&-!.|||||||.!^^&||||^$##@&||||||
||^#%.|%#@@@$$.|||||||||||||||.||||||||||&&-.$!|!$$@#$@@.|||||
|^^%^|&##$@@@$@.|||||||||||||||||||||||||!$-...$$$@##@@#&|||||
|^^!!$##@%!..$$!&||||||||||||||||||||||||||-&%^$^!%&.$@@$.||||
||||||-.||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''

win = '''
##########################################
################_||||#||||_###############
###########|||||||||||||||||||||##########
##########$|||||||||||||||||||||$#########
######|||||||||||||||||||||||||||||||#####
######|||||||||__-$$$$$$$$$$|||||||||#####
##$||||||||$|||$$$$$$$$$$$$$|||$||||||||##
###|||||||||$|||$$$$$$$$$$$@||$|||||||||##
####|||||||||$$||$$$$$$$$$|||$|||||||||###
#$||||||||||||||$$$$$$$$$$$@|||||||||||||#
#||||||||||||||||||$$$$$|||||||||||||||||@
###|||||||||||||||||$$$$|||||||||||||||@##
##|||||||||||||||||$$$$$||||||||||||||||$#
#||||||||||||||||||$$$$$$||||||||||||||||@
####-||||||||||||$$$$$$$$$||||||||||||-###
####|||||||||||||$$$$$$$$$||||||||||||-###
####|||||||||||||$$$$$$$$$|||||||||||||###
########||||||||@@||@@@@@@@||||||||#######
########||||||||||||||||||||||||||$#######
#############||||||||||||||||$############
##############||###$|||###$||#############
'''

# ------------- Start -------------

while True:
    #Player select
    print('\nStart Wizard Duel?\n[Y] - Yes\n[N] - No')
    select = input("Your select : ")
    if select == 'N' or select == 'n':
        break
    elif (not select == 'Y') and (not select == 'y'):
        print("Error! Try again.")
    else:
        # Start new game
        print('==========================================')
        print(new_round)
        for round in range(1,4):
            choice = True
            while choice:
                player_select = input("\nSelect spell: ")
                if player_select > '0'and player_select <= str(len(spells)):
                    player_select = int(player_select)
                    player_select = player_select - 1
                    bot_select = random.randint(0, len(spells)- 1 )
                    choice = False
                else:
                    print("Eror! Try again!")  
            play_1 = spells[player_select][name]
            # The spell selected by the player
            play_2 = spells[bot_select][name]
            # The spell selected by the bot
            print(f'''----ROUND No {round}----''')          


