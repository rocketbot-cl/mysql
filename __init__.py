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
global mysql_module

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "connect":
    host = GetParams("host")
    port = GetParams("port")
    user = GetParams("user")
    password = GetParams("pass")
    database = GetParams("db")
    var_ = GetParams("result")

    try:
        port = int(port)
        r = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
        res = r.open
        r.close()
        mysql_module = {
                    'port':port,
                    'host': host,
                    'user': user,
                    'password': password,
                    'database': database
                }
        SetVar( var_,  res)
    except Exception as e:
        PrintException()
        raise Exception(e)

if module =="query":
    query = GetParams("query")
    var_ = GetParams("result")

    try:
        conn = pymysql.connect(**mysql_module)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(query)
        if query.upper().startswith('SELECT'):
            data_ = cursor.fetchall()  # Traer los resultados de un select
            for r in data_:
                for d in r:
                    if isinstance(r[d], datetime.date):
                        r[d] = r[d].strftime("%d-%m-%Y %H:%M:%S")
            data = data_
        else:
            conn.commit()  # Hacer efectiva la escritura de datos
            data = True
        conn.close()
        SetVar(var_, data)
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\u2193\x1B[" + "0m")
        PrintException()
        conn.close()
        raise Exception(e)


