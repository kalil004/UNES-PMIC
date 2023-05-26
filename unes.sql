create database unes;
use unes; 

create table contatos(
email varchar(70),
assunto varchar(20),
descricao varchar(200)
);

create user "root'@'localhost" IDENTIFIED BY 'fatec';
grant all privileges on unes to "root"@"localhost"
