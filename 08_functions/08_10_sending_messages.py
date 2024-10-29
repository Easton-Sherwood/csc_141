messages = ['Hey, hows your day going', 'Its going good, hows yours', 'Mines going great, thanks for asking.']
sent = []

def show_messages(texts):
   while texts:
    text = texts.pop()
    print(text)
    sent.append(text)
   print(sent)
   print(messages)


show_messages(messages)
