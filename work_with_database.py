import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from database_info import *


def open_connection_psql():
    try:
        connection = psycopg2.connect(user=psql_user,
                                      password=psql_password,
                                      host=psql_host,
                                      port=psql_port)
        print("Соединение c PostgreSQL установлено")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    return connection


def open_connection_database(database_name):

    try:
        connection = psycopg2.connect(user=psql_user,
                                      password=psql_password,
                                      host=psql_host,
                                      port=psql_port,
                                      database=database_name)

        print("Соединение c базой "+database_name+" установлено")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    return connection

def close_connection(connection):

    try:
        connection.close()
        print("Соединение с PostgreSQL закрыто")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def create_database(database_name):

    try:
        connection = open_connection_psql()
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cursor = connection.cursor()
        sql_create_database = 'CREATE DATABASE ' + database_name
        cursor.execute(sql_create_database)
        print("База данных " + database_name + " успешно создана!")
        connection.close()
        print("Соединение с PostgreSQL закрыто")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    return

def delete_database(database_name, connection):
    try:

        cursor = connection.cursor()
        sql_delete_database = 'DROP DATABASE '+ database_name
        cursor.execute(sql_delete_database)
        print("База данных " + database_name + " удалена")

    except(Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    return


def create_table(connection_database):
    try:

        cursor_database = connection_database.cursor()
        create_table_query = '''CREATE TABLE budget_data( 
                            id bigint NOT NULL,
                            tag text NOT NULL,
                            day date NOT NULL,
                            money bigint NOT NULL,
                            category text NOT NULL,
                            comment text,
                            CONSTRAINT budget_data_pkey PRIMARY KEY (id)
                            )'''
        cursor_database.execute(create_table_query)
        print("Таблица budget_data успешно создана!")
        connection_database.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


