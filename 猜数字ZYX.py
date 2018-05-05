# 猜数字游戏编写 2.0
#coding=utf-8

'''
有四位数字，系统自动生成一个四位数的答案.
人来输入四位数，系统返回输入的四位数字，且同时告诉玩家两个信息。1、有几个数字是正确的，但位数不一定相符。2、有几个数字正确，且位数相符的数字。
但是当所采数字完全正确时，提示‘you win’和猜对所用的次数
'''





player = input ('Hello! Do you want to play the Guess-Number game? y/n: ')
print('=================================================================')

# inport an package
import random
A = 0
i99=10000
i100=10000
i101=10000

# 创建一个函数，后面创建防止输入不符合的对象
def numAns():
	# 为了防止位数不够,第一个数字为'1'
	Answer = random.randint(10000,19999)
	
	# while Answer < 101:
	# 	Answer = random.randint(0000,9999)
	
	# 转化成列表
	strAns = str(Answer)
	listAns = list(strAns)
	del listAns[0]


	An1=listAns[0]
	An2=listAns[1]
	An3=listAns[2]
	An4=listAns[3]

	return (Answer,strAns,listAns,An1,An2,An3,An4)
# 防止输入不符合
while (player!='y') and (player!='n'):
	player = input ('Hello! Do you want to play the Guess-Number game? y/n: ')

# 选择难度
while player == 'y':
	print('Please choose difficulty level: ')
	print('[a] One star(easy)  [b] Tow stars (normal)  [c] Three stars (hard)')
	dif = input('Your choise: ')
	while (dif != 'a') and (dif!='b') and (dif!='c'):
		print('Please choose difficulty level: ')
		print('[a] One star(easy)  [b] Tow stars (normal)  [c] Three stars (hard)')
		dif = input('Your choise: ')
	if dif == 'a':
		# Generate an answer
		Answer,strAns,listAns,An1,An2,An3,An4=numAns()
		# In case same figures appear
		while (An1==An2) or (An1==An3) or (An1==An4) or (An2==An3) or (An2==An4) or (An3==An4):
			Answer,strAns,listAns,An1,An2,An3,An4=numAns()

		# 重置数据
		i = 0 # i: 尝试次数
		j = 0 # j：包含的字母个数
		
		# 建立空列表，后面盛放数据
		enterYou = [] # 输入的数字
		enJ = [] # 每次所含的数字个数
		
		while j<4:


			j = 0 # j：包含的字母个数
			# Get the player's number
			print('=============================================================')
			You = input('Please enter the number what you think is Answer: ')
			print('=============================================================')

			# 退出
			if You == 'q':
				You = 1
				break

			# 防止输入的数字数目不为4 
			ansLen = len(You)
			if ansLen != 4:
				print('Sorry! You can only enter 4 figures, neither more nor less!')
				continue

			#  想要知道答案时
			elif You == 'dage':
				print(strAns[1:])
				print('======')
				continue


			elif You.isdigit()==False:
				print('Sorry! You can only enter 4 figures, including no alphabet!')
				continue

			
			# 提取输入的数字
			else:
				strYou = str(You)
				list1 = list(strYou)

			# 判断有几个数字相同
			j1=0
			while j1 < 4:
				if list1[j1] in listAns:
					j+=1
				j1+=1	


			# 输出的结果
			# 为了美观
			print('You   in                    (tried: %s)'%(i+1))
			print('---------------------------------------------')


			i+=1 #判断输入的次数

			# 列表获取数据
			enterYou.append(You)
			enJ.append(j)

			# 输出数据
			Length = len(enterYou)

			L = 0
			while Length>L:
				print('%s   %d   '%(enterYou[L],enJ[L])) 
				L+=1

		# 输出总结果
		if You == 'q':
			print('=============================')
			print('Sorry. You lose.')
			print('You have tried: %d    Best:%d'%(i,i100))
			print('The answer is '+strAns[1:])
			print('=============================')
		# 显示出最好成绩
		if i<i99:
			i99=i 		
		if You != 'q' :
			print('=============================')
			print('Congratulations!! You win!!')
			print('You have tried: %d    Best:%d'%(i,i99))
			print('=============================')

		# 玩家是否继续 
		player = input('Do you want to play again? y/n: ')
		while (player!='y') and (player!='n'):
			player = input('Do you want to play again? y/n: ')

	elif dif == 'b':
		Answer,strAns,listAns,An1,An2,An3,An4=numAns()
		# In case same figures appear
		while (An1==An2) or (An1==An3) or (An1==An4) or (An2==An3) or (An2==An4) or (An3==An4):
			Answer,strAns,listAns,An1,An2,An3,An4=numAns()

		# 重置数据
		A = 0 # A：完全正确的字母的数目
		i = 0 # i: 尝试次数
		j = 0 # j：包含的字母个数
		
		# 建立空列表，后面盛放数据
		enterYou = [] # 输入的数字
		enA = [] # 每次匹配的数字个数
		enJ = [] # 每次所含的数字个数
		
		while A<4:


			A = 0 # A：完全正确的字母的数目
			j = 0 # j：包含的字母个数
			# Get the player's number
			print('=============================================================')
			You = input('Please enter the number what you think is Answer: ')
			print('=============================================================')

			# 退出
			if You == 'q':
				You = 'q'
				break

			# 防止输入的数字数目不为4 
			ansLen = len(You)
			if ansLen != 4:
				print('Sorry! You can only enter 4 figures, neither more nor less!')
				continue

			#  想要知道答案时
			elif You == 'dage':
				print(strAns[1:])
				print('======')
				continue


			elif You.isdigit()==False:
				print('Sorry! You can only enter 4 figures, including no alphabet!')
				continue

			
			# 提取输入的数字
			else:
				strYou = str(You)
				list1 = list(strYou)


			# 判断有几个数字相同
			j1=0
			while j1 < 4:
				if list1[j1] in listAns:
					j+=1
				j1+=1	


			# 判断有几个数字相同，且同时位置相同
			A1=0
			while A1<4:
				if list1[A1] == listAns[A1]:
					A+=1
				A1+=1	


			# 输出的结果
			# 为了美观
			print('You   in  match              (tried: %s)'%(i+1))
			print('---------------------------------------------')


			i+=1 #判断输入的次数

			# 列表获取数据
			enterYou.append(You)
			enA.append(A)
			enJ.append(j)

			# 输出数据
			Length = len(enterYou)

			L = 0
			while Length>L:
				print('%s   %d    %d'%(enterYou[L],enJ[L],enA[L])) 
				L+=1


		# 输出总结果
		if You == 'q':
			print('=============================')
			print('Sorry. You lose.')
			print('You have tried: %d    Best:%d'%(i,i100))
			print('The answer is '+strAns[1:])
			print('=============================')
		# 显示出最好成绩
		if i<i100:
			i100=i 
		if You != 'q':
			print('=============================')
			print('Congratulations!! You win!!')
			print('You have tried: %d    Best:%d'%(i,i100))
			print('=============================')

		# 玩家是否继续 
		player = input('Do you want to play again? y/n: ')
		while (player!='y') and (player!='n'):
			player = input('Do you want to play again? y/n: ')


	elif dif == 'c':
		# Generate an answer
		Answer,strAns,listAns,An1,An2,An3,An4=numAns()

		# 重置数据
		A = 0 # A：完全正确的字母的数目
		i = 0 # i: 尝试次数
		j = 0 # j：包含的字母个数
		
		# 建立空列表，后面盛放数据
		enterYou = [] # 输入的数字
		enA = [] # 每次匹配的数字个数
		enJ = [] # 每次所含的数字个数
		
		while A<4:


			A = 0 # A：完全正确的字母的数目
			j = 0 # j：包含的字母个数
			# Get the player's number
			print('============================================================')
			You = input('Please enter the number what you think is Answer: ')
			print('============================================================')

			# 退出
			if You == 'q':
				You = 'q'
				break

			# 防止输入的数字数目不为4 
			ansLen = len(You)
			if ansLen != 4:
				print('Sorry! You can only enter 4 figures, neither more nor less!')
				continue

			#  想要知道答案时
			elif You == 'dage':
				print(strAns[1:])
				print('======')
				continue



			elif You.isdigit()==False:
				print('Sorry! You can only enter 4 figures, including no alphabet!')
				continue


			
			# 提取输入的数字
			else:
				strYou = str(You)
				list1 = list(strYou)


			# 判断有几个数字相同
			j1=0
			while j1 < 4:
				if list1[j1] in listAns:
					j+=1
				j1+=1	


			# 判断有几个数字相同，且同时位置相同
			A1=0
			while A1<4:
				if list1[A1] == listAns[A1]:
					A+=1
				A1+=1	


			# 输出的结果
			# 为了美观
			print('You   in  match              (tried: %s)'%(i+1))
			print('---------------------------------------------')


			i+=1 #判断输入的次数

			# 列表获取数据
			enterYou.append(You)
			enA.append(A)
			enJ.append(j)

			# 输出数据
			Length = len(enterYou)

			L = 0
			while Length>L:
				print('%s   %d    %d'%(enterYou[L],enJ[L],enA[L])) 
				L+=1
 

		# 输出总结果
		if You == 'q':
			print('=============================')
			print('Sorry. You lose.')
			print('You have tried: %d    Best:%d'%(i,i100))
			print('The answer is '+strAns[1:])
			print('=============================')
		# 显示出最好成绩
		if i<i101:
			i101=i			
		if You != 'q':
			print('=============================')
			print('Congratulations!! You win!!')
			print('You have tried: %d    Best:%d'%(i,i101))
			print('=============================')

		# 玩家是否继续 
		player = input('Do you want to play again? y/n: ')
		while (player!='y') and (player!='n'):
			player = input('Do you want to play again? y/n: ')
		
if player == 'n':
	print('Good bye!')

	
