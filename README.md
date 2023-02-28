# 😼 Keep your cat busy, with MouseJiggler! 

Are you tired of your cat always distracting you from your work? Do you want to keep your computer active while you're away without risking your screensaver kicking in? Mouse Jiggler is the solution for you!

Mouse Jiggler is a CLI App that moves your mouse cursor in an ever changing random pattern, keeping your computer active and helping to keep your cat entertained for hours. With adjustable parameters for distance, interval, threshold, and even a speedup probability, you can customize the movement of your mouse to fit your needs and maximize your cat's enjoyment.

### ✨ Features

- **Distance**: This parameter controls the maximum distance (in pixels) that the mouse cursor can move in any direction during each movement. Increasing this value will result in larger movements and a wider range of potential cursor locations.
- **Interval**: This parameter controls the duration of the pause (in seconds) between each movement of the mouse cursor. Decreasing this value will result in more frequent cursor movements and a busier mouse cursor.
- **Threshold**: This parameter determines the maximum distance (in pixels) that the mouse cursor can move before the loop is exited. If the cursor moves beyond this distance during a single movement, the loop will exit automatically. This can be used to detect manual movements of the mouse cursor and prevent interference with the automated movement pattern.
- **Speedup probability**: This parameter controls the probability that the mouse cursor will move with a higher speed than usual. When this parameter is set to a value greater than 0, the program will randomly choose a factor between 1.0 and 3.0 to increase the speed of the movement. This can be used to add some variability to the movement pattern and keep your cat more engaged.


### 🛣️ Roadmap

- **cats**: add more cats!.

### 🚀 Installation 

First clone the repository:

```
git clone https://github.com/idrisschebak/mousejiggler
```

Then install the dependencies:

```
pip install -r requirements.txt
```

### 📝 Usage

Run the script from the root of the repository:

```
python mouthjiggler.py
```

To stop it run ```ctrl+c```


Infos :
```
"""
Usage: mousejiggler.py [-h] [-d DISTANCE] [-i INTERVAL] [-t THRESHOLD] [-s SPEEDUP_PROBABILITY]

Move the mouse cursor in a random pattern with the specified distance and interval indefinitely, but break the loop if
the mouse cursor position changes by more than the threshold.

Optional arguments:
  -h, --help            show this help message and exit
  -d DISTANCE, --distance DISTANCE
                        Distance of mouse movement (in pixels)
  -i INTERVAL, --interval INTERVAL
                        Interval between mouse movements (in seconds)
  -t THRESHOLD, --threshold THRESHOLD
                        Threshold for mouse movement detection (in pixels)
  -s SPEEDUP_PROBABILITY, --speedup-probability SPEEDUP_PROBABILITY
                        Probability of increasing mouse movement speed
"""
```

Optionally, you can also change the parameters:
```
python jiggle.py --distance 10 --interval 0.5 --threshold 5 --speedup-prob 0.1
```

# 💡 Reporting Bugs and Contributing

If you encounter any bugs or would like to suggest new features, please create an issue on the GitHub repository. Contributions are also welcome! If you would like to contribute to Kitsec, please create a pull request on the GitHub repository.

# 🚨 Disclaimer

Mouse Jiggler is intended for entertainment purposes only and should not be used for any malicious or illegal activities. Please use responsibly and at your own risk. We are not responsible for any damage caused by over-enthusiastic cats.# 

# 🔖License

This project is licensed under the terms of the MIT license.