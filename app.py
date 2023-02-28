import streamlit as st
import pyautogui
import time
import random
import os
os.environ['DISPLAY'] = ':0'
import math

pyautogui.FAILSAFE = False

def jiggle(distance, interval, speedup_prob, scale, duration):
    """
    Move the mouse cursor in a random pattern with the specified distance and interval for the specified duration,
    following a random Gaussian curve with mean 0 and standard deviation 1.
    """
    speedup_factor = 1.0
    distance_factor = 1.0
    duration_factor = 1.0
    end_time = time.time() + duration

    while time.time() < end_time:
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

# Set up the Streamlit app
st.title(" 🐭 Mouse Jiggler")
st.write("Move the mouse cursor in a random pattern with the specified distance and interval.")

# Add collapsible section for the options
with st.expander("Options"):
    distance = st.slider("Distance of mouse movement (in pixels)", min_value=10, max_value=100, value=50, step=10)
    interval = st.slider("Interval between mouse movements (in seconds)", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    speedup_prob = st.slider("Probability of increasing mouse movement speed", min_value=0.0, max_value=1.0, value=0.1, step=0.1)
    scale = st.slider("Scaling factor for Gaussian distribution", min_value=10, max_value=30, value=20, step=5)

# Add textbox for the duration option
duration = st.text_input("Duration of mouse jiggling (in seconds)", value="60")

# Center the "Start Jiggling" button
jiggler_button = st.button("Start Jiggling!", key="jiggler_button")
jiggler_button_container = st.container()
with jiggler_button_container:
    st.write(" ")
if jiggler_button:
    jiggle(distance, interval, speedup_prob, scale, int(duration))
st.markdown("</div>", unsafe_allow_html=True)

if jiggler_button:
    jiggle(distance, interval, speedup_prob, scale, int(duration))
