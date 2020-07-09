import pyttsx3
from gtts import gTTS
from tqdm import tqdm
from time import sleep

engn = pyttsx3.init() #инициализация библиотеки pyttsx3

file_path = input( 'Введите путь к файлу: ')  #путь к файлу
file = open( file_path, 'r' ) #открытие файла для чтения
theText = file.read() #чтение и запись файла

engn.say( theText )
engn.runAndWait()
file.close()

for i in tqdm(range(100)):
	sleep(0.01)

tts = gTTS( text = theText, lang = 'en')
tts.save( 'filename.mp3' )

print('Файл сохранен')