import bmp

#========= GLOBAL VARS =============#
# Pixel
r = 0; g = 1; b = 2

# Formatting Strings
brdr = (30*"=" + "\n")
dsh  = (25*"-")
ln   = "\n"

# Sub Menu Strings
flip_title  = "Flip Image Options"
brite_title = "Brightness Options"
con_title   = "Contrast Options"
chan_title  = "Channel Options"

op_h = "[h] Horizontal"
op_v = "[v] Vertical"
op_q = "[q] Back"

op_plus  = "[+] Increase"
op_minus = "[-] Decrease"

op_r = "[r] Red"
op_g = "[g] Green"
op_b = "[b] Blue"
#===================================#

class ImageProcesser():

    def __init__(self, filename):
        self.newName = "alt_" + filename
        self.pixelgrid = bmp.ReadBMP(filename)
        self.height = len(self.pixelgrid)
        self.width = len(self.pixelgrid[0])
        
    def save(self, newName): bmp.WriteBMP(self.pixelgrid, newName)

    def invert(self):
        for row in range(self.height):
            for col in range(self.width):
                pixel = self.pixelgrid[row][col]
                pixel[r] = 255 - pixel[r]
                pixel[g] = 255 - pixel[g]
                pixel[b] = 255 - pixel[b]

    def displayChannel(self, channel):
        for row in range(self.height):
            for col in range(self.width):
                pixel = self.pixelgrid[row][col]
                if (channel == "r"): pixel[g] = 0; pixel[b] = 0
                if (channel == "g"): pixel[r] = 0; pixel[b] = 0
                if (channel == "b"): pixel[r] = 0; pixel[g] = 0
    
    def flip(self, axis):
        pixel = self.pixelgrid

        if (axis == "v"): self.pixelgrid = self.pixelgrid[::-1]
        if (axis == "h"):
            for row in range(self.height):
                pixel[row] = pixel[row][::-1]

    def grayscale(self):
        for row in range(self.height):
            for col in range(self.width):
                pixel = self.pixelgrid[row][col]
                gray = (pixel[r]+pixel[g]+pixel[b])//3
                pixel[r] = gray; pixel[g] = gray; pixel[b] = gray

    def brightness(self, op):

        for row in range(self.height):
            for col in range(self.width):
                pixel = self.pixelgrid[row][col]

                if op == "+":
                    # Red Increment
                    if ((pixel[r]+25) <= 255): pixel[r] = pixel[r]+25
                    else: pixel[r] = pixel[r]+(255-pixel[r])
                    # Green Increment
                    if ((pixel[g]+25) <= 255): pixel[g] = pixel[g]+25
                    else: pixel[g] = pixel[g]+(255-pixel[g])
                    # Blue Increment
                    if ((pixel[b]+25) <= 255): pixel[b] = pixel[b]+25
                    else: pixel[b] = pixel[b]+(255-pixel[b]) 

                if op == "-":
                    # Red Decrement
                    if ((pixel[r]-25) >= 0): pixel[r] = pixel[r]-25
                    else: pixel[r] = 0
                    # Green Decrement
                    if ((pixel[g]-25) >= 0): pixel[g] = pixel[g]-25
                    else: pixel[g] = 0
                    # Blue Decrement
                    if ((pixel[b]-25) >= 0): pixel[b] = pixel[b]-25
                    else: pixel[b] = 0

    def contrast(self, conChoice):

        for row in range(self.height):
            for col in range(self.width):
                pixel = self.pixelgrid[row][col]

                if conChoice == "+":
                    C = 45
                    factor = (259*(C+255))/(255*(259-C))

                    # Red
                    newPixel = int(factor*(pixel[r] - 128) + 128)
                    if (newPixel < 255 and newPixel > 0): pixel[r] = newPixel
                    else:
                        if(newPixel > 255): pixel[r] = 255
                        if(newPixel < 0): pixel[r] = 0
                    # Green
                    newPixel = int(factor*(pixel[g] - 128) + 128)
                    if (newPixel < 255 and newPixel > 0): pixel[g] = newPixel
                    else:
                        if(newPixel > 255): pixel[r] = 255
                        if(newPixel < 0): pixel[r] = 0
                    # Blue
                    newPixel = int(factor*(pixel[b] - 128) + 128)
                    if (newPixel < 255 and newPixel > 0): pixel[b] = newPixel
                    else:
                        if(newPixel > 255): pixel[r] = 255
                        if(newPixel < 0): pixel[r] = 0 

                if conChoice == "-":
                    C = -45
                    factor = (259*(C+255))/(255*(259-C))

                    # Red
                    newPixel = int(factor*(pixel[r] - 128) + 128)
                    if (newPixel < 255 and newPixel > 0): pixel[r] = newPixel
                    else:
                        if(newPixel > 255): pixel[r] = 255
                        if(newPixel < 0): pixel[r] = 0
                    # Green
                    newPixel = int(factor*(pixel[g] - 128) + 128)
                    if (newPixel < 255 and newPixel > 0): pixel[g] = newPixel
                    else:
                        if(newPixel > 255): pixel[r] = 255
                        if(newPixel < 0): pixel[r] = 0
                    # Blue
                    newPixel = int(factor*(pixel[b] - 128) + 128)
                    if (newPixel < 255 and newPixel > 0): pixel[b] = newPixel
                    else:
                        if(newPixel > 255): pixel[r] = 255
                        if(newPixel < 0): pixel[r] = 0

def mainMenuStrings():
    print(f"{brdr}Python Image Processor{ln}{brdr}Select Operation:{ln}")
    print(f"a) Invert Colors{ln}b) Flip Image{ln}c) Display Color Channel{ln}d) Covert to Grayscale{ln}e) Change Brightness{ln}f) Change Contrast{ln}{dsh}")
    print(f"s) SAVE Picture{ln}o) Open New Image{ln}q) Quit{ln}{brdr}", end="")

def subMenuStrings(title, *args):
    print(f"{brdr}{title}{ln}{brdr}Select Operation:{ln}")
    print(*args, sep=f"{ln}")

def flipMenu(photo):
    subMenuStrings(flip_title, op_h, op_v)
    flipChoice = input("(h|v|q): ")
    if (flipChoice == "q"): mainMenu(photo)

    # Flip Choice
    if (flipChoice in ["h","v"]): photo.flip(flipChoice)
    mainMenu(photo)

def channelMenu(photo):
    subMenuStrings(chan_title, op_r, op_g, op_b, op_q)
    chanChoice = input("(r|g|b|q): ")
    if (chanChoice == "q"): mainMenu(photo)

    # Channel Choice
    if (chanChoice in ["r", "g", "b"]): photo.displayChannel(chanChoice)
    mainMenu(photo)

def brightMenu(photo):
    subMenuStrings(brite_title, op_plus, op_minus)
    brightChoice = input("(+|-|q): ")
    if (brightChoice == "q"): mainMenu(photo)

    # Inc or Dec Brightness
    if (brightChoice in ["+", "-"]): photo.brightness(brightChoice)
    brightMenu(photo)

def contrastMenu(photo):
    subMenuStrings(con_title, op_plus, op_minus, op_q)
    conChoice = input("(+|-|q): ")
    if (conChoice == "q"): mainMenu(photo)

    # Inc or Dec Contrast
    if (conChoice in ["+", "-"]): photo.contrast(conChoice)
    contrastMenu(photo)

def mainMenu(photo):
    mainMenuStrings() 
    op = input("(a-f|s|o|q): ")

    # OPERATIONS
    if (op == "q"): exit()                        # Quit
    elif (op == "a"): photo.invert()              # Invert
    elif (op == "b"): flipMenu(photo)             # Flip
    elif (op == "c"): channelMenu(photo)          # Channel
    elif (op == "d"): photo.grayscale()           # Grayscale
    elif (op == "e"): brightMenu(photo)           # Brightness
    elif (op == "f"): contrastMenu(photo)         # Contrast
    elif (op == "s"): photo.save(photo.newName)   # Save
    elif (op == "o"): main()                      # Open New

    mainMenu(photo)
        
def main():
    filename = input("Enter filename of source image (must be .bmp): ")
    photo = ImageProcesser(filename)
    mainMenu(photo)

# Start of Program
main()