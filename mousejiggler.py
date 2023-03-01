import click
import pyautogui
import time
import math
import random

pyautogui.FAILSAFE = False

@click.command()
@click.option("--distance", default=30, help="Distance of mouse movement (in pixels)")
@click.option("--interval", default=0.5, help="Interval between mouse movements (in seconds)")
@click.option("--threshold", default=5, help="Threshold for mouse movement detection (in pixels)")
@click.option("--speedup-prob", default=0.1, help="Probability of increasing mouse movement speed")
def jiggle(distance, interval, threshold, speedup_prob):
    """
    Move the mouse cursor in a random pattern with the specified distance and interval indefinitely.
    """
    while True:
        current_position = pyautogui.position()
        x_offset = random.gauss(0, distance)
        y_offset = random.gauss(0, distance)
        if random.random() < speedup_prob:
            speedup_factor = random.uniform(1.0, 3.0)
        else:
            speedup_factor = 1.0
        pyautogui.moveRel(x_offset, y_offset, duration=0.25/speedup_factor)
        time.sleep(interval)
        
        # Check for mouse movement and continue moving the mouse
        new_position = pyautogui.position()
        distance_moved = math.sqrt((new_position[0] - current_position[0])**2 + (new_position[1] - current_position[1])**2)
        if distance_moved > threshold:
            pass

if __name__ == "__main__":
    jiggle()