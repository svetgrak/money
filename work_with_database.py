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

    # подключение к postgreSQL (возвращает подключение)
    def open_connection(self):
        try:
            connection = psycopg2.connect(user=self.connect_user, password=self.connect_password,
                                          host=self.connect_host, port=self.connect_port)
            print("Соединение c PostgreSQL установлено")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.connection = connection

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

        return self.get_connection()

    # закрыть любое подключение (передать подключение)
    def close_connection(self, connection):
        try:
            connection.close()
            print("Соединение с PostgreSQL закрыто")

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    #создание базы данных budget_project, передать подключение к postgreSQL
    def create_database(self, connection_postresql):
        try:
            connection_postresql.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

            cursor = connection_postresql.cursor()
            sql_create_database = 'CREATE DATABASE ' + self.database_name
            cursor.execute(sql_create_database)
            print("База данных " + self.database_name + " успешно создана!")

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

        return

    # удалить базу данных (передать имя базы данных и подключение к postgreSQL)
    def delete_database(self, connection_postgresql):
        try:

            cursor = connection_postgresql.cursor()
            sql_delete_database = 'DROP DATABASE ' + self.database_name
            cursor.execute(sql_delete_database)
            print("База данных " + self.database_name + " удалена")

        except(Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)
        return

    # подключение к базе данных по имени database_name (возвращает подключение)
    def open_connection_database(self):
        try:
            connection = psycopg2.connect(user=self.connect_user, password=self.connect_password,
                                          host=self.connect_host, port=self.connect_port,
                                          dbname=self.database_name)

            print("Соединение c базой " + self.database_name + " установлено")
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.connection = connection

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

        return self.get_connection()

    # создать таблицу (передать подключение к базе данных)
    def create_table(self, connection_database):

        try:

            cursor_database = connection_database.cursor()
            create_table_query = '''CREATE TABLE ''' + self.table_name + ''' ( 
                                id bigint NOT NULL,
                                tag text NOT NULL,
                                day date NOT NULL,
                                money bigint NOT NULL,
                                category text NOT NULL,
                                comment text,
                                CONSTRAINT budget_data_pkey PRIMARY KEY (id)
                                )'''
            cursor_database.execute(create_table_query)
            print("Таблица " + self.table_name + " успешно создана!")
            connection_database.commit()

        except (Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)


    # очистить таблицу (передать подключение к базе данных)
    def truncate_table(self, connection_database):
        try:
            cursor_database = connection_database.cursor()
            query_truncate_table = "TRUNCATE " + self.table_name

            cursor_database.execute(query_truncate_table)
            print("Таблица " + self.table_name + " очищена")

        except(Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    # удалить таблицу
    def delete_table(self, connection_database):
        try:
            cursor_database = connection_database.cursor()
            query_truncate_table = "DROP TABLE " + self.table_name

            cursor_database.execute(query_truncate_table)
            print("Таблица " + self.table_name + " удалена")

        except(Exception, Error) as error:
            print("Ошибка при работе с PostgreSQL", error)

    def get_connection(self):
        return self.connection


psql = WorkWithPostgreSQL()
connection_psql = psql.open_connection()
psql.create_database(connection_psql)
psql.close_connection(connection_psql)

connection_db = psql.open_connection_database()
psql.create_table(connection_db)
psql.truncate_table(connection_db)
psql.delete_table(connection_db)
psql.close_connection(connection_db)

connection_psql = psql.open_connection()
psql.delete_database(connection_psql)
psql.close_connection(connection_psql)



