import chatterbot

Bot = chatterbot.ChatBot("ChatDot")
Bot.initialize()

print("Starting...")


while True:
    Query = input("Query: \t")
    Response = Bot.get_response(Query)

    print(Query)
    print(Response)
