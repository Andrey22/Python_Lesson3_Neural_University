#1 методами строк очистить текст от знаков препинания;
import string
import re

x_srt = open('ThirdLessonText.txt', 'r', encoding='UTF-8')
x_srt = x_srt.read()
x_srt = re.sub(r'[^\w\s]','',x_srt)
print(x_srt)