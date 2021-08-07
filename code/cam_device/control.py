from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import time

i2c = busio.I2C(SCL,SDA)
pca = PCA9685(i2c)
pca.frequency = 50

servo_row = servo.Servo(pca.channels[7], min_pulse=500,max_pulse=2500)
servo_col = servo.Servo(pca.channels[5], min_pulse=500,max_pulse=2500)

def control_row(angle):
    servo_row.angle = angle
    print('this is row')

def control_col(angle):
    servo_col.angle = angle
    print('this is col')
    #pca.deinit()
#pca.deinit()
#
#60
#40
#servo4.angle = 60
#time.sleep(1)
#50
#108
#166
#control_col(60)