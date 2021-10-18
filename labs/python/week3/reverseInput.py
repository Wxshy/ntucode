message = input('Please enter a message: ').split()

message.sort(reverse=True)
print([i for i in message])