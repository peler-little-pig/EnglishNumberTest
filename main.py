import random
import pyttsx3
from num2words import num2words

def fayin(text):
    # 创建对象
    engine = pyttsx3.init()

    # 设置新的语音速率
    engine.setProperty('rate', random.randint(200,230))

    # 获取当前语音声音的详细信息  # 这里我也是找到的实例代码感觉写的很矛盾，最后发出的还是女声
    voices = engine.getProperty('voices')
    engine.setProperty('voice', random.choice(list(voices)))

    # engine.save_to_file(text, filename='go_out.wav', name='test')
    # print('aaa')
    # engine.runAndWait()

    # 将语音文本说出来
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == '__main__':
    print("############################")
    print("English number listening practice tools")
    print("developed by Peler")
    print("copyright Peler 2023 all rights receive")
    print("############################")

    while True:
        a = random.randint(0,99)
        b = random.randint(0,99)
        c = random.randint(0,99)
        d = random.randint(0,99)
        number = a*1000000000+b*1000000+c*1000+d
        # print(number)

        while True:
            s = num2words(number).replace("-"," ")
            print("----------------------------------------------")
            print("spell the number now.")
            fayin(s)
            answer = input("please input your answer here(press Enter to submit): ")
            if answer == str(number):
                print("the answer is right, great!")
                break
            elif answer == "show":
                print("----------------------------------------------")
                print(number)
                print(s)
                input("press Enter to listen again")
            else:
                print("something wrong, please try again.")
