create database cadastro_cd;
use cadastro_cd;
create table gravadora(
cod_grav int primary key,
nome_grav varchar(60),
endereço varchar(100),
telefone varchar(10),
contato varchar(20),
url varchar(80));

create table cd(
cod_cd int primary key,
cod_gravadora int,
nome varchar(100),
preço decimal (14,2),
data_lanc date,
cd_indicado int);

create table musica(
cod_mus int primary key not null auto_increment,
nome_mus varchar(100),
dur_mus decimal (14,2));

create table faixa(
cod_cdfaixa int,
cod_musfaixa int,
numero_faixa int);

 alter table faixa
 add constraint fk_cd
 foreign key (cod_cdfaixa) references cd (cod_cd);
 
 alter table faixa 
 add constraint fk_musica
 foreign key (cod_musfaixa) references musica (cod_mus);
 
 alter table cd 
 add constraint fk_gravadora
 foreign key (cod_gravadora) references gravadora (cod_gra);
 
 alter table gravadora modify nome_gra varchar(80);
 alter table cd drop column cd_indicado;
 alter table cd change nome Título varchar (100);
 alter table gravadora modify url varchar(200);
 alter table gravadora modify cod_grav int not null auto_increment;
 alter table cd change column cod_cd cod_cd int not null auto_increment;
 
