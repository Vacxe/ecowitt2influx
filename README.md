## Ecowitt to Influx
### About Ecowitt
![image](https://github.com/user-attachments/assets/77f41c21-beb4-4f1c-ad5d-2bdb2ec1d6c7)

[Ecowitt station](https://www.ecowitt.com/shop/goodsDetail/183) can upload weather data to 3rd party services like Wunderground or Ecowitt. However you may able to send your data to your personal server. One of the must popular timestamp databases is [Influx](https://www.influxdata.com/). This repository contains an tiny server on python which will help you to receive the data from the weather station and proceed in into database. 

### Setup

  #### Station
  * Go to "Settings" -> "Weather Server" -> "Customized"
  * Set your server IP and Port of container (For example `8001`)
  * Interval is up to you. In my case I set it for 15 seconds
  * Leave Path as `/data/report/`
  #### Container
  * pull `vacxe/ecowitt2influx` docker image from the Docker Hub
  * Create new container with port forwarding `8001 -> 80`, or any other port, which will called by your stating from the previous step
  * Go to your Influx instance and provide into container next environment variables
    * INFLUX_URL - url with port for example `10.0.0.10:8086`
    * INFLUX_TOKEN
    * INFLUX_ORG
    * INFLUX_BUCKET
   
  All numerical data which will be recieved from your station will be stored into influx with the default keys and all strings values will be ignored.
  
### Grafana

You may use Grafana dashboad to represend the data from the Influx

<img width="1063" alt="Screen Shot 2025-05-07 at 3 16 06 pm" src="https://github.com/user-attachments/assets/7010fe1d-56c4-4bbb-b847-3fe9db8c748e" />

Dashboad can be found in the repo

