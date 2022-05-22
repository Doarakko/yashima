import time
import pygame.mixer
import RPi.GPIO as GPIO

SENSOR_PIN = 18
MUSIC_PATH = "sample.mp3"


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SENSOR_PIN, GPIO.IN)

    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC_PATH)

    print("setup is successful")


def loop():
    while True:
        if GPIO.input(SENSOR_PIN) == GPIO.HIGH:
            print("status: on")

            if not pygame.mixer.music.get_busy():
                channel = pygame.mixer.music.play(1)
                print("action: start")
        else:
            print("status: off")

        time.sleep(2)
        print()


def destroy():
    GPIO.cleanup()

    pygame.mixer.quit()

    print("destroy is successful")


if __name__ == "__main__":
    setup()

    try:
        loop()
    except KeyboardInterrupt:
        destroy()
