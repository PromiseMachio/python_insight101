# SQL, MODELS, AND MIGRATIONS
## DATA
In relational databases data is stored in tables and columns like in SQL
### Database Management system
    Mysql
    PostgreSQL
    SQLite

    SQLite Types
        -TEXT
        -NUMERICS
        -INTEGER
        -REAL(can have decimal)
        -BLOB(binary data)

    MySQL Type
        -CHAR(size)
        -VARCHAR(size)
        -SMALLINT
        -BIGINT
        -FLOAT
        -DOUBLE


### Basic SQL commands
#### 1. CREATE TABLE
```
Example creating a table called flight (one can have any desired name)
    CREATE TABLE flights(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        duration INTEGER NOT NULL
    );
    NOTE: This are the columns that we will be having 

    We will also have something called CONSTRAINTS
        -CHECK        => Validates a column meets a specific logical condition
        -DEFAULT      => Assigns an automatic value of non is specified
        -NOT NULL     => Ensures column can not store a null value
        -PRIMARY KEY  => Uniquely identifies each row in a table
        -UNIQUE       => Prevents duplicate values in a column  
        -FORIEN KEY   => Links to table together to maintain referential integrity
    
    
```
#### 2 . ADD DATA INTO A TABLE (INSERT INTO <table_name> (COLUMN VARIABLES) VALUES (DATA) )
```
 Adding data into a table we use a command called insert to our created table
        INSERT INTO flights
        (origin, destination,status, duration)
        VALUES ('Nairobi', 'Kampala','onboarding', 425);

Adding multiple lines 
        INSERT INTO flights
                (origin, destination, status, duration)
                VALUES 
                ('Nairobi', 'Kampala','onboarding', 425),
                ('Bungoma', 'Mombasa','pending', 145),
                ('Turkana', 'Nyamira','onboarding', 200),
                ('Nairobi', 'Siaya','pending', 123);

```

#### 3. RETRIVE DATA FROM A TABLE (SELECT)
```
Retriving all the data in a table we:

```
sql
    SELECT * FROM flights;
```

NOTE: * is a wildcard that states select all

Or you can retrieve with a known data in the columns to get its specific data 

```
sql
   SELECT * FROM flights WHERE origin = 'Nairobi';
```
But data retrival can be filtered and narrowed down to:
        -Specific conditions
            Examples FILTERING ROWS(WHERE):
```
sql
                SELECT origin, destination 
                FROM flights
                WHERE status = 'onboarding' AND duration >= 100
```            
        -Sorting with desending and ascending  (LIMIT => This orders how many rows to return for instance 3)
```
sql
           SELECT origin, duration
           FROM flights
           ORDER BY duration DESC
           LIMIT 3
```


```
Way to display data 
.mode columns
.headers yes

NOTE: In the usage of select and in using conditions of AND or OR we are retriving data from the tables passing certain conditions in them.

##### Functions on numerical data
There are multiple functions in SQL language to compute data
    -Average
    -Count
    -Max
    -Min
    -Sum

#### 4. UPDATE DATA IN A TABLE
Data in a table can be updated using : UPDATE <table_name> SET (desired value in column) and the conditions 
```
sql 
    UPDATE flight 
    SET duration = 500
    WHERE origin = 'Nairobi'
    AND destination = 'Kampala';
```
#### 5. DELETE FROM TABLE
Here we are able to delete data in a table specifing where exactly we want to delete
```
sql
    DELETE FROM flights WHERE destination = 'Kampala';
```
Other clauses 
    -LIMIT
    -ORDER BY
    -GROUP BY
    -HAVING

### RELATIONSHIPS IN SQL 
When working with sql one will have to realize that there could more than one tables and instead there could be like 10 or 20 and all of them are interconnected in some ways so with that in mind we can have tables reffering to other tables with FORIEN KEYS. 
However, that is not enough there still can be a situation where in lets say a flight example a pessanger is related to many flights and so we have examples like: ONE-TO-ONE   (1:1) => One passanger has data on one flight and (vice versa)
                          ONE-TO-MANY  (1:N) => One flight has data on Many passengers while each passanger have their data only on that flight
                          MANY-TO-MANY (M:N) => Passangers have there data on multiple Flights and flights have multiple data related to the passengers 

So in SQL we can have our multiple related data and have them joined together to create a desired output using 
#### JOIN Query
For example we have our passangers table created and we want to join them with their respective flights
```
sql 
    SELECT first, origin, destination
     FROM flights JOIN passangers
    ON passangers.flight_id = flights.id;
```
##### Types of JOINs
    -JOIN / INNER JOIN  => Only rows with matching values in both tables 
    -LEFT OUTER JOIN    => All rows from the left table, plus matched rows from the right table
    -RIGHT OUTER JOIN   => All rows from the right table, plus matched rows from the left table
    -FULL OUTER JOIN    => All rows from where there is a match in either left or right tables
    -CROSS JOIN         => Every possible combination of rows from both tables (cartesian product)
    -SELF JOIN          => Joind a table to itself(using aliases) to compare rows within the same table

##### CREATE INDEX
This is basically a look up structure on one or more tables allowing quick data retrivals
For instance a data of passangers where you will be frequenly checking there last name so one creates an index to enable that
```
sql
    CREATE INDEX name_idx ON passangers (last)
```

### SQL INJECTION ATTACK
This is a cyber threat occuring where untrusted user input concatenated directly into a database query, allowing attackers to manipulate the SQL commands

### RACE CONDITION
This is basically a when two or more concurrent database sessions read and and modifies the same data at the same time , causing the final outcome to depend on timing and leading to corrupted or inconsistent data.





## DELETE IN RELETED TABLES 
There are different types of on_delete options used on ForiegnKey and OneToOneFields to define what happens when the parent is deleted:
    CASCADE => Deletes child row too
    PROTECTS => Parent must never be deleted when the child exists (eg User --> profile)

# DEPARTMENT & STAFF MANAGEMENT SYSTEM.
So we are going to work on a project inside django and in this project we will include the creation of models which will help in the basic CRUD functionality of SQL and the other Clauses mentioned above 

Inside my project I only have one application called:
    depertment =>(nevermind the spelling should have been department)
    Where I have my structure designed in a way that I have:-models Institution 
                 Employees
                 Depertment
This models are interconnected with FK and M:N relationship where an Employee in a certain institution can work in more than one depertment.

       :Inside views => I have quite a number of sophosticated designed fuctions to execute funtionality like 
                        1: Displaying all departments
                        2: Navigating a department and see  the employees registered to it
                        3: Ability to add an employee to a depertment
                        4: Creating an employee dashboard to view their tasks and departments

The rest are common stuffs like the urls, etc
#### New things that I have learnt.
1. The use of python shell in executing sqlite configs like:
                - Inserting data to modules table
                - Viewing data 
                - Assigning variables to data created 
                - Saving the data (variables) 
2. Django admin configurations
                - I have find it easy to use django-admin framework in adding data and saving it
                - Authentication 
                - And designing how to view information inside it using django-admin configurations.
                