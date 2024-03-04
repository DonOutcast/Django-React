<h4>Реализованная функциональность</h4>
<ul>
    <li>Команада для создания супер пользователя python manage.py create_super_user;</li>
    <li>Django Admin Panel(Bootstrap);</li>
    <li>RESTP API для получения списка distributions и статистики;</li>
    <li>Frontend React ajax(with interval);</li>

</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Разделени логики;</li>
 <li>Соответсвеие паттерну MVC;</li>
 <li>Докеризация проекта;</li>
 <li>Makefile;</li>
 <li>Tests;</li>  
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Python, Django, DRF, pytest</li>
	<li>React, axios</li>
    <li>Github, Docker, Poetry</li>

  
 </ul>



СРЕДА ЗАПУСКА
------------
1) Нужно переименовать файлы .env.example  в .env (их два)
2) Если запуск в среде Unix подобных систем то достаточно использовать утилиту make run
3) В Makefile различные команды для работы с backend

ТРЕБОВАНИЯ
------------
1) требуется установленный doccker;
2) требуется установленная python 3.12;
3) требуется node v>=21
4) требуется наличие postgresql если запуск осуществлен вне докер контейнера или же можно изменить на локальный sqlite3


Запуск
------------

Выполните 
~~~
docker-compose up --build
...
~~~
Вручную
~~~
poetry install
python3 main.py
yarn start
...
~~~

РАЗРАБОТЧИКИ

<h4>Айдин Шамиль fullstack https://t.me/Hard_Wolf_l </h4>
