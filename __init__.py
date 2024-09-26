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
import os
import sys
import pymysql
import pandas as pd
import datetime
from decimal import Decimal


# Add modules libraries to Rocektbot
# -----------------------------------
base_path = tmp_global_obj["basepath"]
cur_path = os.path.join(base_path, 'modules', 'mysql', 'libs')

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize >= 2**32 and cur_path_x64 not in sys.path:
        sys.path.append(cur_path_x64)
if sys.maxsize < 2**32 and cur_path_x86 not in sys.path:
        sys.path.append(cur_path_x86)

def import_lib(relative_path, name, class_name=None):
    """
    - relative_path: library path from the module's libs folder
    - name: library name
    - class_name: class name to be imported. As 'from name import class_name'
    """

    import importlib.util

    cur_path = base_path + 'modules' + os.sep + \
        'mysql' + os.sep + 'libs' + os.sep

    spec = importlib.util.spec_from_file_location(
        name, cur_path + relative_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    if class_name is not None:
        return getattr(foo, class_name)
    return foo


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
        if sys.maxsize > 2**32:
            create_engine = import_lib(f"Windows{os.sep}x64{os.sep}sqlalchemy{os.sep}__init__.py", "sqlalchemy", "create_engine") # from sqlalchemy import create_engine
        if sys.maxsize > 32:
            create_engine = import_lib(f"Windows{os.sep}x86{os.sep}sqlalchemy{os.sep}__init__.py", "sqlalchemy", "create_engine") #    

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
            "cursor": cursor,
            "engine": None
        }
        engine = create_engine(
                f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
                echo=False
                )
        mod_mysql_sessions[session]["engine"] = engine        
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

if module =="manyUpdates":
    session = GetParams("session")
    query = GetParams("table")
    colum_values = GetParams("list1")
    clausulas_values = GetParams("list2")
    oneTable = GetParams("onetable")
    var_ = GetParams("result1")
    
    try:
        
        if not session:
            session = SESSION_DEFAULT

        cursor = mod_mysql_sessions[session]["cursor"]
        conn = mod_mysql_sessions[session]["connection"]
        colum_values = eval(colum_values)
        clausulas_values = eval(clausulas_values) 
      
        if oneTable:
            data = list(zip(colum_values, clausulas_values))
        else:
            data = list(zip(*colum_values, clausulas_values))
        cursor.executemany(query, data)
        conn.commit()
        data = True

        SetVar(var_, data)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        conn.close()
        raise Exception(e)

if module =="importData":
    session = GetParams('session')
    hoja = GetParams('hoja')
    schema = GetParams('schema')
    tabla = GetParams('tabla')
    path_file = GetParams('path_file')
    chunk = GetParams('chunk')
    method = GetParams('method')

    try:
        
        if not session:
            session = SESSION_DEFAULT

        if chunk:
            chunk = int(chunk)
        else:
            chunk = None
        
        if not method or method == "None":
            method = None
                
        engine = mod_mysql_sessions[session]["engine"]
        if hoja:
            df = pd.read_excel(path_file, sheet_name=hoja, engine='openpyxl')
        else:
            df = pd.read_excel(path_file, engine='openpyxl')
        
        df.to_sql(tabla, con=engine, schema=schema, if_exists='replace', index=False, chunksize=chunk, method=method)

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

    

