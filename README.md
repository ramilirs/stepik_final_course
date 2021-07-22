# stepik_final_course
Финальный проект по Selenium+Python

**base_page.py** - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

**locators.py** - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

**main_page.py** - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

**test_main_page.py** - тут мы выполняем сами тесты(assert-ы) по префиксу "test_". Тут вызванные функции будут запускаться.

Здесь мы будем создавать функции, которым:

выдаём нужный для проверки линк
созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
добавляем проверки, которые создавали методами в main_page.py


## Шпаргалки, учебные материалы, полезные команды для настройки Git

git config –list  список конфигураций

git config --global http.proxy proxyaddress:port – настройка прокси-сервера

git config --global http.proxy – установка прокси-сервера

git config --global --unset http.proxy – сброс настроек прокси-сервера

git config --global user.name "Full Name"

git config --global user.email email@address.com

git config --global user.password "********"

git config –list – проверка актуальных настроек сервера

git config --global http.proxy http://**login**:**password**@**proxyadress**:**port** – конфигурирование прокси сервера

q – выйти из git config –list

git config --global –unset {название настройки. Например: http.proxy}

git add –all – добавить все

git commit –m “сообщение которое отправишь при коммите добавленных файлов»

git push origin main – закинуть изменения

git rm <filename> - удалить определенный файл

[Gitflow](https://bitworks.software/2019-03-12-gitflow-workflow.html)

[Ветвление в Git](https://git-scm.com/book/ru/v2/%D0%92%D0%B5%D1%82%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-Git-%D0%9E-%D0%B2%D0%B5%D1%82%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B8-%D0%B2-%D0%B4%D0%B2%D1%83%D1%85-%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%85)

[Цикл разработки через Github](https://habr.com/ru/post/192614/)

[Руководство по Git](https://proglib.io/p/git-for-half-an-hour)

[Шпаргалка по Git](http://rogerdudler.github.io/git-guide/index.ru.html)
 
[Курс обучения по Git](https://githowto.com/ru/setup)

[Тренажер по Git](https://learngitbranching.js.org/?locale=ru_RU)



## Полезные ссылки на xpath и CSS-селекторы

[Шпаргалка по Xpath](https://devhints.io/xpath)

[Псевдоклассы в CSS](https://developer.mozilla.org/ru/docs/Web/CSS/Pseudo-classes)

[1. CSS-селекторы](https://learn.javascript.ru/css-selectors)

[2. CSS-селекторы](https://developer.mozilla.org/ru/docs/Web/CSS/CSS_Selectors)

[3. CSS-селекторы](https://www.w3schools.com/css/css_selectors.asp)

[4. CSS-селекторы](https://puzzleweb.ru/css/selectors.php)

[Тренажер по Xpath](https://topswagcode.com/xpath/)

[Тренажер по CSS-селекторам](https://flukeout.github.io/)

[Список методов find element by](https://selenium-python.com/locating-web-elements)



