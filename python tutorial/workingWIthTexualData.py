message = "Hello pranav"
print(message)
print(len(message))
print(message[0])
print(message[0:4])
print(message[:4])
print(message[6:10])
print(message.lower())
print(message.upper())
print(message.count('a'))
print(message.count('Hello'))
print(message.find('p'))
print(message.find('pranav'))
print(message.find('universe'))

# replace message
message = message.replace('pranav','Santosh')
print(message)

message = message + ' ' + 'Kamat'
print(message)

# newer way
name = "gayatri"
surname = "kamat"
message = "{} {} , how are you ".format(name,surname)
print(message)
