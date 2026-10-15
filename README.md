## IoT-ICA

#SmartWash

Washing your clothes involves more than just putting the clothes in the washing machine. User's must determine when a cycle has finished and decide where to dry their clothes based off the available conditions. In Ireland's climate it may be sunny at 4pm and raining at 4:15. This makes it harder to keep on top of this and it can become easy to leave your clothes outside to dry just for it to rain and make them wet once again.

In comes Smart wash, an IoT-based home clothes-washing management system that monitors washing machine activity and help's users decide how and where to dry their clothes.It will do this by monitoring the washing machine's vibrations and pinging your phone when it has stopped, upon completion it will display some insight into the drying conditions using a local weather API and comparing against the temperature and humidity conditions in the home gathered via sensors. And should it recommend the outdoors, it will give you a guide on the forecast, if you need to bring them in before a certain time as it may rain and possibly a time estimation.

The idea is to have the MPU6050 Accelerometer placed on top of the washing machine to pick up vibrations and post the data to the backend and then to deliver the notification to a FASTAPI PWA.

Alongside the accelerometer, the DHT22 will sit beside it, measuring humidity and temperature to assess the drying conditions and then post the data to the backend where the calculations will happen.

The sensors involved:
* [MPU6050](https://www.mouser.ie/en/ProductDetail/DFRobot/SEN0142?qs=sGAEpiMZZMu3sxpa5v1qrulGv0Cf5EFzMbJVumFAMJA%3D) (Yet to be purchased)
* DHT22 (Purchased)

