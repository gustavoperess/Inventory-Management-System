-- Database created using PostgreSQL

-- Below is the table for testing purpose

-- Drop tables and sequences if they exist
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS products_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Create sequence for users
CREATE SEQUENCE users_id_seq;

-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    email VARCHAR(255) UNIQUE
);

-- Create sequence for products
CREATE SEQUENCE products_id_seq;

-- Create products table with a foreign key constraint
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    quantity INT,
    category VARCHAR(255),
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Insert sample data into users and products tables
INSERT INTO users (username, password, email) VALUES ('Gustavo', 'gustavo123', 'gustavo123@gmail.com');
INSERT INTO users (username, password, email) VALUES ('Ashley', 'ashley123', 'ashley123@gmail.com');
INSERT INTO users (username, password, email) VALUES ('Mario', 'mario123', 'mario123@gmail.com');
INSERT INTO users (username, password, email) VALUES ('Rosangela', 'rosangela123', 'rosangela123@gmail.com');
INSERT INTO products (product_name, quantity, category, user_id) VALUES ('milk', 5, 'dairy',  1);
INSERT INTO products (product_name, quantity, category, user_id) VALUES ('eggs', 3,  'dairy',  1);
INSERT INTO products (product_name, quantity, category, user_id) VALUES ('lettuce', 1, 'vegetables',  2);
