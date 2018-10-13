#!/usr/bin/env python
# -*- coding:utf-8 -*-
import qrcode
import base64
import hashlib


def make_qrcode(text):
    image = qrcode.make(text)
    image.save('qrcode.png')
    image.get_image().show()
    print("你的二维码已保存为qrcode.png")


def sha256_convert(text):
    sha256 = hashlib.sha256()
    sha256.update(text)
    print(sha256.hexdigest())


def base64_encode(text):
    stri = base64.b64encode(text)
    print(bytes.decode(stri))


def base64_decode(text):
    stri = base64.b64decode(text)
    print(bytes.decode(stri))

while True:
    choose = input("输入1实现sha256加密，2实现base64加解密，3实现字符串生成二维码，4退出：")

    if choose == "3":
        text = input("请输入文本：")
        make_qrcode(text)
        continue

    if choose == "1":
        text = input("请输入文本：")
        text1 = text.encode("utf-8")
        sha256_convert(text1)
        continue

    if choose == "2":
        while True:
            choose1 = input("解码输入1，编码输入2：")

            if choose1 == "1":
                while True:
                        s = input("请输入base64码，或输入4退出：")
                        try:
                            if s == "4":
                                break
                            else:
                                text = str.encode(s)
                                base64_decode(text)
                        except:
                            print("输入非base64码，请确认后重新输入。")
                            continue
                        else:
                            break
                break

            if choose1 =="2":
                s = input("请输入文本：")
                text = str.encode(s)
                base64_encode(text)
                break
            else:
                print("您的输入不正确，请输入指定数字。")
        continue

    if choose == "4":
        print("谢谢使用！")
        break

    else:
        print("您的输入不正确，请输入指定数字。")
        continue
