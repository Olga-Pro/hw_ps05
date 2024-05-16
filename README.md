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
</br></br>Загрузка страницы и проверка
* fetch("https://divan.ru")
</br></br>Для тренировки. Ищем тэги h2
* response.css('h2')
</br></br>Для тренировки. Ищем класс
* response.css('h2.vFBoK')
</br></br>Переходим на нужную страницу
* fetch("https://www.divan.ru/category/svet")
</br></br>Отбор данных по классу lsooF
* response.css('div.lsooF')
</br></br>Отбор данных по классу lsooF. 1 Элемент класса
* response.css('div.lsooF').get()
</br></br>Сохранить выгрузку в переменную:
* a=response.css('div.lsooF')
</br></br>Количество элементов в выгрузке:
* len(a)
</br></br>Можно взять любой элемент по индексу:
* a0=a[0]
</br></br>Можно сделать запрос содержимого элемента (взять теэги div, a):
* a0.scc('div')
* a0.scc('a')

</br></br>Код в файле divansvet.py
</br></br>
</br></br>Открываем новый терминал
</br></br>Перейти в каталог проекта в папку spiders:
* cd D:\Документы\GitHub\hw_ps05\divanparssvet\divanparssvet\spiders
</br></br>Выполнить программу:
* scrapy crawl divansvet


