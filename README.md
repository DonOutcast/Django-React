<h4>Реализованная функциональность</h4>
<ul>
    <li>Отправка статусов в Amplitude;</li>
    <li>Выбор персонажий из web_app;</li>
    <li>Отправка запросов в openAI;</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Для web_app был использован мой личный репозиторий https://github.com/DonOutcast/DonOutcast.github.io;</li>
 <li>Написан на языке Python3.12;</li>
 <li>Использован шаблонизвтор Jinja2;</li>
 <li>Middleware;</li>
 <li>FSM;</li>  
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Python, Aiogram, Asyncio</li>
	<li>HTML, CSS, JavaScript,</li>
    <li>Github, Docker, Poetry</li>

  
 </ul>



СРЕДА ЗАПУСКА
------------
1) Нужно переименовать файлы .env.example  в .env (их два)
2) Если запуск в среде Unix подобных систем то достаточно использовать утилиту make run

ТРЕБОВАНИЯ
------------
1) требуется установленный doccker;
2) требуется установленная python 3.12;
3) требуется наличие postgresql если запуск осуществлен вне докер контейнера или же можно изменить на локальный sqlite3


Запусе
------------
### Установка пакета name

Выполните 
~~~
docker-compose up --build
...
~~~
Вручную
~~~
poetry install
python3 main.py
...
~~~

РАЗРАБОТЧИКИ

<h4>Айдин Шамиль fullstack https://t.me/Hard_Wolf_l </h4>
