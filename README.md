# Обрезка ссылок с помощью Битлинк

Программа принимает на вход командной строки рабочую ссылку сайта и возвращает её ввиде `bit.ly/[код ссылки]`.

Пример ввода: 
``..\Course_Python\API>python3 main.py https://dvmn.org/``

Вывод: "`Битлинк: bit.ly/3Bx5lIm`"

В случае если программа принимает на вход битлинк ссылку - выводит колличество кликов по ней.
Пример ввода: ``..\Course_Python\API>python3 main.py http://bit.ly/3Bx5lIm``

Вывод: `Количество кликов по bit.ly ссылке: 2`

В случае не исправности ссылки программа выведет:
``Ошибка: requests.exceptions.HTTPError``

### Как установить 

Для запуска программы необходим ТОКЕН. 
Получаем его на сайте [Bitly Developer](https://dev.bitly.com/). 
Пример:
```
BITLY_TOKEN = '64742862d105dd2a5d408adf065d2cafb1a0fec2'
```
Вносим BITLY_TOKEN в файл `.env`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).