-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);