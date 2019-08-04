#include "I2Cdev.h"
#include "MPU6050.h"
#include "ESP_MICRO.h"

#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
    #include "Wire.h"
#endif

MPU6050 accelgyro;

int16_t ax, ay, az;
int16_t gx, gy, gz;

#define OUTPUT_READABLE_ACCELGYRO
#define LED_PIN 13
bool blinkState = false;
int testvariable = 0;

void setup() {
    #if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
        Wire.begin();
    #elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
        Fastwire::setup(400, true);
    #endif

    Serial.begin(38400);

    Serial.println("Initializing I2C devices...");
    accelgyro.initialize();

    Serial.println("Testing device connections...");
    Serial.println(accelgyro.testConnection() ? "MPU6050 connection successful" : "MPU6050 connection failed");
    pinMode(D3, OUTPUT);
    start("Rajput","abhey neelam");
}

void loop() {
  if(ax == 0 || ax == -1)
    digitalWrite(D3,LOW);
  else
    digitalWrite(D3,HIGH);
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
String x = String(ax);
x = x + " ";
x = x + ay;
x = x + " ";
x = x + az;
x = x + " ";
x = x + gx;
x = x + " ";
x = x + gy;
x = x + " ";
x = x + gz;
Serial.println(x);

//    //Waits until a new request from python come
  returnThisStr(x); //Returns the data to python
  waitUntilNewReq();
}
