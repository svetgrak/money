import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from database_info import *


class WorkWithPostgreSQL(object):

    connect_user = psql_user
    connect_password = psql_password
    connect_host = psql_host
    connect_port = psql_port
    database_name = "budget_project"
    table_name = "budget_data"
    connection = ""

    def __init__(self):
        self.open_connection_database()

    # подключение к postgreSQL (возвращает подключение)
    def open_connection(self):
        try:
            self.connection = psycopg2.connect(user=self.connect_user, password=self.connect_password,
                                          host=self.connect_host, port=self.connect_port)
            print("Соединение c PostgreSQL установлено")
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

        return self.connection

    # закрыть любое подключение (передать подключение)
    def close_connection(self):
        try:
            self.connection.close()
            print("Соединение с PostgreSQL закрыто")

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    #создание базы данных budget_project, передать подключение к postgreSQL
    def create_database(self):
        try:
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = self.connection.cursor()
            sql_create_database = 'CREATE DATABASE ' + self.database_name
            cursor.execute(sql_create_database)
            print("База данных " + self.database_name + " успешно создана!")

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

        return

    # удалить базу данных (передать имя базы данных и подключение к postgreSQL)
    def delete_database(self):
        try:
            cursor = self.connection.cursor()
            sql_delete_database = 'DROP DATABASE ' + self.database_name
            cursor.execute(sql_delete_database)
            print("База данных " + self.database_name + " удалена")

        except(Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        return

    # подключение к базе данных по имени database_name (возвращает подключение)
    def open_connection_database(self):
        try:
            self.connection = psycopg2.connect(user=self.connect_user, password=self.connect_password,
                                          host=self.connect_host, port=self.connect_port,
                                          dbname=self.database_name)

            print("Соединение c базой " + self.database_name + " установлено")
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

        return self.connection

    # создать таблицу (передать подключение к базе данных)
    def create_table(self):
        try:
            cursor_database = self.connection.cursor()
            create_table_query = '''CREATE TABLE ''' + self.table_name + ''' ( 
                                id SERIAL PRIMARY KEY,
                                tag text NOT NULL,
                                day date NOT NULL,
                                money int NOT NULL,
                                category text NOT NULL,
                                comment text
                                )'''
            cursor_database.execute(create_table_query)
            print("Таблица " + self.table_name + " успешно создана!")
            self.connection.commit()

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    # создание автоинкремента в таблице для столбца id
    def create_increment_in_table(self):
        return


    # очистить таблицу (передать подключение к базе данных)
    def truncate_table(self):
        try:
            cursor_database = self.connection.cursor()
            query_truncate_table = "TRUNCATE " + self.table_name

            cursor_database.execute(query_truncate_table)
            print("Таблица " + self.table_name + " очищена")

        except(Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    # удалить таблицу
    def delete_table(self):
        try:
            cursor_database = self.connection.cursor()
            query_truncate_table = "DROP TABLE " + self.table_name

            cursor_database.execute(query_truncate_table)
            print("Таблица " + self.table_name + " удалена")

        except(Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)



    #добавить транзакцию в таблицу
    def insert_transaction_in_table(self, data_insert):
        try:
            cursor_database = self.connection.cursor()
            query_insert_in_table = ("INSERT INTO " + self.table_name +
                                     "(tag,day,money,category,comment) VALUES ('+', '2023-09-12', 100, 'питание работа', 'энергетос')")
            cursor_database.execute(query_insert_in_table)
            print("Данные добавлены")
            self.connection.commit()
        except(Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    #удалить транзакцию из таблицы



def init_database():

    psql = WorkWithPostgreSQL()
    psql.close_connection()
    psql.open_connection()
    psql.create_database()
    psql.close_connection()

    psql.open_connection_database()
    psql.create_table()
    psql.insert_transaction_in_table('123')
    psql.close_connection()


psql = WorkWithPostgreSQL()
psql.close_connection()
psql.open_connection()
psql.delete_table()
psql.close_connection()
init_database()




