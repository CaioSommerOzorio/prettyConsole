# prettyConsole
Gives complete control of the console to make console applications cleaner and nicer looking.

# DOCUMENTATION 

## draw function

Description: 
The draw function is designed to insert an image represented as a 2D array into a larger canvas or console. The image is positioned on the canvas based on the specified coordinates (x and y). The function iterates over each element of the image array and places it onto the canvas starting from the specified position.

Usage:
Making custom 2d lists look like something can be quite tricky, make a drawing in another file, and open it using `file = open("file.ext", "r").readlines()` then draw it out on the screen using `draw(file, x, y)`.

```python
def draw(img: List, x: Int, y: Int):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] != "\n":
                console[i+y][j+x] = str(img[i][j])
```
 
 
## write function

Description:
The write function can be used to print out any string of text onto the console.

```python
def write(text: String, x: Int, y: Int):
    for i in range(len(text)):
        game_console[y][x+i] = text[i]
```
