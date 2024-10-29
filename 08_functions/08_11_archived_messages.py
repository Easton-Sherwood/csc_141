messages = ['Hey, hows your day going', 'Its going good, hows yours', 'Mines going great, thanks for asking.']
sent = []

def send_messages(texts):
    while texts:
        text = texts.pop()
        print(f"Sending message: {text}")
        sent.append(text)

send_messages(messages[:])

print("\nOriginal messages list:", messages)
print("Sent messages list:", sent)