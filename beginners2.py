# Print hello world

message = 'hello world'
new_message = message.replace('world','universe')
message = message.replace('world','universe')

print (message)
print (len(message))
print (message[10])
print (message[0:5])
print (message[:5])
print (message[6:])
print (message.upper())
print (message.count('hello'))
print (message.count('l'))
print (message.find('world'))
print (message.find('l'))
print (new_message)

greeting = 'Hello'
name = 'Michael'

message = greeting + ', ' + name + '. Welcome!'
message = '{}, {}. Welcome!'.format(greeting, name)
message = f'{greeting}, {name.upper()}. Welcome!'

print (message)
print (dir(name))
print (help(str))
print (help(str.lower))