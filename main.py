# Make grid
cols, rows = 120, 36
console = [[" "] * cols for _ in range(rows)]

# Prints out img in any part of the console
def add_img(img, x, y):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if img[i][j] != "\n":
                console[i+y][j+x] = img[i][j]

# Same as add_img but adds text instead, singular loop because it's a string not a list of strings
def add_text(text, x, y):
    for i in range(len(text)):
        console[y][x+i] = text[i]
