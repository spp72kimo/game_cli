import player

Alex = player.Warrior('Alex')
Jason = player.Mage('Jason')
Steven = player.Monk('Steven')

Alex.show()
Jason.show()
Steven.show()

Alex.attack(Jason)
Jason.show()
print(type(Jason))
Steven.healling(Jason)