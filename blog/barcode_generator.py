import urllib.request


#Функция принимает строчку и создаёт bar-cod изображение в данной директории
def barcode_generator(code:str):
    url = "https://barcode.tec-it.com/barcode.ashx?data=" + code + "&code=Code128&dpi=96&dataseparator="
    return url


