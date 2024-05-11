import time

from PIL import Image
import pytesseract

def extract_text_from_jpeg(jpeg_path):
    """Use OCR to extract text from a JPEG image."""
    # Load the image from the file path
    image = Image.open(jpeg_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image, lang="eng")  # Specify language codes if you need to recognize multiple or specific languages

    return text

def main():
    # Path to your JPEG image
    jpeg_path = "data/IMG_2988.jpg"
    
    # Extract text
    start = time.time()
    for i in range(100):
        text = extract_text_from_jpeg(jpeg_path)
    print(f"Time elapsed: {time.time()-start}")
    print("Extracted Text:")
    print(text)

if __name__ == "__main__":
    main()
