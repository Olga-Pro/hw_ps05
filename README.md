# hw_ps05
# scrapy
ДЗ </br>
Попробуй написать spider для нахождения всех источников освещения с сайта divan.ru

Нужно взять название источника освещения, цену и ссылку

*Можно попробовать сделать это на другом сайте с продажей источников освещения


</br>Действия в терминале:
</br></br>Загрузка модуля scrapy:
* pip install scrapy
</br></br>Автоматически создать папки в проекте:
* scrapy startproject divanparssvet
</br></br>Перейти в каталог проекта в папку spiders:
* cd D:\Документы\GitHub\hw_ps05\divanparssvet\divanparssvet\spiders
</br></br>Автоматически создать файл в папке spiders:
* scrapy genspider divansvet divan.ru
</br></br>В файле divansvet.py исправить ссылки.
</br></br>Загрузка модуля ipython (наверное, можно было это сделать вначале):
* pip install ipython
</br></br>В файле srcapy.cfg, в секции settings добавить shell=ipython.
</br></br>Запуск интерактивной оболочки в терминале (для возможности выполнения запросов):
* scrapy shell
</br></br>Проверка загрузки страницы
* fetch("https://divan.ru")


