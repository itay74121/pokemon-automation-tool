import pip
from os import system



pip.main(['install','pillow','pytesseract','telegram_send','pywin32','pynput','--user'])
# install tessarect
system("./tesseract-ocr-w64-setup-v5.2.0.20220708.exe")

#prepare bot
system("telegram-send --config")


