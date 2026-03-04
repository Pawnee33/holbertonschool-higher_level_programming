-- Script that creates hbtn_0d_usa database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- Script that creates table states on your MySQL server
-- Ceates table states on your MySQL server
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) not null
);
