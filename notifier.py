import time
import notify2

notify2.init('News Notifier')
n = notify2.Notification(None)

n.set_urgency(notify2.URGENCY_NORMAL)

n.set_timeout(10000)

n.update('Test Notification',"This is the description for the test notification")

n.show()