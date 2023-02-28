import mysql.connector
import pandas as pd
import pymysql

class CL_Conexion:
    #Contiene la conexion de las bases de datos
    def __init__(self):
            #Conexio de base
            self.config = {'user': 'root', 'password': 'Heimy311098',
                        'host': '127.0.0.1', 'port':'3306', 'database': 'proyecto_web_noticias', 'raise_on_warnings': True}
            
            self.data = {}
            self.headers = {
                    'token': '7ca057fab5edfb90831da61d0c3cc5bd',
                    'Content-Type': 'application/json'
                }
    #Función que realiza cambios en la base de datos, recibe un query y los valores
    def set_DB(self, query, values):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()
        cursor.execute(query, values)
        id = cursor.lastrowid
        cnx.commit()
        cursor.close()
        cnx.close()
        return id

    #Función que realiza cambios en la base de datos, recibiendo un query o consulta
    def set_DataBase(self, query):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()
        cursor.execute(query)
        id = cursor.lastrowid
        cnx.commit()
        cursor.close()
        cnx.close()
        return id
        
    #Función que obtiene datos de la base según la solicitud del query y retorna un diccionario
    def get_DB(self, query):
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()
        row_headers = []
        cursor.execute(query,)
        # this will extract row headers 
        for x in cursor.description:
            row_headers.append(x[0])
        elements = cursor.fetchall()
        cursor.close()
        cnx.close()
        data = {}
        for element in elements:
            data[element[0]] = (dict(zip(row_headers, element)))
        return data

    #Función que obtiene información  de la base de datos según la dolicitud del query y retorna un arreglo
    def get_DB_value(self, query,value):#get_DB_service
        cnx = mysql.connector.connect(**self.config)
        cursor = cnx.cursor()
        row_headers = []
        cursor.execute(query, value)
        for x in cursor.description:
            row_headers.append(x[0])
        elements = cursor.fetchall()
        cursor.close()
        cnx.close()
        data = []
        for element in elements:
            data.append(dict(zip(row_headers, element)))
        return data