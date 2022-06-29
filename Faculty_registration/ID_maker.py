from PIL import Image, ImageFont, ImageDraw
import PIL
class IDmaker:
    def __init__(self,data) -> None:
        my_image = Image.open("Faculty_registration/ID.jpg")
        paste_image=Image.open("Faculty_registration/QR.jpeg")
        paste_image=paste_image.resize((1090,1090))
        my_image.paste(paste_image,(500,700))
        title_font = ImageFont.truetype('Faculty_registration/BebasNeue-Regular.ttf',120)
        image_editable = ImageDraw.Draw(my_image)
        image_editable.text((780,2050),data["ID"], (0, 0,0), font=title_font)
        image_editable.text((780,2200),data['name'], (0, 0,0), font=title_font)
        image_editable.text((780,2350),data['Dept'], (0, 0,0), font=title_font)
        image_editable.text((780,2500),data['designation'], (0, 0,0), font=title_font)
        image_editable.text((780,2650),data["phNo"], (0, 0,0), font=title_font)
        my_image.save("Faculty_registration/result.jpg")
data=dict()
data["name"]="V Swathi"
"""
if len lessthan equal to 25 then 120
if len lessthan equal to 30 then 100
formulae if greater than 
"""
data["Dept"]="SalesForce"
data["phNo"]="6304905773"
data["ID"]="788041"
data["designation"]="Jr Software Engineer"
IDmaker(data)