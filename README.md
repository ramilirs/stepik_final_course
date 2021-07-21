# stepik_final_course
Финальный проект по Selenium+Python
base_page.py - тут мы храним методы которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.

locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать

main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

test_main_page.py - тут мы выполняем сами тесты(assert-ы) по префиксу "test_". Тут вызванные функции будут запускаться.

Здесь мы будем создавать функции, которым:

выдаём нужный для проверки линк
созаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
добавляем проверки, которые создавали методами в main_page.py


## Полезные команды для настройки GIT

git config –list  список конфигураций

git config --global http.proxy proxyaddress:port – настройка прокси-сервера

git config --global http.proxy – установка прокси-сервера

git config --global --unset http.proxy – сброс настроек прокси-сервера

git config --global user.name "Full Name"

git config --global user.email email@address.com

git config --global user.password "********"

git config –list – проверка актуальных настроек сервера

git config --global http.proxy http://<login>:<password>@<proxyadress>:<port> – конфигурирование прокси сервера

q – выйти из git config –list

git config --global –unset {название настройки. Например: http.proxy}

git add –all – добавить все

git commit –m “сообщение которое отправишь при коммите добавленных файлов»

git push origin main – закинуть изменения

git rm <filename> - удалить определенный файл
 