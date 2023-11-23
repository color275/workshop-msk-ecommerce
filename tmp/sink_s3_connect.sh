curl -X DELETE "http://localhost:8083/connectors/kafka-connect-s3-target" | jq

curl --location --request POST 'http://localhost:8083/connectors' \
--header 'Content-Type: application/json' \
--data-raw '{
  "name": "kafka-connect-s3-target",
  "config": {
    "connector.class":"io.confluent.connect.s3.S3SinkConnector",
	"s3.region":"ap-northeast-2",
	"flush.size":"1",
	"schema.compatibility":"NONE",
	"tasks.max":"1",
	"topics":"workshop.ecommerce.orders",
	"storage.class":"io.confluent.connect.s3.storage.S3Storage",
	"s3.bucket.name":"chiho-datalake",
	"partition.duration.ms":"3600000",
	"partitioner.class":"io.confluent.connect.storage.partitioner.TimeBasedPartitioner",
	"topics.dir":"orders",
    "path.format":"'\'year\''=YYYY/'\'month\''=MM/'\'day\''=dd/'\'hour\''=HH",
	"timezone":"Asia/Seoul",
	"locale":"ko_KR",
	"format.class":"io.confluent.connect.s3.format.parquet.ParquetFormat",	
	"key.converter":"com.amazonaws.services.schemaregistry.kafkaconnect.AWSKafkaAvroConverter",
	"value.converter":"com.amazonaws.services.schemaregistry.kafkaconnect.AWSKafkaAvroConverter",
	"key.converter.schemaAutoRegistrationEnabled":"true",
	"value.converter.schemaAutoRegistrationEnabled":"true",
	"key.converter.region":"ap-northeast-2",
	"value.converter.region":"ap-northeast-2",
	"value.converter.avroRecordType":"GENERIC_RECORD",
	"key.converter.avroRecordType":"GENERIC_RECORD",
	"value.converter.compatibility":"NONE",
	"key.converter.compatibility":"NONE",
	"store.kafka.keys":"false",
	"schema.compatibility":"NONE",
	"value.converter.registry.name":"msk-connect-blog-values",
	"key.converter.registry.name":"msk-connect-blog-keys",
	"store.kafka.headers":"false"
  }
}' | jq

curl --location --request GET 'http://localhost:8083/connectors/kafka-connect-s3-target/status' | jq