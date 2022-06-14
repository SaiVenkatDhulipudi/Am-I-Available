from PIL import Image, ImageFont, ImageDraw 
import PIL
class IDmaker:
    def __init__(self,data) -> None:
        my_image = Image.open("Faculty_registration/ID.jpg")
        my_image=my_image.rotate(-90,PIL.Image.NEAREST, expand = 1)
        title_font = ImageFont.truetype('Faculty_registration/BebasNeue-Regular.ttf',120)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((780,2050),data["ID"], (0, 0,0), font=title_font)
        image_editable.text((780,2200),data['name'], (0, 0,0), font=title_font)
        image_editable.text((780,2350),data['Dept'], (0, 0,0), font=title_font)
        image_editable.text((780,2500),data['designation'], (0, 0,0), font=title_font)
        image_editable.text((780,2650),data["phNo"], (0, 0,0), font=title_font)
        my_image.save("Faculty_registration/result.jpg")
data=dict()
data["name"]="Sai Venkat Dhulipudi"
data["Dept"]="CSE"
data["phNo"]="9014038339"
data["ID"]="11234"
data["designation"]="Student"
IDmaker(data)