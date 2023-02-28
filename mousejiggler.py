import click
import pyautogui
import time
import random
import math

pyautogui.FAILSAFE = False

@click.command()
@click.option("--distance", default=50, help="Distance of mouse movement (in pixels)")
@click.option("--interval", default=0.5, help="Interval between mouse movements (in seconds)")
@click.option("--speedup-prob", default=0.1, help="Probability of increasing mouse movement speed")
@click.option("--scale", default=20, help="Scaling factor for Gaussian distribution")
def jiggle(distance, interval, speedup_prob, scale):
    """
    Move the mouse cursor in a random pattern with the specified distance and interval indefinitely,
    following a random Gaussian curve with mean 0 and standard deviation 1.
    """
    speedup_factor = 1.0
    distance_factor = 1.0
    duration_factor = 1.0

    while True:
        # Generate random values for x and y offsets following a Gaussian distribution
        x_offset = int(random.gauss(0, 1) * scale * distance_factor)
        y_offset = int(random.gauss(0, 1) * scale * distance_factor)

        # Adjust the distance, duration, and speedup factor based on random factors
        distance_factor = random.uniform(0.8, 1.2)
        duration_factor = random.uniform(0.8, 1.2)
        if random.random() < speedup_prob:
            speedup_factor = random.uniform(1.5, 3.0)
        else:
            speedup_factor = 1.0

        # Move the mouse cursor with the specified x and y offsets and duration
        pyautogui.moveRel(x_offset, y_offset, duration=0.25/speedup_factor*duration_factor)

        # Sleep for the specified interval
        time.sleep(interval)

if __name__ == "__main__":
    jiggle()