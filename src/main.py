from fastapi import FastAPI, Response, Request
import os
import json
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import sys

try:
    bucket = os.environ['INFLUX_BUCKET']
    org = os.environ['INFLUX_ORG']
    token = os.environ['INFLUX_TOKEN']
    url = os.environ['INFLUX_URL']
except:
    print(f"Please define: INFLUX_BUCKET, INFLUX_ORG, INFLUX_TOKEN, INFLUX_URL")
    sys.exit()

influx = InfluxDBClient(url=url, token=token, org=org)
write_api = influx.write_api(write_options=SYNCHRONOUS)
app = FastAPI()

@app.post("/data/report/")
async def receive(request: Request):   
    data = json.loads(await request.body())
    points = []
    for key, value in data.items():
        try:
            floatValue = float(value)
            point = Point("ecowitt").field(key, floatValue).time(datetime.utcnow(), WritePrecision.NS)
            points.append(point)
        except:
            None

    write_api.write(bucket=bucket, record=points)
    return Response()