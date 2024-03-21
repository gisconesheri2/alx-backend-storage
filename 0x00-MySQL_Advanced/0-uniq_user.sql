-- create a table user on any database
CREATE TABLE users IF NOT EXISTS (
    id INT NOT NULL AUTO-INCREMENT,
    email CHAR(255) NOT NULL UNIQUE,
    name CHAR(255),
    PRIMARY KEY (id)
)
