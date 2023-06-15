# MySQL
  
Módulo para trabalhar com banco de dados MySQL. Use apenas se a versão nativa do comando não funcionar  

*Read this in other languages: [English](Manual_mysql.md), [Português](Manual_mysql.pr.md), [Español](Manual_mysql.es.md)*
  
![banner](imgs/Banner_mysql.png o jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Conectar
  
Configure a conexão MySQL, pode usar um identificador para alternar entre outras conexões.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Url do servidor|Url do servidor, pode ser um IP ou um domínio|127.0.0.1|
|Porta|Porta de conexão, padrão 3306|3306|
|Base de dados|Nome da base de dados|database_name|
|Usuário|Usuário do base de dados|Rocketbot|
|Senha|Senha do usuário|secr3t_p@ss|
|Sessão|Identificador de conexão, se vazio, a conexão padrão será usada|Conn1|
|Resultado|Variável onde o resultado da conexão é armazenado|conectado|

### Consulta MySQL
  
Realiza uma consulta MySQL (Select, insert, delete, etc)
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Query|Query to execute|select * from db|
|Sessão|Identificador de conexão|Conn1|
|Resultado|Variável onde o resultado da consulta é armazenado|resultado|

### Obter a última linha inserida
  
Executar uma consulta MySQL para obter a última linha inserida.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Tabela onde a última inserção aconteceu|Nome da tabela onde a última inserção aconteceu|Inventário|
|Chave Primária|Nome da coluna que é chave primária|id|
|Sessão|Identificador de conexão|Conn1|
|Resultado|Variável onde o resultado é armazenado|resultado|

### Fechar conexão
  
Fecha uma conexão de oracle por sessão
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão|Identificador da conexão|Conn1|
