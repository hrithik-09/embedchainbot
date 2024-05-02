from embedchain import App
chat_bot = App()
# chat_bot.add("youtube_video","__ADD YOUR LINK__")
# chat_bot.add("web_page","__ADD YOUR LINK__")
chat_bot.add("https://replit.com/@HRITHIKRANJAN/embedchainbot#nanomaterials-10-01700-v2-1.pdf")
while True:
 input_query = input("\nAsk your Question: ")
 answer = chat_bot.query(input_query)
 print(f"Answer: {answer}\n")

