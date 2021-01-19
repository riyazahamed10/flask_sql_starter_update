# Database setup

create database book_shop;

create table book_shop.book_details(
id int primary key auto_increment,
book_name varchar(30) not null,
author_name varchar(30) not null);




DB_TYPE=mysql+pymysql
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=root
DB_NAME=book_shop

DB_URI=mysql+pymysql://root:root@localhost:3306/book_shop

locally run:(passing db value in env)

   1. docker build -t flask_sql_starter .
   2. docker run -e DB_URI=mysql+pymysql://root:root@localhost:3306/book_shop
       -d -p 8000:8000 --network=host flask_sql_starter 

(passing db value in .env file) :
   1. docker build -t flask_sql_starter .
   2. docker run  --env-file .env python:3.7 env | grep DB  (to verify)
   3. docker run --env-file .env -d -p 8000:8000 --network=host flask_sql_starter

  Docker-compose:
   1. docker-compose up --build

  

