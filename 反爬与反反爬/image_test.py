from PIL import Image
import pytesseract

im = Image.open('./1.png')

result = pytesseract.image_to_string(im)

print(result)