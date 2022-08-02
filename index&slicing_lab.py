message = input("Please enter a message: ")

print("The first character of your message is: ", message[0])
print("The last character of your message is: ", message[-1])
print("The middle character of your message is: ", message[int(len(message) / 2)])
print("The even characters of your message are: ", message[0::2])
print("The odd characters of your message are: ", message[1::2])
print("Your message reversed is: ", message[::-1])