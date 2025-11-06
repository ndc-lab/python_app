create database if not exists db_registrarr;

use db_registrarr;

create table if not exists tbl_student (
st_ID int unsigned not null primary key auto_increment, 
first_name varchar(100),
last_name varchar(100),
birth_date date,
email text not null
);
 
select * from tbl_student;
