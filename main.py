from PIL import Image, ImageFile, ImageEnhance
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

#loops through all files in the directory of where my pictures are stored
for f in os.listdir('/Volumes/Drone/DCIM/100MEDIA'):
    if f.endswith ('.JPG') and not(f.startswith('._')): #ignores the unusable files
        image = Image.open("/Volumes/Drone/DCIM/100MEDIA/" + f)
        color_enhancer = ImageEnhance.Color(image)
        sharp_enhancer = ImageEnhance.Sharpness(image)
        enhanced_image = color_enhancer.enhance(1.6)
        more_enhanced_image = sharp_enhancer.enhance(5)
        #more_enhanced_image.show()
        more_enhanced_image.save("/Volumes/Drone/DCIM/100MEDIA/ENHANCED_" + f)