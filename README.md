<strong>Скрипт позволяет собрать с необходимого сайта список прокси и проверить их на применимость для HTTPS, реализован обход cloudflare.</strong>

Для парсинга списка прокси используется библиотека Selenium, для проверки применимости - библиотека requests, для обхода cloudflare - библиотеки undetected_chromedriver 
и Selenium. За сбор данных с сайта отвечает функция get_proxy, за проверку прокси - check_proxy. Каждая из функций может использоваться самостоятельно.

### Предусловия
Как правило, данные об ip-адресе и порте прокси представлены на сайтах в табличном виде. Скрипт с использованием функции get_proxy позволяет извлекать со страницы эти 
данные.  В скрипте использовании функции get_proxy необходимо указывать адрес сайта (url), номер колонки (col_ip), содержащей информацию об ip-адресе, и номер колонки 
(col_port), содержащей информацию о порте прокси.
```ruby
32   get_proxy(driver, url: str, col_ip: int, col_port: int)
```
## Установка
```ruby
$ git clone https://github.com/SofronovRoman/Check_free_proxy.git
$ cd Check_free_proxy
$ python3 -m pip install -r requirements.txt
```
## Конфигурирование
Задайте в main.py список url (переменная urls) с прокси в табличном виде, задайте значения col_ip и col_port

## Использование
```ruby
$ python3 main.py
```
## Результат
![image](https://user-images.githubusercontent.com/106806612/222446523-f547149a-35f1-4c58-a219-557a7a1862a2.png)


