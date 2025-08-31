import pytesseract
from PIL import Image

# ✅ Set the full path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load and process image
image = Image.open("quote1.png")
text = pytesseract.image_to_string(image)

# Display the extracted text
print(text)
