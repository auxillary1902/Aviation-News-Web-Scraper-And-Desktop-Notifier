import time
import notify2
import json

def displayNotification():
	with open('newsData.json') as json_data:
		jsonData = json.load(json_data)


	# for i in jsonData:
	# 	print(i['url'])

	notify2.init('News Notifier')
	n = notify2.Notification(None)

	n.set_urgency(notify2.URGENCY_NORMAL)

	n.set_timeout(10000)

	for newsItem in jsonData:
		n.update('Aviation News Notification',newsItem['heading'])
		n.show()
		time.sleep(2)


if __name__ == '__main__':
    displayNotification()

# n.update('Aviation News Notification',"This is the description for the test notification")
# n.show()