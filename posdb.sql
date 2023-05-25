
Drop database posdb;
create database posdb;


use posdb;


CREATE TABLE newapp_item 
(id INTEGER() NOT NULL AUTO_INCREMENT primary key,
    item_name NVARCHAR(100) NOT NULL,
 item_price DOUBLE(7, 2) NOT NULL,
 stock_quantity INTEGER(3),
 );


INSERT INTO newapp_item (item_name, item_price, stock_quantity)
VALUES ('Burger', 25.00, 80);

INSERT INTO newapp_item
VALUES ('Cheese Burger', 35.00, 60);

INSERT INTO newapp_item
VALUES ('Big Burger', 50.00,45);

INSERT INTO newapp_item
VALUES ('Quarter-Pounder', 70.00, 43);

INSERT INTO newapp_item
VALUES ('Double Burger', 70.00, 76);

