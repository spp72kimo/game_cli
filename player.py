class Warrior:
	def __init__(self, name):
		self.name = name
		self.job = '戰士'
		self.hp = 300
		self.atk = 20
		self.defense = 15
		print(self.name, '誕生了！')


	def attack(self,target):
		print(self.name, '攻擊->', target.name)
		print(target.name, 'HP:', target.hp, '-> ', end='')
		if target.defense > self.atk:
			target.hp = target.hp - (target.hp * 5 / 100)
		else:
			target.hp = target.hp - self.atk + target.defense
		print(target.hp)

	def show(self):
		print('Name:', self.name)
		print('Job:', self.job)
		print('HP:', self.hp)
		print('ATK:', self.atk)
		print('DEF:', self.defense, '\n')


class Mage:
	def __init__(self, name):
		self.name = name
		self.job = '法師'
		self.hp = 200
		self.mp = 50
		self.atk = 10
		self.defense = 10
		print(self.name, '誕生了！')

	def attack(self, target):
		if self.mp == 0:
			print('法力用光了！')
		else:
			print(self.name, '攻擊->', target.name)
			print(target.name, 'HP:', target.hp, '-> ', end='')
			if target.defense > self.atk:
				target.hp = target.hp - (target.hp * 5 / 100)
				self.mp -= 10
				print(target.hp)
				if self.mp < 0:
					self.mp = 0
			else:
				target.hp = target.hp - self.atk + target.defense
				self.mp -= 10
				print(target.hp)
				if self.mp < 0:
					self.mp = 0

	def show(self):
		print('Name:', self.name)
		print('Job:', self.job)
		print('HP:', self.hp)
		print('MP:', self.mp)
		print('ATK:', self.atk)
		print('DEF:', self.defense, '\n')


class Monk:
	def __init__(self,name):
		self.name = name
		self.job = '僧侶'
		self.hp = 100
		self.mp = 50
		self.atk = 10
		self.heal = 15
		self.defense = 10
		print(self.name, '誕生了！')

	def attack(self,target):
		if self.mp == 0:
			print('法力用光了！')
		else:
			print(self.name, '攻擊->', target.name)
			print(target.name, 'HP:', target.hp, '-> ', end='')
			if target.defense > self.atk:
				target.hp = target.hp - (target.hp * 5 / 100)
				self.mp -= 10
				print(target.hp)
				if self.mp < 0:
					self.mp = 0
			else:
				target.hp = target.hp - self.atk + target.defense
				self.mp -= 10
				print(target.hp)
				if self.mp < 0:
					self.mp = 0

	def healling(self,target):
		if self.mp == 0:
			print('法力用光了！')
		else:
			print(self.name, '治療->', target.name)
			print(target.name, 'HP:', target.hp, '-> ', end='')
			target.hp = target.hp + self.heal
			self.mp -= 10
			print(target.hp)
			if self.mp < 0:
					self.mp = 0

	def show(self):
		print('Name:', self.name)
		print('Job:', self.job)
		print('HP:', self.hp)
		print('MP:', self.mp)
		print('ATK:', self.atk)
		print('DEF:', self.defense, '\n')				