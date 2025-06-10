#!/bin/bash
set -e

# 1. Start Connect in background
echo "🚀 Starting Kafka Connect distributed..."
connect-distributed /etc/kafka/connect-distributed.properties &
CONNECT_PID=$!

# 2. Wait for REST API
echo "🕓 Waiting for Kafka Connect REST API on http://localhost:8083..."
until curl -s http://localhost:8083/connectors > /dev/null; do
  echo "Still waiting for Connect..."
  sleep 5
done

# 3. Wait for internal topics to be created (configs, offsets, statuses)
echo "⏳ Waiting for internal Kafka topics to be created..."
until curl -s http://localhost:8083/connectors | grep -q '\[\]'; do
  echo "Still initializing Connect (topics not ready yet)..."
  sleep 5
done

# 4. Register connector
echo "📑 Registering Debezium PostgreSQL connector..."
/register-connector.sh

# 5. Wait for Connect process
wait $CONNECT_PID
