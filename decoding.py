import pytesseract
from PIL import Image
import time as tm
import os

img_path = 'picture.jpg'


def get_message(img_path):
    img = Image.open(img_path)
    # im_crop = img.crop((850, 50, 1700, 1700))
    # im_crop.save('guido_pillow_crop.jpg', quality=95)
    custom_configs = r'--oem 3 --psm 3'
    tessdata_dir_config = r'--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'
    text = pytesseract.image_to_string(img, lang='rus', config=custom_configs)
    return text


def get_text(img_path):
    img = Image.open(img_path)
    im_crop = img.crop((840, 200, 1700, 950))
    im_crop.save('decode_pict/guido_pillow_crop.jpg', quality=95)
    x1 = 0
    y1 = 0
    n = 1
    for i in range(10):
        for j in range(5):
            current_word = im_crop.crop((x1, y1, x1 + 170, y1 + 75))
            current_word.save(f'decode_pict/{n}.jpg')
            x1 += 170
            n += 1
        x1 = 0
        y1 += 75


def get_key_picture():
    key = []
    for i in range(1, 50):
        file = f'decode_pict/{i}.jpg'
        text = get_message(file)
        # print(text)
        # print(i)
        if 'ОТПРАВЛЕНО:' in text:
            for j in range(2):
                i += 1
                file = f'decode_pict/{i}.jpg'
                text = get_message(file)
                # print(text)
                key.append(text[0:-2])
                key_final = ' '.join(key)
                # print(text)
    return key_final


def decode():
    data = []
    with open('result.txt', 'r') as file:
        for line in file:
            data.append(line)
    # print(data)

    text = open("decoded.txt")
    uncode = text.read()

    uncode = uncode.split()
    text.close()

    # print(uncode)

    def decode_key(data):
        full_key = str(data)
        # print(type(full_key))
        str_key = full_key[23:42]
        # print(str_key)
        t = tm.strptime(str_key, '%Y-%m-%d %H:%M:%S')
        # print(t)
        unix_time = tm.mktime(t)
        key = "".join(str(int(unix_time)))
        key = key * 10
        print(key)
        return (key)

    key = decode_key(data[1])
    print(key)

    # Читаем файл с секретным сообщением
    message = open("result.txt")
    mes = message.read()
    message.close()
    mes = mes.split()

    print(mes)

    # Читаем файл с секретным сообщением

    def shifr(key, uncode, mes):
        for z in range(0, 1):

            try:
                sep = ' '
                x = int()
                q = int(0)
                count = int(0)
                for i in range(0, 100):

                    p = int(key[i])
                    # print("p=", p)
                    if i == 0:
                        x = int(key[i])
                    else:
                        if p == q:
                            x = x + 1
                            print("Здесь х=0")
                        else:
                            x = x + int(key[i])
                            # print(mes[x])
                    uncode[i] = mes[x] + sep
                    count = count + 1

                    if mes[x] == '!':
                        print(uncode[0:count])
                        # print(count)
                        print("Читать закончил")
                        break

                    else:
                        pass
                        # print(uncode[0:count])


            # file.writelines(key)

            except IndexError:
                print('Error')
                print(uncode)

        print('ЗАПИСЫВАЮ ДЕШИФРОВКУ')
        with open('uncoded.txt', 'w') as file:
            file.writelines(uncode[0:count])
            print(count)

    shifr(key, uncode, mes)


decode()

if __name__ == '__main__':
    clear_file()
    decode()
