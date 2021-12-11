# vesm3-lokaverkefni

kóðinn sem ég notaði í soilsensor final var gerður með hjálp frá kóða Berinie Chen, **Capacitive Soil Moisture Sensor. Created _2015-10-21_** bernie.chen@dfrobot.com.


skynjarinn sendir data til arduino, arduino sendir annaðhvort þurrt, blautt eða mjög blautt í serial monitor eftir mælingum og raspberry pi les serial monitor. ef það er þurrt byrjar pumpan að dæla vatni, ef það er mjög blautt hættir hún að dæla vatni. raspberry pi sendir líka gögnin til adafruit IO.
