# https://yooloo.tistory.com/137
cd /home/ec2-user/environment/kafka
./bin/connect-distributed.sh -daemon ./config/connect-distributed.properties

kafka-topics.sh --bootstrap-server $MSK_BOOTSTRAP_ADDRESS --command-config /tmp/client_iam.properties --list
kafka-topics.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--delete --topic 


curl -X DELETE "http://localhost:8083/connectors/kafka-connect-source" | jq
curl localhost:8083/connector-plugins | jq
curl --location --request GET 'http://localhost:8083/connectors' | jq
curl --location --request GET 'http://localhost:8083/connectors/kafka-connect-source/status' | jq

curl -X GET "http://localhost:8083/connectors/kafka-connect-source/config" | jq
curl -X GET "http://localhost:8083/connectors/kafka-connect-source/status" | jq

curl -X GET "http://localhost:8083/connectors?expand=status&expand=info" | jq



curl -X GET "http://localhost:8083/connectors/kafka-connect-source/tasks"
curl -X GET "http://localhost:8083/connectors/kafka-connect-source/tasks/0/status"
curl -X GET "http://localhost:8083/connectors/kafka-connect-source/topics" | jq


kafka-topics.sh --bootstrap-server $MSK_BOOTSTRAP_ADDRESS --command-config /tmp/client_iam.properties --describe --topic workshop.ecommerce.orders
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group micro-service-group --describe
kafka-consumer-groups.sh --bootstrap-server $MSK_BOOTSTRAP_ADDRESS --group amazon.msk.canary.group.broker-1 --describe | grep '<topic-name>' | awk '{sum += $5} END {print sum}'

kafka-consumer-groups.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--group amazon.msk.canary.group.broker-1 --offsets --describe

kafka-topics.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--describe --topic workshop.ecommerce.orders



kafka-console-consumer.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--consumer.config /tmp/client_iam.properties \
--topic workshop.ecommerce.orders \
--partition 3 \
--offset 1 \
--property print.key=true \
--property print.value=true
