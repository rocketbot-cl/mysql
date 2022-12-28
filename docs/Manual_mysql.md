# MySQL
  
Module for working with MySQL database. Use only if the native version of the command does not work  

*Read this in other languages: [English](Manual_mysql.md), [Español](Manual_mysql.es.md).*
  
![banner](imgs/Banner_mysql.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



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
|Query|Query to execute|select * form db|
|Session|Connection identifier|Conn1|
|Result|Variable where the result of the query is stored|result|

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
