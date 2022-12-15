import pytesseract as tes
import cv2
import pybase64
import numpy as np

def textDetection(body):

    image = body["base64"]

    imEncode = image.encode('ascii')
    im64encode = pybase64.b64encode(imEncode)
    im64 = pybase64.b64decode(im64encode)

    imBytes = pybase64.b64decode(im64)

    imArray = np.frombuffer(imBytes, dtype=np.uint8)

    imagem = cv2.imdecode(imArray, flags=cv2.IMREAD_COLOR)
    print(imagem.shape)

    caminho = r"C:\Program Files\Tesseract-OCR"
    tes.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'

    texto = tes.image_to_string(imagem, lang="por")

    print(f'Texto {texto}')

    text = { 'texto': texto }

    return text
