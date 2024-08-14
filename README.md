# BMP Buddy

Edit Bitmap Images with the BMP Buddy Python Program! 

## Table of Contents

- [Installation & Setup](#installation--setup)
    1. [Clone the Repository](#1-clone-the-repository)
    2. [Compile the Program](#2-compile-the-program)
- [Usage](#usage)
    - [Reading](#reading)
        - [Output to Console](#the-output-will-be-displayed-in-the-console)
        - [Output to File](#optionally-you-can-include-a-name-of-a-file-to-place-the-output)
    - [Writing](#writing)
        - [No Output File Specified](#the-output-will-be-placed-in-a-file-named-outputdat-by-default)
        - [Output File Specified](#optionally-a-custom-output-file-name-can-be-included)
- [License](#license)

## Installation & Setup

### 0. Prerequisites
Make sure you have the latest version of the Python installed. You can download it from the [<u>Microsoft store</u>](https://apps.microsoft.com/detail/9ncvdn91xzqp?hl=en-us&gl=US)  
Alternatively, you can install it from the [<u>official site</u>](https://www.python.org/downloads/)

### 1. Clone the Repository
```bash
git clone https://github.com/prebish/bmp-buddy.git
```

### 2. Move to Program Directory
```bash
cd ./bmp-buddy
```

## Usage

### Program Startup
Use the following command within the program directory:
```bash
python editor.py
```

This is the prompt you should get when you first start the program.   
You can use the sample file included in the repository for testing.  

```bash
Enter filename of source image (must be .bmp):
Enter filename of source image (must be .bmp): image.bmp
```

### Editing Options
```bash
==============================
Select Operation:

a) Invert Colors
b) Flip Image
c) Display Color Channel
d) Covert to Grayscale
e) Change Brightness
f) Change Contrast
-------------------------
s) SAVE Picture
o) Open New Image
q) Quit
==============================
(a-f|s|o|q):
```



## License

This project is licensed under the **MIT License** - see the `LICENSE` file for details

