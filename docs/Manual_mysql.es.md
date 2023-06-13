# MySQL
  
Módulo para trabajar con base de datos MySQL. Usar solo si no funciona la versión nativa del comando  

*Read this in other languages: [English](Manual_mysql.md), [Português](Manual_mysql.pr.md), [Español](Manual_mysql.es.md)*
  
![banner](imgs/Banner_mysql.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar
  
Configura conexión MySQL, puedes usar un identificador para cambiar entre otras conexiones
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Url de Servidor|Url de servidor, puede ser una IP o un dominio|127.0.0.1|
|Puerto|Puerto de conexión, por defecto 3306|3306|
|Base de datos|Nombre de la base de datos|database_name|
|Usuario|Usuario de la base de datos|Rocketbot|
|Contraseña|Contraseña del usuario|secr3t_p@ss|
|Sesión|Identificador de la conexión, si se deja vacío se usará la conexión por defecto|Conn1|
|Resultado|Variable donde se almacena el resultado de la conexión|conectado|

### Consulta MySQL
  
Realiza una consulta MySQL(Select, insert, delete, etc)
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Consulta|Consulta a realizar|select * from db|
|Sesión|Identificador de la conexión|Conn1|
|Resultado|Variable donde se almacena el resultado de la consulta|resultado|

### Obtener la ultima fila insertada
  
Realiza una consulta a MySQL para obtener la ultima fila insertada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Tabla donde se inserto ultimo|Nombre de la tabla donde se inserto ultimo|Inventory|
|Primary Key|Nombre de la columna que es primary key|id|
|Sesión|Identificador de la conexión|Conn1|
|Resultado|Variable donde se almacena el resultado de la consulta|resultado|

### Cerrar conexión
  
Cierra una conexión de oracle por sesión
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión|Identificador de la conexión|Conn1|
