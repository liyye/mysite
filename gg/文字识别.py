from PIL import Image
import pytesseract
img = Image.open('code1.jpg')
print(img)
text = pytesseract.image_to_string(Image.open('code1.jpg'),lang='chi_sim')
print(text)
print(type(text))