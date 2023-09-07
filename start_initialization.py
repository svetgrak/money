from work_with_database import *

def initialization_test_database():

    name_database = "budget_project"

    create_database(name_database)

    connection_database = open_connection_database(name_database)

    create_table(connection_database)

    close_connection(connection_database)

