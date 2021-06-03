## VKinder

Данный бот подбирает пару по входным данным - возраст, пол, город.
У тех людей, которые подошли по требованиям пользователю, бот получает топ-3 популярных фотографии с аватара. Популярность определяется по количеству лайков.
Результаты о понравившихся людях сохраняются в базу данных PostgreSQL.
## settings.py

Бот использует 2 токена: 

* Токен группы для общения с пользователем, получить его можно в интерфейсе настроек сообщества. Для этого достаточно открыть раздел «Управление сообществом» («Управление страницей», если у Вас публичная страница), выбрать вкладку «Работа с API» и нажать «Создать ключ доступа».


* Персональный токен для поиска по пользователям вконтакте.
https://vk.com/dev/authcode_flow_user
  
Так же нужно указать URL базы данных в формате: postgresql://{user}:{password}@{hostname}:{port}/{database-name}

example: 'postgresql://scott:tiger@localhost/mydatabase'

  