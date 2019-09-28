import RPi.GPIO as GPIO
import time

#port declaration
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.OUT) #this referes to the vertical position
GPIO.setup(19,GPIO.OUT) #this one to the horizontal
p_vertical = GPIO.PWM(21,50)
p_horizontal = GPIO.PWM(19,50)
p_vertical.start(7.5)
p_horizontal.start(7.5)
ldr_left   = 7
ldr_right  = 13
ldr_center = 15
ldr_below  = 16
ldr_above  = 18


#variable declaration
delayt = .1
value_left   = 0
value_right  = 0
value_center = 0
value_below  = 0
value_above  = 0
var_vertical = 7.5
var_horizontal = 7.5

#define of rc_time
def rc_time(ldr, delay):
    count = 0
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, False)
    time.sleep(delay)

    GPIO.setup(ldr, GPIO.IN)

    while (GPIO.input(ldr) == 0):
        count +=1

    return count


try:
    while True:
        value_left = rc_time(ldr_left  ,delayt)
        value_right = rc_time(ldr_right ,delayt)
        value_center = rc_time(ldr_center,delayt)
        value_below = rc_time(ldr_below,delayt)
        value_above = rc_time(ldr_above ,delayt)

        if(value_center * 6 > value_above or value_center * 6 > value_below):
            if(value_above > value_below):

                print("Bajar")
                p_vertical.ChangeDutyCycle(var_vertical)
                var_vertical = var_vertical + 0.2
                time.sleep(0.1)

            else:
                print("Subir")
                p_vertical.ChangeDutyCycle(var_vertical)
                var_vertical = var_vertical - 0.2
                time.sleep(0.1)

        else:
            print("No mover vertical")


        if(value_center * 6 > value_left or value_center * 6 > value_right):
            if(value_left > value_right):

                print("Izquierda")
                p_horizontal.ChangeDutyCycle(var_horizontal)
                var_horizontal = var_horizontal + 0.2
                time.sleep_horizontal(0.1)

            else:
                p_horizontalrint("Derecha")
                p_horizontal.ChangeDutyCycle(var_horizontal)
                var_horizontal = var_horizontal - 0.2
                time.sleep_horizontal(0.1)

        else:
            print("No mover horizontal")

except KeyBoardInterrupt:
    pass
finally:
    GPIO.cleanup()
