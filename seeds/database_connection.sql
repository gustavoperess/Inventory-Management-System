DROP TABLE IF EXISTS users_test;

CREATE TABLE users_test (id SERIAL PRIMARY KEY, user_name VARCHAR(255), user_password VARCHAR(255));

INSERT INTO users_test (user_name) VALUES ('first_user', 'first_password');