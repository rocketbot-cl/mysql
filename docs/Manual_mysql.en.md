



# MySQL
  
Module to work with MySQL database. Use only if the native version of the command does not work  

*Read this in other languages: [English](Manual_mysql.md), [Português](Manual_mysql.pr.md), [Español](Manual_mysql.es.md)*
  
![banner](imgs/Banner_mysql.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect
  
Configure MySQL connection to server, can use identifier for change between others connections
|Parameters|Description|example|
| --- | --- | --- |
|Url Server|Server url, can be an IP or a domain|127.0.0.1|
|Port|Connection port, default 3306|3306|
|Database|Database name|database_name|
|User|Database user|Rocketbot|
|Password|User password|secr3t_p@ss|
|Session|Connection identifier, if empty the default connection will be used|Conn1|
|Result|Variable where the result of the connection is stored|connected|

### Query MySQL
  
Create MySQL query (Select, insert, delete, etc)
|Parameters|Description|example|
| --- | --- | --- |
|Query|Query to execute|select * from db|
|Session|Connection identifier|Conn1|
|Result|Variable where the result of the query is stored|result|

### Executes Multiple Updates
  
Executes multiple updates at once
|Parameters|Description|example|
| --- | --- | --- |
|Session|Connection identifier|Conn1|
|Result|Variable where the result of the query is stored|result|
|Update to be performed|Update to be performed|UPDATE city SET name = %s, capital = %s WHERE ID = %s|
|List of values to assign in the columns in order|List of values to assign in the columns|[['Chile', 'Argentina', 'Venezuela'], ['Santiago', 'Buenos Aires', 'Caracas']]|
|List of clauses|Clause|[1, 2, 3]|
|There is only one column|If this box is checked, means there's only one column to update|True|

### Import data
  
Import data to a MySQL database
|Parameters|Description|example|
| --- | --- | --- |
|Session|Connection session name|Conn1|
|Sheet name|Name of the spreadsheet to import|Sheet1|
|Table schema|Schema of the table to import.|schema|
|Name of the table to import|Name of the SQL table where the data will be imported. If it does not exist, it will be created.|Table|
|Base file path|Base file path to import|Path|
|Batch size|Rows will be written in batches of this size at a time. By default, all rows will be written at once.|2000|
|Method|||

### Get last row inserted
  
Gets the last row inserted
|Parameters|Description|example|
| --- | --- | --- |
|Table were the last insert happened|Table name were the last insert happened|Inventory|
|Primary Key|Column name that is primary key|id|
|Session|Connection identifier|Conn1|
|Result|Variable where the result is stored|result|

### Close connection
  
Close oracle connection for session
|Parameters|Description|example|
| --- | --- | --- |
|Session|Connection identifier|Conn1|
