# 🎨 Flow Field Art Generator

This project generates stunning flow field art using Perlin noise and custom drawing techniques with PyQt5. The generated images exhibit a variety of colors, patterns, and designs, inspired by the uploaded examples.

## ✨ Features

- 🎨 Dynamic color variations using HSV values
- 🌈 Multiple pattern types generated from Perlin noise
- 🖌️ Customizable transparency and pen width for different visual effects
- 🎲 Randomized seed for unique image generation

## 🛠️ Requirements

- 🐍 Python 3.x
- 📦 PyQt5
- 📦 NumPy

## 🚀 Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/piyushmali/Flow-Field-Art-Generator.git
   cd Flow-Field-Art-Generator
   ```

2. Install the required Python packages:

   ```sh
   pip install PyQt5 numpy
   ```

## 📂 Directory Structure

Ensure your directory structure looks like this:

```
Flow-Field-Art-Generator/
├── draw_script.py
├── utils.py
└── painter.py
```

- `draw_script.py`: Contains the main drawing function.
- `utils.py`: Contains utility functions like `QColor_HSV`, `save`, and `Perlin2D`.
- `painter.py`: Contains the `Painter` class for drawing.

## 🖥️ Usage

To generate flow field art, run the `draw` function with desired parameters:

```python
import random
from draw_script import draw  # Ensure this matches the actual module name

# Example usage with different parameters
draw(
    width=3000,
    height=2000,
    color=random.randint(0, 360),
    backgroundColor=(0, 0, 0),
    perlinFactorW=4,
    perlinFactorH=5,
    step=0.35,
    pattern_type=random.choice([1, 2, 3])
)
```

### Parameters

- `width` (int): Width of the generated image in pixels.
- `height` (int): Height of the generated image in pixels.
- `color` (int): Base hue for the colors (0-360).
- `backgroundColor` (tuple): RGB tuple for the background color.
- `perlinFactorW` (int): Perlin noise factor for width.
- `perlinFactorH` (int): Perlin noise factor for height.
- `step` (float): Step size for drawing lines.
- `pattern_type` (int): Type of pattern to generate (1, 2, or 3).

### Output

The generated image will be saved in the current directory with a filename in the format `image_<seed>.png`.

## 📸 Examples

Here are some example images generated by this script:

![Example 1](examples/image_1.png)
![Example 2](examples/image_2.png)
![Example 3](examples/image_3.png)
![Example 4](examples/image_4.png)
![Example 5](examples/image_5.png)

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

Feel free to make any additional adjustments to suit your needs!
