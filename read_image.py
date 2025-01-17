import base64

def Image_convert(path, output):
    with open(path, "rb") as my_image:
        image_string = base64.b64encode(my_image.read()).decode()

    with open(output, "w") as file:
        file.write(image_string)
        
Image_convert("test.jpeg","text_extract.txt")
