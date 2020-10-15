class PlayerCharacter:
	membership = True
	def __init__(self, name):
		self.name = name

	def run(self):
		print(f'run to the edge{PlayerCharacter.membership}')

player1 = PlayerCharacter('harry')

print(player1.run())