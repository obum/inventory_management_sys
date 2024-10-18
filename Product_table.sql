create database if not exists product_store;

use product_store;

create table if not exists Products(
product_id INT auto_increment primary key,
product_name varchar(130),
category varchar(130),
stock_quantity INT,
price DOUBLE
);

SELECT product_name FROM products;