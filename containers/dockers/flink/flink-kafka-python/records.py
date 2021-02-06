from kafka import KafkaProducer 
from json import dumps 

def create_records_topics():
    set_counter = 0
    producer = KafkaProducer(bootstrap_servers=['kafka-server:9092'],
                            value_serializer=lambda x: dumps(x).encode('utf-8'))
    while set_counter <= 100:
        print("Push records to Kafka")
        data = {
                'name':"Tom-"+str(set_counter),
                'age':20+set_counter,
                "base_location":"chennai-"+str(set_counter),
                "experience":str(set_counter),
                "office_location":"chennai-"+str(set_counter)
                }
        future = producer.send('transactions-data', value=data)
        set_counter += 1
        if set_counter > 100:break;
    print("Pushed records to Kafka ... ")
    return True


def main():
    create_records_topics()

if __name__ == "__main__":
    
    main()        