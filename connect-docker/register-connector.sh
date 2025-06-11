#!/bin/bash
set -e
#
#echo "Starting Kafka Connect distributed..."
#connect-distributed /etc/kafka/connect-distributed.properties &
#CONNECT_PID=$!

echo "Waiting for Kafka Connect REST API on http://localhost:8083..."
until curl -s http://localhost:8083/connectors > /dev/null; do
  echo "Still waiting for Connect..."
  sleep 5
done

#echo "Waiting for internal Kafka topics to be created..."
#until curl -s http://localhost:8083/connectors | grep -q '\[\]'; do
#  echo "Still initializing Connect (topics not ready yet)..."
#  sleep 5
#done

# 4. Register connector
#!/bin/bash

echo "Rejestruję Debezium PostgreSQL connector..."
curl -X POST http://localhost:8083/connectors \
  -H "Content-Type: application/json" \
  -d '{
    "name": "debezium-postgres-connector",
    "config": {
      "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
      "database.hostname": "postgres",
      "database.port": "5432",
      "database.user": "postgres",
      "database.password": "postgres",
      "database.dbname": "bigdata",
      "database.server.name": "bigdata",
      "plugin.name": "pgoutput",
      "slot.name": "debezium_slot",
      "publication.name": "debezium_publication",
      "snapshot.mode": "initial",
      "key.converter": "io.confluent.connect.avro.AvroConverter",
      "key.converter.schema.registry.url": "http://schema-registry:8081",
      "value.converter": "io.confluent.connect.avro.AvroConverter",
      "value.converter.schema.registry.url": "http://schema-registry:8081"
    }
  }'


# 5. Wait for Connect process
wait $CONNECT_PID
