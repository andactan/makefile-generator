Report Generator
================

This standalone project plots and saves various graphs to be used in weekly report presentations as it fetches and
aggregates daily analyses of the most recent week.

Table of Contents
-----------------
[Project Structure](#project-structure)  
[Creating Procedures in MySQL](#creating-procedures-in-mysql)  
[Connecting to Remote Databases via SSH](#connecting-to-remote-databases-via-ssh)  
[Calling Procedures within Python Code](#calling-procedures-within-python-code)  
[Plotting with Seaborn](#plotting-with-seaborn) 

### Project Structure
   
The project itself is divided into two separate packages:
1. procedures: A simple class to invoke procedure calls of MySQL database through Python interface.
2. visualization : A graph plotter class which uses Seaborn package to visualize fetched results.

You can see tree of project structure below.

```bash
├── procedures
│   ├── __init__.py
│   └── procedure_caller.py
└── visualization
    ├── __init__.py
    └── plot_figures.py
├── requirements.txt
```  

### Creating Procedures in MySQL
Creating and using SQL procedures is no more complex and hard-to-understand than what classical programming languages offer for
function implementation and its relevant call syntax. 

A template syntax of creating a procedure is like this:
```sql
CREATE PROCEDURE [procedure_name](<[IN | OUT | INOUT parameter_name]>)
  BEGIN
    ...do somethin'
  END;
```
A non-creative example of procedure creation would be like:
```sql
CREATE PROCEDURE where_art_thou(IN who VARCHAR(25), OUT here VARCHAR(24))
  BEGIN
    SELECT location INTO here
    FROM locations_table
    WHERE name = who
    ORDER BY day_thou_lost DES
    LIMIT 1;
  END;
```
After creating desired procedure, you must execute the whole procedure code to embed it in database structure.

To call a procedure,
```sql
CALL [procedure_name](<parameters>);
```
should be invoked.

According to our mock procedure we have just written, call syntax looks like this:
```sql
CALL where_art_thou('waldo')
```

For further information, you may want to visit below addressess:  
- <https://dev.mysql.com/doc/connector-net/en/connector-net-tutorials-stored-procedures.html>
- <https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html>
- <https://code.tutsplus.com/articles/an-introduction-to-stored-procedures-in-mysql-5--net-17843>

### Connecting to Remote Databases via SSH
Since all operations is going to be done on a remote MySQL database, a connection through SSH must be established to enable 
Python modules interact with database elements. For the case mentioned, we can make use of a Python library called __sshtunnel__.

Connection to the database could be established with the simple yet effective code below.  

```python
from sshtunnel import SSHTunnelForwarder
from sqlalchemy import create_engine

# Create a tunneling instance
ssh = SSHTunnelForwarder(
      (<remote_server_name>),
      ssh_username = <ssh_user_name>,
      ssh_pkey = <ssh_key>,
      remote_bind_address = (<database_endpoint>, 3306)
      )

# Accomplish, in other words start, SSH connection
ssh.start()

# Create a database engine using create_engine function of SQLAlchemy
engine = create_engine('mysql://<username>:<password>@127.0.0.1:{}/daily_analyses'.format(ssh.local_bind_port))

# Drop, or start, SSH connection.
ssh.stop()
```

### Calling Procedures within Python Code
For the sake of simplicity, using SQLAlchemy framework with raw SQL queries should do the job. A sample call of procedures with SQLAlchemy
is as follows.

```python
from sqlalchemy import text
def call_procedure():
  params = {'who': 'waldo', 'here': ''}
  query = text('CALL where_art_thou(:who, :here)')
  db_cursor = engine.execute(query, params)
  
  return [dict(row) for row in db_cursor]
```

### Plotting with Seaborn
After reliably connecting to database and being able to invoke procedures and getting call results, it is now the time for plotting actions. For the case, plotting library Seaborn is being used which is an extension and polishment over core graph library, just with style improvements.  
- <https://seaborn.pydata.org/index.html>
