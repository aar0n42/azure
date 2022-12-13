import logging

import azure.functions as func

import pyodbc

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    server = '<name>.database.windows.net'
    database = 'mySampleDatabase'
    username = 'azureuser'
    password = '{<pw>}'
    driver= '{ODBC Driver 18 for SQL Server}'
    strin=""
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT *  FROM SalesLT.Customer")
            row = cursor.fetchone()
            while row:
                strin = strin + " "  + str(row[3])
                row = cursor.fetchone()

    return func.HttpResponse(f"{strin}")
