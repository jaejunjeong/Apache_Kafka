##Download Kafka
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz

##Unzip Kafka
tar -xzf kafka_2.12-2.8.0.tgz

##Start DB
start_mysql

##Connect server
mysql --host=127.0.0.1 --port=3306 --user=root --password=

##Create DB
create database tolldata;

##Create table
use tolldata;
create table livetolldata(timestamp datetime,vehicle_id int,vehicle_type char(15),toll_plaza_id smallint);

##Exit SQL
exit

## Install the python module kafka-python help to communicate with kafka server. It can used to send and receive messages from kafka.
python3 -m pip install kafka-python

##Install the python module mysql-connector-python help to interact with mysql server.
python3 -m pip install mysql-connector-python==8.0.31
