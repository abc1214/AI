import aiml
kernel = aiml.Kernel()
kernel.learn("std-startup1.xml")
kernel.respond("load aiml b")
while True:
 message = input("Enter your message to bot: ")
 if message == "quit":
  break
 else:
  bot_response = kernel.respond(message)
  print(bot_response)
