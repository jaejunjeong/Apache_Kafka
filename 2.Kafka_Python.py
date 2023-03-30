##Install kafka-python
pip install kafka-python

##Create a KafkaAdiminClient object(enable fundamental administrative management operations on kafka server)
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

##Create new topics
#Define empty topic list
topic_list = []

#Use NewTopic class to create topic
new_topic = NewTopic(name="bankbranch", num_partitions= 2, replication_factor=1)
topic_list.append(new_topic)
admin_client.create_topics(new_topics=topic_list)
''' in kafka CLI it is same as "kafka-topics.sh --bootstrap-server localhost:9092 --create --topic bankbranch  --partitions 2 --replication_factor 1" '''

#check topic configuration 
configs = admin_client.describe_configs(
    config_resources=[ConfigResource(ConfigResourceType.TOPIC, "bankbranch")])
''' in kafka CLI kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic bankbranch '''

#define and create a KafkaProducer
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
'''
Since Kafka produces and consumes messages in raw bytes, we need to encode our JSON messages and serialize them
into bytes.

For the value_serializer argument, we define a lambda function to take a Python dict/list object and
serialize it into bytes.
'''

#send message using json format
'''
producer.send("bankbranch", {'atmid':1, 'transid':100})
producer.send("bankbranch", {'atmid':2, 'transid':101})
'''

'''
in kafka CLI kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bankbranch
'''

#define and create a KafkaConsumer subscribing to the topic bankbranch
consumer = KafkaConsumer('bankbranch')
for msg in consumer:
    print(msg.value.decode("utf-8"))
''' in kafka CLI kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch '''

