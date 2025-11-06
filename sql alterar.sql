create database vendinhaZe;
use vendinhaZe;
create table clientes ( 
id Int primary key auto_increment not null, 
nome VARCHAR(100), 
email VARCHAR(100));
create table pedidos ( 
 id INT primary key auto_increment not null,
 cliente_id INT not null,
 produto VARCHAR(100),
 qnt INT );
 alter table pedidos add data_pedidos date;
 alter table clientes add endereço varchar(50);
 alter table clientes modify nome varchar(150);
 alter table clientes add UF varchar(2);
 alter table clientes add cidade varchar(100);
 alter table pedidos add val_pedido decimal (10,2);
 alter table clientes change endereço edr varchar(100);
 alter table pedidos change cli_id cliente_id int;
 alter table clientes add primary key (id);
 alter table pedidos add primary key (id);
 alter table clientes modify id int auto_increment not null;
 create table func(
 id integer not null primary key,
 nome varchar(50),
 salario numeric(10,2)
 );

 alter table pedidos 
 add constraint fk_cliente 
 foreign key (cli_id) references clientes (id);
 
 
 
insert into clientes(id,nome,email,UF,cidade,edr)
values (12,"caliborn", "siids@gmail.com", "CU", "hell","rua bosta"),
(13, "calliope", '', "Ur", "unggu","rua gswgrgrw");
update clientes 
set cidade="muguengue", edr="avenida jesus" where id = 11;
insert into func(id,nome,salario) values
(4,"fb",2034),
(5,"fwe",3694),
(6,"rsjh",1102);
select nome, salario + 200 as aumento from func;
select avg(salario) as media,
sum(salario) as total,
max(salario) as maior,
min(salario) as menor
from func;

delete from func
where id = 3;
