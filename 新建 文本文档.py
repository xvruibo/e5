import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('专注时间结束！')

t = input("输入您想要的专注时间，单位为秒：")
countdown(int(t))
