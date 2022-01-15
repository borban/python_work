invite_list = []
invite_list.append('Elon Musk')
invite_list.append('Grandpa')
invite_list.append('Grandma')
invite_list.append('Teddy Roosevelt')

for person in invite_list: print('Would you come to dinner? ' + person)

print('Unfortunately, ' + invite_list[3] + ' cannot make it...')

del invite_list[3]

for person in invite_list: print('Would you come to dinner? ' + person)