
Список задач из уроков
======================


Lesson 1
--------

Функционал:
    Первая часть домашнего задания будет заключаться в реализации простого клиент-серверного
    взаимодействия по протоколу JIM (JSON instant messaging):
    1. клиент отправляет запрос серверу;
    2. сервер отвечает соответствующим кодом результата.
    
    Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие
    функции.

Функции ​​клиента​:
    1. сформировать presence-сообщение;
    2. отправить сообщение серверу;
    3. получить ответ сервера;
    4. разобрать сообщение сервера;
    5. параметры командной строки скрипта client.py <addr> <port>:
       1. addr - ip-адрес сервера;
       2. port - tcp-порт на сервере, по умолчанию 7777.

Функции ​​сервера​:
    1. принимает сообщение клиента;
    2. формирует ответ клиенту;
    3. отправляет ответ клиенту;
    4. имеет параметры командной строки:
       1. -p <port> - TCP-порт для работы (по умолчанию использует порт 7777);
       1. -a <addr> - IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).

Тесты:
    Для всех функций необходимо написать тесты с использованием doctest (небольшие тесты в
    документации функций), unittest или py.test (в дальнейшем упор будет делаться на библиотеку py.test).
    Тесты должны быть оформлены в отдельных скриптах с префиксом test_ в имени файла (например,
    test_client.py).

Дополнительно:
    В качестве практики написания тестов напишите тесты для домашних работ курса Python-1.



# Lesson 2
----------

Основное задание:
    Реализовать логгирование с использованием модуля logging:
    1. Реализовать декоратор @log, фиксирующий обращение к декорируемой функции:
    сохраняет имя функции и её аргументы.
    2. Настройку логгера выполнить в отдельном модуле log_config.py:
       1. Создание именованного логгера.
       2. Сообщения лога должны иметь следующий формат:
    "<дата-время> <уровень_важности> <имя_модуля> <имя_функции> <сообщение>"
       3. Журналирование должно производиться в лог-файл.
       4. На стороне сервера необходимо настроить ежедневную ротацию лог-файлов
       5. Реализовать обработку нескольких клиентов на сервере с использованием
    функции select таким образом, что клиенты общаются в "общем чате", т.е.
    каждое сообщение каждого клиента отправляется всем клиентам,
    подключенным к серверу.
       6. Реализовать функции отправки/приёма данных на стороне клиента. Для
    упрощения разработки приложения на данном этапе пусть клиентское
    приложение будет либо только принимать, либо только отправлять сообщения в
    общий чат:
       7. запуск скрипта клиента должен осуществляться с параметром командной
    строки: -r (чтение чата) или -w (передача сообщений в чат).
       8. Для всех функций необходимо написать тесты.

Дополнительно:
    1. Реализовать скрипт, запускающий два клиентских приложения - одно на чтение чата, другое на
    запись в чат (уместно использовать модуль subprocess).
    2. Реализовать скрипт, запускающий указанное количество клиентских приложений.
    3. Для ОС UNIX реализовать обработку выбора ввода данных от пользователя с клавиатуры и
    чтение из сокета с использованием функции select.
    4. В декораторе @log реализовать фиксацию функции, из которой была вызвана декорированная
    функция. Т.е. если имеется код:
    ```python
    @log
    def func_z():
        pass
        
    def main():
        func_z()
    ```
    То в логе должна быть отражена информация:
    "<дата-время> Функция func_z() вызвана из функции main"


# Lesson 3
----------

Основное задание:

    Перейти к объектной модели в реализации проекта “Мессенджер”. В качестве основы
    слушателям предлагается следующая ООП-модель системы:
    1. Класс JIMСообщение - класс, реализующий сообщение (msg) по протоколу JIM.
    2. Класс JIMОтвет - класс, реализующий ответ (response) по протоколу JIM.
    3. Класс Клиент - класс, реализующий клиентскую часть системы.
    4. Класс Чат - класс, обеспечивающий взаимодействие двух клиентов.
    5. Класс ЧатКонтроллер - класс, обеспечивающий передачу данных из Чата в
    ГрафическийЧат и обратно; обрабатывает события от пользователя (ввод данных,
    отправка сообщения).
    6. Класс ГрафическийЧат - базовый класс, реализующий интерфейс пользователя (UI) -
    вывод сообщений чата, ввод данных от пользователя - служит базой для разных
    интерфейсов пользователя (консольный, графический, WEB).
       1. Дочерний класс КонсольныйЧат - обеспечивает ввод/вывод в простой консоли.
    7. Класс Сервер - базовый класс сервера мессенджера; может иметь разных потомков -
    работающих с потоками или выполняющих асинхронную обработку.
    8. Класс Хранилище - базовый класс, обеспечивающий сохранение данных (сохранение
    информации о пользователях на сервере, сохранение сообщений на стороне клиента).
       1. Дочерний класс ФайловоеХранилище - обеспечивает сохранение информации в
    текстовых файлах
    3. Для всех методов и функций необходимо написать тесты.
       1. Уместно воспользоваться дескрипторами для реализации атрибутов классов.

Дополнительное задание:
    1. Реализовать метакласс ClientVerifier, выполняющий базовую проверку класса Клиент (для
    некоторых проверок уместно использовать модуль dis):
       1. отсутствие вызовов accept и listen для сокетов
       2. использование сокетов для работы по TCP
       3. отсутствие создания сокетов на уровне классов, т.е. отсутствие конструкций вида:
        ```python
        class Client:
            s = socket()
        ```
    
    2. Реализовать метакласс ServerVerifier, выполняющий базовую проверку класса Сервер:
       1. отсутствие вызовов connect для сокетов;
       2. использование сокетов для работы по TCP.


# Lesson 4
----------
1. Реализовать класс Хранилище для клиента и сервера. Хранение необходимо осуществлять в
базе данных. В качестве базы данных можно выбрать любую СУБД (sqlite, PostgreSQL, MySQL
и прочие). Для взаимодействия с БД можно использовать ORM.
В качестве опорной схемы базы данных предлагается следующий вариант.
На стороне сервера БД содержит следующие таблицы:
    1. клиент:
        1. логин;
        2. информация.
    2. история_клиента:
        1. время входа;
        2. ip-адрес.
    3. список_контактов (составляется на основании выборки всех записей с id_владельца)
        1. id_владельца;
        2. id_клиента.
    4. Реализовать хранение информации в БД на стороне клиента:
        1. список_контактов;
        2. история_сообщений.

2. Реализовать функционал работы со списком контактов по протоколу JIM:
Получение​​ списка ​​контактов
Запрос к серверу:
```json
{
  "action": "get_contacts",
  "time": <unix timestamp>,
}
```
Положительный ответ сервера будет состоять из нескольких частей. Первая часть содержит код
результата и количество контактов текущего пользователя:
```json
{
  "response": 202,
  "quantity": xxx # количество контактов
}
```
Далее сервер отсылает xxx сообщений формата:
```json
{
  "action": "contact_list",
  "user_id": "nickname"
}
```

Получение списка контактов - не самая частая операция при взаимодействии с сервером. Она должна
выполняться после подключения (и авторизации) клиента. Инициируется клиентом. В процессе
получения списка контактов клиенту не допускается инициировать другие запросы.
Добавление/удаление​​контакта​в список контактов:
Запрос к серверу:
```json
{
    "action": "add_contact" | "del_contact",
  "user_id": "nickname",
  "time": <unix timestamp>,
}
```

Ответ сервера будет содержать одно сообщение с кодом результата и не обязательной
расшифровкой:
```json
{
  "response": xxx,
}
```

Для работы со списком контактов предлагается реализовать дополнительные классы:
    1. СписокКонтактов - класс, реализующий операции с контактами (добавление,
удаление);
    2. КонтактКонтроллер - класс, реализующий взаимодействие классов СписокКонтактов и
СписокКонтактовGUI;
    3. СписокКонтактовGUI - базовый класс для отображения списка контактов (консольный,
графический, WEB)

2. * Реализовать возможность создавать чат для нескольких пользователей (группа):
   1. хранение информации о группах в БД сервера;
   2. отправка сообщений пользователям группы.


# Lesson 5
----------
Реализовать графический интерфейс для мессенджера, используя библиотеку PyQt.
1. Реализовать графический интерфейс пользователя на стороне клиента:
   1. отображение списка контактов;
   2. выбор чата двойным кликом на элементе списка контактов;
   3. добавление нового контакта в локальный список контактов;
   4. отображение сообщений в окне чата;
   5. набор сообщения в окне ввода сообщения;
   6. отправка ввёденного сообщения.
2. *Реализовать графический интерфейс администратора сервера:
   1. отображение списка всех клиентов
   2. отображение статистики клиентов
   3. настройка сервера (подключение к БД, идентификация)

# Lesson 6
----------
1. Реализовать многопоточность на сервере (обработка многих соединений) и клиенте (работа с
несколькими чатами):
   1. на стороне сервера организовать обработку клиентских запросов с использованием
потоков;
   2. на стороне клиента реализовать приём/отправку сообщений с использованием потоков.
2. *На стороне сервера реализовать обработку клиентов в отдельных процессах.


# Lesson 7
----------
1. Реализовать аутентификацию пользователей на сервере.
2. Реализовать декоратор @login_required, проверяющий авторизованность пользователя для
выполнения той или иной функции.
3. Реализовать хранение паролей в БД сервера (пароли не хранятся в открытом виде - хранится
хэш-образ от пароля с добавлением криптографической соли).
4. *Реализовать возможность сквозного шифрования сообщений (использовать асимметричный
шифр, ключи хранятся только у клиентов).
5. *Реализовать поддержку протокола ssl.


# Lesson 8
----------
1. Подготовить приложение для клиента.
   1. Подготовить документацию проекта с использованием sphinx-doc.
   2. Сформировать whl-пакеты с дистрибутивами сервера и клиента.
2. Настроить buildbot/tox для проекта “Мессенджер”.