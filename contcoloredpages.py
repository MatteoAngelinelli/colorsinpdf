import fitz
import os

def has_color(page):
    """
    Check whether a page contains colours other than black in the text and images.
    """
    # Verifica il colore dei blocchi di testo
    blocks = page.get_text("dict")["blocks"]
    for block in blocks:
        if "lines" in block:
            for i in range(len(block["lines"])):
                for span in block["lines"][i]["spans"]:
                    color = span["color"]
                    if color != 0 :
                        return True

    # Checking the colour of images
    images = page.get_images()
    for image in images:
        image_obj = fitz.Pixmap(fitz.open(pdf_path), image[0])
        colorspace = image_obj.colorspace
        if colorspace and colorspace != "DeviceGray":
            return True

    return False

def find_colored_pages(pdf_path):
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF file '{pdf_path}' does not exist.")
    
    colored_pages = []
    with fitz.open(pdf_path) as doc:
        for page_number in range(doc.page_count):
            page = doc.load_page(page_number)
            if has_color(page):
                colored_pages.append(page_number + 1)
    return colored_pages

pdf_path = input("Enter the path of the PDF file: ")
colored_pages = find_colored_pages(pdf_path)
print("Pages with colors:", colored_pages)
print("Number of pages with colors:", len(colored_pages))
