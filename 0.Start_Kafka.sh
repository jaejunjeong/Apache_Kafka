##Terminal_1
#download the Apache Kafka
wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz

#unzip Kafka
tar -xzf kafka_2.12-2.8.0.tgz

#Run ZooKeeper
cd kafka_2.12-2.8.0
bin/zookeeper-server-start.sh config/zookeeper.properties

##Terminal_2
#Run Broker service
cd kafka_2.12-2.8.0
bin/kafka-server-start.sh config/server.properties

##Terminal_3
#Create Topic
cd kafka_2.12-2.8.0
bin/kafka-topics.sh --create --topic Sample --bootstrap-server localhost:9092

#Run the Producer
bin/kafka-console-producer.sh --topic Sample --bootstrap-server localhost:9092
#Test words
'''Good morning
Good day
Enjoy the Kafka lab'''

##Terminal_4
#Start consumer
cd kafka_2.12-2.8.0
bin/kafka-console-consumer.sh --topic Sample --from-beginning --bootstrap-server localhost:9092
