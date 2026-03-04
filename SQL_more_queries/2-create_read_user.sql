-- Script that creates database 'user_0d_2'
-- Ceates user_0d_2 into the MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Script that creates the MySQL server user 'user_0d_2'
-- Creates server user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Script that grants all privileges on the MySQL server to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
