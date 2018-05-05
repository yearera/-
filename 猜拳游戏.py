      #猜拳游戏

#import a package,a toolbox
import random

#Waiting for the plarer to enter
player = input('Please input  (a)Scissors  (b)Rock  (c)Paper (d) Exit : ')
while (player != 'a') and (player != 'b') and (player != 'c') and (player != 'd'):
	player = input('Please input  (a)Scissors  (b)Rock  (c)Paper (d) Exit : ')

'''
Don't use these
a = 0
A = 0
b = 1
B = 1
c = 2
C = 2
'''
while player != 'd':
# Ubuntu's enter
	Ubuntu = random.randint(1,3)  #random number 1 to 3, integer only

	if Ubuntu == 1:
		Ubuntu = 'a'
	elif Ubuntu ==2:
		Ubuntu = 'b'
	elif Ubuntu == 3:
		Ubuntu = 'c'

	if (player == 'a' and Ubuntu == 'c') or (player == 'b' and Ubuntu == 'a') or (player == 'c' and Ubuntu == 'b'):
		print('=============================================================')
		print('Ubuntu: %s, You: %s'%(Ubuntu, player))
		print('Congratulations! you win!')
		print('=============================================================')

	elif (player == 'a' and Ubuntu == 'a' ) or (player == 'b' and Ubuntu == 'b' ) or (player == 'c' and Ubuntu == 'c'):
		print('=============================================================')
		print('Ubuntu: %s, You: %s'%(Ubuntu, player))
		print('Draw. Do you want to play again?')
		print('=============================================================')
	elif (player == 'a' and Ubuntu == 'b') or (player == 'b' and Ubuntu == 'C') or (player == 'c' and Ubuntu == 'a'):
		print('=============================================================')
		print('Ubuntu: %s, You: %s'%(Ubuntu, player))
		print('Sorry. You lose. Let\'s fight again!')
		print('=============================================================')


	#Waiting for the plarer to enter
	player = input('Please input  (a)Scissors  (b)Rock  (c)Paper (d) Exit : ')
	while (player != 'a') and (player != 'b') and (player != 'c') and (player != 'd'):
		player = input('Please input  (a)Scissors  (b)Rock  (c)Paper (d) Exit : ')
