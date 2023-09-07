from work_with_database import *

name_database = "budget_project"

#create_database('budget_project')

def delete():
    connection_psql = open_connection_psql()
    delete_database(name_database, connection_psql)
    close_connection(connection_psql)



delete()

