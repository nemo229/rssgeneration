import requests
import feedparser # импортируем библиотеку feedparser
from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.GREEN + "Авто генератор RSS лент, по названию. Вывод постов из RSS " + Fore.WHITE + "v0.1")
print(Fore.GREEN + "Введи одну из предложенных цифр: ") #Выбор для чего генерить RSS ленту
print(Fore.BLUE + "1-Mastodon \n" + Fore.BLUE + "2-Telegram \n" + Fore.BLUE + "3-VK \n" + Fore.MAGENTA + "4-Pixelfed \n" + Fore.BLUE + "5-Twitter \n" + Fore.WHITE + "6-Neural Meduza\n" + "7-Today holidays\n" + Fore.WHITE + "99-info" )
number = input(Fore.YELLOW + "Вы выбрали число: ") #Выбор числа
try:
  number = int(number)
except ValueError:
  print("Это не целое число") #На случай если число не верное
if number == 1: #Mastodon
  print ("Выводить пример генерируемых постов? (yes/no)")
  answer = input ()
  if answer.lower() == 'yes':
    print ("Вы ввели yes")
    url = "https://rss.evv1l.space/?action=display&bridge=MastodonBridge&canusername=%40{word1}%40{word2}&signaturetype=noquery&format=Atom"
    word2 = input("Введите адрес сервера: ") # например, mastodon.social
    word1 = input("Введите id пользователя: ") # например, dge355
    new_url = url.format(word1=word1, word2=word2)
    print(Fore.GREEN + new_url) # вывод нового URL
    url = new_url
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]:
      print(entry.title) # выводит заголовок поста
      #print(entry.summary) # выводит краткое содержание поста
      #print(entry.link) # выводит ссылку на пост
  elif answer.lower() == 'no':
    print ("Вы ввели no")
    url = "https://rss.evv1l.space/?action=display&bridge=MastodonBridge&canusername=%40{word1}%40{word2}&signaturetype=noquery&format=Atom"
    word2 = input("Введите адрес сервера: ") # например, mastodon.social
    word1 = input("Введите id пользователя: ") # например, dge355
    new_url = url.format(word1=word1, word2=word2)
    print(Fore.GREEN + new_url) # вывод нового URL
  else:
    print ("Введите yes или no")
elif number == 2: #Telegram
  print ("Выводить пример генерируемых постов? (yes/no)")
  answer = input ()
  if answer.lower() == 'yes':
    print ("Вы ввели yes")
    nick = input("Введите id: ") # Добавляем ник к url 
    url = "https://rsshub.app/telegram/channel/" + nick
    print(Fore.GREEN + url) # вывод нового URL
    feed = feedparser.parse(url)
    for entry in feed.entries[:5]:
      print(entry.title) # выводит заголовок поста
      #print(entry.summary) # выводит краткое содержание поста
      #print(entry.link) # выводит ссылку на пост
  elif answer.lower() == 'no':
    nick = input("Введите id: ") # Добавляем ник к url 
    url = "https://rsshub.app/telegram/channel/" + nick
    print(Fore.GREEN + url) # вывод нового URL
  else:
    print ("Введите yes или no")
elif number == 3: #VK
  print ("Выводить пример генерируемых постов? (yes/no)")
  answer = input ()
  if answer.lower() == 'yes':
    print ("Вы ввели yes")
    url = "https://feed.eugenemolotov.ru/?action=display&bridge=VkBridge&u={word1}&format=Atom"
    word1 = input("Введите id группы: ") # например, радио свобода
    new_url = url.format(word1=word1)
    print(Fore.GREEN + new_url) # вывод нового URL
    feed = feedparser.parse(new_url)
    for entry in feed.entries[:5]:
      print(entry.title) # выводит заголовок поста
      #print(entry.summary) # выводит краткое содержание поста
      #print(entry.link) # выводит ссылку на пост
  elif answer.lower() == 'no':
    url = "https://feed.eugenemolotov.ru/?action=display&bridge=VkBridge&u={word1}&format=Atom"
    word1 = input("Введите id группы: ") # например, радио свобода
    new_url = url.format(word1=word1)
    print(Fore.GREEN + new_url) # вывод нового URL
  else:
    print ("Введите yes или no")
elif number == 4: #Pixelfed
  url = "https://{word4}/users/{word3}.atom"
  word4 = input("Введите адрес сервера: ") # например, mastodon.social
  word3 = input("Введите id пользователя: ") # например, dge355
  new_url = url.format(word3=word3, word4=word4)
  print(Fore.GREEN + new_url) # вывод нового URL
elif number == 5: #Twitter
  print ("Выводить пример генерируемых постов? (yes/no)")
  answer = input ()
  if answer.lower() == 'yes':
    print ("Вы ввели yes")
    url = "https://feed.eugenemolotov.ru/?action=display&bridge=TwitterBridge&context=By+username&u={word1}&format=Atom"
    word1 = input("Введите id группы: ") # например, радио свобода
    new_url = url.format(word1=word1)
    print(new_url) # вывод нового URL
    feed = feedparser.parse(new_url)
    for entry in feed.entries[:5]:
        print(entry.title) # выводит заголовок поста
  elif answer.lower() == 'no':
    url = "https://feed.eugenemolotov.ru/?action=display&bridge=TwitterBridge&context=By+username&u={word1}&format=Atom"
    word1 = input("Введите id группы: ") # например, радио свобода
    new_url = url.format(word1=word1)
    print(new_url) # вывод нового URL   
  else:
    print ("Введите yes или no")
elif number == 6: #Neural Meduza
  url = "https://rss.evv1l.space/?action=display&bridge=MastodonBridge&canusername=%40neural_meduza%40mastodon.ml&signaturetype=noquery&format=Atom" # задаем URL RSS
  feed = feedparser.parse(url) # разбираем ленту
  for entry in feed.entries[:10]: # количество выводимых постов
    print() # выводим пустую строку для разделения постов
    print(Fore.GREEN + entry.title) # выводим заголовок поста
elif number == 7: # Вывод праздников на сегодня 
  print ("Сегодня такие праздники: ")
  url = "https://www.calend.ru/img/export/today-holidays.rss" # задаем URL RSS
  feed = feedparser.parse(url) # разбираем ленту
  for entry in feed.entries[:4]: # для каждого элемента в ленте
    print(Fore.GREEN + entry.title) # выводим заголовок поста
    print() # выводим пустую строку для разделения постов
elif number == 99: #README?
  print("Тестовая версия, будут обнлвление подробнне в файле README") 
else:
  print(Fore.RED + "Ты ввёл не то что надо, попробуй ещё раз)" + Style.RESET_ALL) #На случай если что-то произойдет не так


  


  
