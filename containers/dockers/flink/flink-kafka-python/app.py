import os
from pyflink.datastream import StreamExecutionEnvironment, TimeCharacteristic
from pyflink.table import StreamTableEnvironment, CsvTableSink, DataTypes, EnvironmentSettings
from pyflink.table.descriptors import Schema, Rowtime, Json, Kafka, Elasticsearch
from pyflink.table.window import Tumble

import time
import datetime
import random
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

def create_stream_exec_env(result_file):
    s_env = StreamExecutionEnvironment.get_execution_environment()
    s_env.set_parallelism(1)
    s_env.set_stream_time_characteristic(TimeCharacteristic.EventTime)
    st_env = StreamTableEnvironment \
        .create(s_env, environment_settings=EnvironmentSettings
                .new_instance()
                .in_streaming_mode()
                .use_blink_planner().build())
    print("StreamExecutionEnvironment is ready now - {} ".format(st_env))

    register_transactions_source(st_env)
    register_transactions_sink_into_csv(st_env,result_file)   

    st_env.from_path("source").insert_into("sink_into_csv")
    st_env.execute("app")
     
    return st_env

def register_transactions_source(st_env):
    kafka_conn=st_env.connect(Kafka()
                   .version("universal")
                   .topic("transactions-data")
                   .start_from_latest()
                   .property("zookeeper.connect", "kafka-server:2181")
                   .property("bootstrap.servers", "kafka-server:9092"))

    data_format = kafka_conn.with_format(Json()
        .fail_on_missing_field(True)
        .schema(DataTypes.ROW([
        DataTypes.FIELD("name", DataTypes.STRING()),
        DataTypes.FIELD("age", DataTypes.STRING()),
        DataTypes.FIELD("base_location", DataTypes.STRING()),
        DataTypes.FIELD("experience", DataTypes.STRING()),
        DataTypes.FIELD("office_location", DataTypes.STRING())])))

    data_schema = data_format.with_schema(Schema()
        .field("name", DataTypes.STRING())
        .field("age", DataTypes.STRING())
        .field("base_location", DataTypes.STRING())
        .field("experience", DataTypes.STRING())
        .field("office_location", DataTypes.STRING()))

    data_mode = data_schema.in_append_mode()
    data_mode.create_temporary_table("source")
    return st_env

def register_transactions_sink_into_csv(st_env,result_file):    
    if os.path.exists(result_file):
        os.remove(result_file)
    st_env.register_table_sink("sink_into_csv",
                               CsvTableSink(["name",
                                             "age",
                                             "base_location",
                                             "experience",
                                             "office_location"],
                                            [DataTypes.STRING(),
                                             DataTypes.STRING(),
                                             DataTypes.STRING(),
                                             DataTypes.STRING(),
                                             DataTypes.STRING()],
                                            result_file))

def main():
    result_file = "/hsb/son_records.csv"
    get_stream_env = create_stream_exec_env(result_file)
    register_transactions_source(get_stream_env)
    register_transactions_sink_into_csv(get_stream_env,result_file=result_file)
    create_records_topics()

if __name__ == "__main__":
    
    main()        