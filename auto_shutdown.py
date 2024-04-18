from time import sleep
import os

seconds = int(input('می خواهید سیستم شما در چند دقیقه دیگر خاموش شود؟'))
seconds = seconds *60
print('تا خاموش شدن سیستم, از برنامه خارج نشوید')
sleep(seconds)
os.system("shutdown /h /f")