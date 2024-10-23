#!/bin/bash

HOST=http://localhost:8000/api/v1/store

echo "Testing SET  endpoint"
curl -X POST "$HOST/mykey" -H "Content-Type: application/json" -d '{"value": "10"}'
echo $'\n'

echo "Testing GET endpoint"
curl "$HOST/mykey"
echo $'\n'

echo "Testing EXISTS endpoint"
curl "$HOST/mykey/exists"
echo $'\n'

echo "Testing INCREMENT endpoint"
curl -X PUT "$HOST/mykey/increment" -H "Content-Type: application/json" -d '{"increment": 5}'
echo $'\n'

echo "Testing DELETE endpoint"
curl -X DELETE "$HOST/mykey"
echo $'\n'
