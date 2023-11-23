kafka-topics.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--delete --topic kafka-connect-configs | jq
kafka-topics.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--delete --topic kafka-connect-offsets | jq
kafka-topics.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--delete --topic kafka-connect-status | jq
kafka-topics.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--delete --topic workshop | jq
kafka-topics.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--delete --topic workshop.ecommerce.orders | jq
kafka-topics.sh \
--bootstrap-server $MSK_BOOTSTRAP_ADDRESS \
--command-config /tmp/client_iam.properties \
--delete --topic workshop.ecommerce.product | jq

kafka-topics.sh --bootstrap-server $MSK_BOOTSTRAP_ADDRESS --command-config /tmp/client_iam.properties --list