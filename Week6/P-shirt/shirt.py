import sys
from PIL import Image
from PIL import ImageOps



if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

else:
    before_image = sys.argv[1]
    after_image = sys.argv[2]
    if "." in before_image and "." in after_image and before_image.lower().endswith(("jpg", "jpeg", "png")) and after_image.lower().endswith(("jpg", "jpeg", "png")):
        if before_image.split(".")[1] == after_image.split(".")[1]:
            shirt = Image.open("shirt.png")
            size = shirt.size
            image = Image.open(before_image)
            image = ImageOps.fit(image, size)
            image.paste(shirt, shirt)
            image.save(f"{after_image}")
        else:
            sys.exit("Input and Output have different extensions")


    else:
        sys.exit("Invalid input")




