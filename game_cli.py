import player

def cli_menu():
	choice = 0
	print('物件遊戲：')
	print('1.建造角色')
	print('2.顯示現有角色')
	while True:
		choice = input('請選擇：')
		if choice == 1:
			print('1.戰士')
			print('2.法師')
			print('3.僧侶')
			choice = input('請選擇：')
			name = input('名字：')
			Warrior(name)
