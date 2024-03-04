import cv2
import pytesseract
import pathlib
from multiprocessing import Pool
import time

filename = "data/large-receipt-image-dataset-SRD"
path = pathlib.Path(filename)
files = list(path.rglob("*"))
files = [str(file) for file in files if ".jpg" in file.name]


def scrape_text(file):

    image = cv2.imread(file)

    return pytesseract.image_to_string(image)

if __name__ == "__main__":
        start = time.time()
        cores_pool = Pool(10)
        cores_pool.map(scrape_text, files)
        cores_pool.close()
        end = time.time()
        print(end - start)