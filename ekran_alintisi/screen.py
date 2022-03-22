import pyautogui

screen = input('Ekran Goruntusu Alinsinmi: y/n : ')

#y veya Y duymesine tiklarsaniz ekran görüntüsünü alip bulunduğunuz dosyaya save edicekdir.
if screen == 'y' or screen == 'Y':
    s = pyautogui.screenshot("ekran_alıntısı.png")
else:
    exit()



