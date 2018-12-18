## #########scala
curl - o / tmp / postgresql - 42.1
.4.jar
https: // jdbc.postgresql.org / download / postgresql - 42.1
.4.jar
spark - shell - -driver -


class -path / tmp / postgresql-42.1.4.jar --jars / tmp / postgresql-42.1.4.jar

# Connection url and the table(can also be  query instead of table)
val url = "jdbc:postgresql://mydbserver.cern.ch:5432/mytestdb?user=postgres&password=newpassword"
val table = "employees"

# Load the table  into DataFrame
val  sDF = spark.read.format("jdbc").options(Map("url" -> url, "dbtable" -> table)).load()

# Print schema and display sample rows
sDF.printSchema()
sDF.show()

#scala JDBC

spark - shell - -driver -class -path ~ /.ivy2 / jars / org.postgresql_postgresql-42.1.4.jar --packages org.postgresql:postgresql: 42.1.4

# Load postgresql jdbc driver
Class.forName("org.postgresql.Driver")

# Connection url and the table(can also be query instead of table)
val url = "jdbc:postgresql://mydbserver.cern.ch:5432/mytestdb?user=postgres&password=newpassword"
val table = "employees"

#Load the table into DataFrame
val sDF = spark.read.format("jdbc").options(
    Map("driver"-> "org.postgresql.Driver", "url" -> url, "dbtable" -> table)).load()

# Print schema and display sample rows
sDF.printSchema()
sDF.show()



# ##################################Pyspark

# download postgresql jdbc driver
curl - o / tmp / postgresql - 42.1.4.jar https: // jdbc.postgresql.org / download / postgresql - 42.1.4.jar
pyspark - -driver -class -path / tmp / postgresql-42.1.4.jar --jars / tmp / postgresql-42.1.4.jar

#connection url and query
url = 'jdbc:postgresql://mydbserver.cern.ch:5432/mytestdb?user=postgres&password=newpassword'
dbtable = '(select * from employees) as emp'

# load the tables into  dataframe
pgsql_df = spark.read.format('jdbc') \
    .options(url=url, dbtable=dbtable) \
    .load()

#printschema and inspect sample rows
pgsql_df.printSchema()
pgsql_df.show()



#################### SCALA   mysql

park - shell - -driver -


class -path ~ /.ivy2 / jars / mysql_mysql-connector-java-5.1.45.jar --packages mysql:mysql - connector - java: 5.1.45

# Load MySQL jdbc driver
Class.forName("com.mysql.jdbc.Driver")

# Connection url and the table (can also be query instead of table)
val url = "jdbc:mysql://mydbserver.cern.ch:5504/metastore?user=spark&password=mypassword"
val table = "TBLS"

# Load the table into DataFrame
val sDF = spark.read.format("jdbc").options(
    Map("driver" -> "com.mysql.jdbc.Driver", "url" -> url, "dbtable" -> table)).load()

# Print schema and display sample rows
sDF.printSchema()
sDF.show()


#####################################Pys spark  mysql

# download mssql jdbc driver
curl - o / tmp / mysql - connector - java - 5.1.45 - bin.jar https: // cernbox.cern.ch / index.php / s / F3UKUDIK11MEFxF / download pyspark - -driver -class -path / tmp / mysql-connector-java-5.1.45-bin.jar --jars / tmp / mysql-connector-java-5.1.45-bin.jar


mysql_df = spark.read.format('jdbc') \
    .options(url='jdbc:mysql://mydbserver.cern.ch:5504/metastore?user=spark&password=mypassword', dbtable='TBLS') \
    .load()
mysql_df.printSchema()
mysql_df.show()

######   EXP

import os
from pyspark.sql import SQLContext
from pyspark import SparkContext
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars /Users/adityaallamraju/hadoop-install/mysql-connector-java-5.1.45/mysql-connector-java-5.1.45-bin.jar  pyspark-shell'


sc = SparkContext(appName="TestPySparkJDBC")
sqlContext = SQLContext(sc)

#Provide your Spark-master node below
hostname = "10.10.75.167"
dbname = "hive"
jdbcPort = 3306
username = "hive"
password = "hive"
jdbc_url = "jdbc:mysql://{0}:{1}/{2}?user={3}&password={4}".format(hostname,jdbcPort, dbname,username,password)


query = "(select * from DBS) t1_alias"
df1 = sqlContext.read.format('jdbc').options(driver = 'com.mysql.jdbc.Driver',url=jdbc_url, dbtable=query ).load()
df1.show()







##### SCALA  SQL SERVER

spark - shell - -driver -class -path ~ /.ivy2 / jars / com.microsoft.sqlserver_mssql-jdbc-6.2.2.jre8.jar --packages com.microsoft.sqlserver:mssql - jdbc: 6.2.2.jre8

# Load MS SQL Server jdbc driver
Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver")

# Connection url and the table (can also be query instead of table)
val url = "jdbc:sqlserver://mydbserver.cern.ch;databaseName=UC;user=hadoop_user;password=mypassword"
val table = "HadoopDemoTable"

# Load the table into DataFrame
val sDF = spark.read.format("jdbc").options(
    Map("driver"->"com.microsoft.sqlserver.jdbc.SQLServerDriver", "url" -> url, "dbtable" -> table)).load()

# Print schema and display sample rows
sDF.printSchema()
sDF.show()


#### Py SPARK  SQL SERVER

# download MS SQL jdbc driver
curl - o / tmp / sqljdbc42.jar https: // cernbox.cern.ch / index.php / s / X23rvfIygUbLlAl / download

pyspark - -driver -class -path / tmp / sqljdbc42.jar --jars / tmp / sqljdbc42.jar


mssql_df = spark.read.format('jdbc') \
    .options(url='jdbc:sqlserver://mydbserver.cern.ch;databaseName=UC;user=hadoop_user;password=mypassword',
             dbtable='HadoopDemoTable') \
    .load()
mssql_df.printSchema()
mssql_df.show()


########################### SCALA ORACLE

spark - shell - -driver - class -path / tmp / ojdbc7.jar --jars / tmp / ojdbc7.jar

# Connection url and the table (can also be query instead of table)


val url = "jdbc:oracle:thin:username/password@hostname:port/service_name"
val table = "applications"

# Load the table into DataFrame
val sDF = spark.read.format("jdbc").options(
    Map("driver"->"oracle.jdbc.driver.OracleDriver", "url" -> url, "dbtable" -> table)).load()

# Print schema and display sample rows
sDF.printSchema()
sDF.show()


####################### Pyspak Oracle

pyspark - -driver -class -path / tmp / ojdbc7.jar --jars / tmp / ojdbc7.jar


orcl_df = spark.read.format('jdbc') \
    .options(driver='oracle.jdbc.driver.OracleDriver',
             url='jdbc:oracle:thin:username/password@hostname:port/servicename', dbtable='applications') \
    .load()
orcl_df.printSchema()
orcl_df.show()



##########################################
jdbc:postgresql://host:port/database[?propertyName1=propertyValue1][&propertyName2=propertyValue2]...

jdbc:mysql://host[,failoverhost]:port/database[?propertyName1=propertyValue1][&propertyName2=propertyValue2]...

jdbc:sqlserver://[serverName[\instanceName][:portNumber]][;propertyName1=propertyValue1][;propertyName2=propertyValue2]...

jdbc:oracle:thin:[username/password]@[host][:port]:sid
jdbc:oracle:thin:[username/password]@//[host][:port]/service

