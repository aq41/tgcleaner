from telethon.sync import TelegramClient

chat = 'XXXXXXXXXXXXX'
api_id = XXXXXXXX
api_hash = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
your_id = XXXXXXXXX

list = []

with TelegramClient('sesssion', api_id, api_hash) as client:
	for message in client.iter_messages(chat):
		if message.sender_id == your_id:
			print(message.sender_id, ':', message.text)
			list.append(message.id)
	client.delete_messages(entity=message.chat.id, message_ids=list)
