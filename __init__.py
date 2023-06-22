# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import pymysql
import datetime
from decimal import Decimal
global mysql_module

# Globals declared here
global mod_mysql_sessions
# Default declared here
SESSION_DEFAULT = "default"
# Initialize settings for the module here
try:
    if not mod_mysql_sessions:
        mod_mysql_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_mysql_sessions = {SESSION_DEFAULT: {}}


module = GetParams("module")

if module == "connect":
    host = GetParams("host")
    port = GetParams("port")
    user = GetParams("user")
    password = GetParams("pass")
    database = GetParams("db")
    session = GetParams('session')
    var_ = GetParams("result")

    try:
        if not port or port == "":
            port = 3306
        port = int(port)

        if not session:
            session = SESSION_DEFAULT

        r = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        res = r.open
        mysql_module = {
            'port': port,
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'autocommit': True
        }
        conn = pymysql.connect(**mysql_module)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        mod_mysql_sessions[session] = {
            "connection": r,
            "cursor": cursor
        }
        #r.close()
        SetVar( var_,  res)
    except Exception as e:
        PrintException()
        raise Exception(e)

if module =="query":
    query = GetParams("query")
    session = GetParams('session')
    var_ = GetParams("result")

    try:
        if not session:
            session = SESSION_DEFAULT
        cursor = mod_mysql_sessions[session]["cursor"]
        conn = mod_mysql_sessions[session]["connection"]
        cursor.execute(query)
        if query.upper().startswith('SELECT'):
            data_ = cursor.fetchall()  # Traer los resultados de un select
            for r in data_:
                for d in r:
                    if isinstance(r[d], datetime.date):
                        r[d] = r[d].strftime("%d-%m-%Y %H:%M:%S")
                    if isinstance(r[d], Decimal):
                        r[d] = float(r[d])
            data = data_
        else:
            conn.commit()
            # Hacer efectiva la escritura de datos
            data = True
        #conn.close()
        SetVar(var_, data)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        conn.close()
        raise Exception(e)


if module == "close":
    session = GetParams('session')

    if not session:
        session = SESSION_DEFAULT

    cursor = mod_mysql_sessions[session]["cursor"]
    con = mod_mysql_sessions[session]["connection"]

    try:
        cursor.close()
        con.close()
    except Exception as e:
        PrintException()
        raise e

if module == "getLastInsertedId":
    session = GetParams('session')
    var_ = GetParams("result")

    if not session:
        session = SESSION_DEFAULT
    
    cursor = mod_mysql_sessions[session]["cursor"]
    conn = mod_mysql_sessions[session]["connection"]
    
    table = GetParams("table")
    primaryKey = GetParams("primaryKey")
    if not primaryKey:
        primaryKey = "id"
    
    query = f"SELECT * FROM {table} WHERE {primaryKey}=(SELECT LAST_INSERT_ID())"
    cursor.execute(query)
    
    data_ = cursor.fetchall()  # Traer los resultados de un select
    for r in data_:
        for d in r:
            if isinstance(r[d], datetime.date):
                r[d] = r[d].strftime("%d-%m-%Y %H:%M:%S")
    data = data_

    SetVar(var_, data)

    

