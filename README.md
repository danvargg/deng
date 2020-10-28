# Data Engineering

## Data modeling

### OLAP vs OLTP
- Online Analytical Processing (`OLAP`): Databases optimized for these workloads allow for complex analytical and ad hoc queries, including aggregations. These type of databases are optimized for reads.
- Online Transactional Processing (`OLTP`): Databases optimized for these workloads allow for less complex queries in large volume. The types of queries for these databases are read, insert, update, and delete.

### Structuring the database
- Normalization: 
- Denormalization: 

### Normal form
- To free the database from unwanted insertions, updates, & deletion dependencies
- To reduce the need for refactoring the database as new types of data are introduced
- To make the relational model more informative to users
- To make the database neutral to the query statistics

#### First Normal Form (1NF):
- Atomic values: each cell contains unique and single values
- Be able to add data without altering tables
- Separate different relations into different tables
- Keep relationships between tables together with foreign keys

#### Second Normal Form (2NF):
- Have reached 1NF
- All columns in the table must rely on the Primary Key

#### Third Normal Form (3NF):
- Must be in 2nd Normal Form
- No transitive dependencies
- Remember, transitive dependencies you are trying to maintain is that to get from A-> C, you want to avoid going through B.
- When to use 3NF: When you want to update data, we want to be able to do in just 1 place. We want to avoid updating the table in the Customers Detail table (in the example in the lecture slide).

#### Star schema