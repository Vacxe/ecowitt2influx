from fastapi import FastAPI, Response, Request
import os
import json
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import sys

try:
    bucket = os.environ['INFLUX_BUCKET']
    print("Bucket: {}".format(bucket))
    org = os.environ['INFLUX_ORG']
    print("Org: {}".format(org))
    token = os.environ['INFLUX_TOKEN']
    print("Token: {}".format(token))
    url = os.environ['INFLUX_URL']
    print("Url: {}".format(url))
except:
    print(f"Please define: INFLUX_BUCKET, INFLUX_ORG, INFLUX_TOKEN, INFLUX_URL")
    sys.exit()

influx = InfluxDBClient(url=url, token=token, org=org)
write_api = influx.write_api(write_options=SYNCHRONOUS)
app = FastAPI()

@app.post("/data/report/")
async def receive(request: Request):
    print("Received data")
    body = await request.body()
    metrics = body.decode("utf-8").split("&")
    points = []
    for metric in metrics:
        try:
            kv = metric.split("=")
            floatValue = float(kv[1])
            point = Point("ecowitt").field(kv[0], floatValue).time(datetime.utcnow(), WritePrecision.NS)
            points.append(point)
        except:
            None

    write_api.write(bucket=bucket, record=points)
    return Response()
