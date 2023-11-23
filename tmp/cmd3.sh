curl --location --request POST 'http://localhost:8083/connectors' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "kafka-connect-source",
"config": {
        "connector.class":"io.debezium.connector.mysql.MySqlConnector",
        "snapshot.mode":"schema_only",
        "tasks.max":"1",
        "transforms":"unwrap",
        "transforms.unwrap.type":"io.debezium.transforms.ExtractNewRecordState",
        "include.schema.changes":"true",
        "key.converter.schemas.enable":"true",
        "value.converter.schemas.enable":"true",
        "topic.prefix":"workshop",
        "database.hostname":"10.20.100.36",
        "database.port":"3306",
        "database.server.id":"123411",
        "database.user":"testuser",
        "database.password":"testuser",
        "database.connectionTimeZone":"Asia/Seoul",
        "database.include.list":"ecommerce",
        "table.include.list":"ecommerce.product,ecommerce.orders",
        "time.precision.mode":"connect",
        "schema.history.internal.kafka.topic":"workshop",
        "schema.history.internal.kafka.group.id":"kafka-connect-cluster",
        "schema.history.internal.kafka.bootstrap.servers":"b-1.workshopmskcluste.qhqpi8.c2.kafka.ap-northeast-2.amazonaws.com:9098,b-2.workshopmskcluste.qhqpi8.c2.kafka.ap-northeast-2.amazonaws.com:9098,b-4.workshopmskcluste.qhqpi8.c2.kafka.ap-northeast-2.amazonaws.com:9098",
        "schema.history.internal.consumer.security.protocol": "SASL_SSL",
        "schema.history.internal.consumer.sasl.mechanism": "AWS_MSK_IAM",
        "schema.history.internal.consumer.sasl.jaas.config": "software.amazon.msk.auth.iam.IAMLoginModule required;",
        "schema.history.internal.consumer.sasl.client.callback.handler.class": "software.amazon.msk.auth.iam.IAMClientCallbackHandler",
        "schema.history.internal.producer.security.protocol": "SASL_SSL",
        "schema.history.internal.producer.sasl.mechanism": "AWS_MSK_IAM",
        "schema.history.internal.producer.sasl.jaas.config": "software.amazon.msk.auth.iam.IAMLoginModule required;",
        "schema.history.internal.producer.sasl.client.callback.handler.class": "software.amazon.msk.auth.iam.IAMClientCallbackHandler"
    }
}' | jq







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
	"value.converter.schemas.enable":"false",
	"format.class":"io.confluent.connect.s3.format.json.JsonFormat",
	"key.converter":"org.apache.kafka.connect.storage.StringConverter",
	"value.converter":"org.apache.kafka.connect.json.JsonConverter",
	"storage.class":"io.confluent.connect.s3.storage.S3Storage",
	"s3.bucket.name":"chiho-datalake",
	"partition.duration.ms":"3600000",
	"partitioner.class":"io.confluent.connect.storage.partitioner.TimeBasedPartitioner",
	"path.format":"'\'year\''=YYYY/'\'month\''=MM/'\'day\''=dd/'\'hour\''=HH",
	"timezone":"Asia/Seoul",
	"locale":"ko_KR"
  }
}' | jq
