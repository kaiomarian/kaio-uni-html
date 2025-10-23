create database vendinhaZe;
use vendinhaZe;
create table clientes ( 
id Int-, 
nome VARCHAR(100), 
email VARCHAR(100));
create table pedidos ( 
 id INT,
 cliente_id INT,
 produto VARCHAR(100),
 qnt INT );
 alter table pedidos add data_pedidos date;
 alter table clientes add endereço varchar(50);
 alter table clientes modify nome varchar(150);
 alter table clientes add UF varchar(2);
 alter table clientes add cidade varchar(100);
 alter table pedidos add val_pedido decimal (10,2);
 alter table clientes change endereço edr varchar(100);
 alter table pedidos change cliente_id cli_id int;
 alter table clientes add primary key (id);
 alter table pedidos add primary key (id);
 alter table clientes modify id int auto_increment not null;
 alter table pedidos 
 add constraint fk_cliente 
 foreign key (cli_id) references clientes (id);

