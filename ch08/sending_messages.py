# Exercise 8-10. Sending Messages

def send_messages(to_send, sent):
    """Print the messages from the list 'to_send' and move them to the list 'sent'."""
    while to_send:
        msg = to_send.pop()
        print("Sending message:", msg)
        sent.append(msg)

messages_to_send = ["Hi", "How are you?", "Good morning", "Good afternoon", "Good evening", "Good night"]
sent_messages = []

send_messages(messages_to_send, sent_messages)

print("\nto send:", messages_to_send)
print("sent:", sent_messages)
