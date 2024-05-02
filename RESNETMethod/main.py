# coding=utf-8

import os
import datetime
from pytz import timezone
import time

# 基本参数设置
app_name = "人脸识别系统"
app_version = "demo2"
app_developer = "人脸识别系统开发小组"
app_update_time = "2024.5.2"
app_quote = "永远相信美好的事情即将发生"
app_user = ("亲爱的同学")
app_hello = ("你好")
app_goodbye = ("期待您的再次使用")
app_say_hello = app_user + app_hello
app_say_goodbye = app_user + app_goodbye
cli_width = 100 - len(app_name)

# 时间参数设置
shanghai_tz = timezone('Asia/Shanghai')
current_beijing_time = datetime.datetime.now(shanghai_tz)
current_beijing_time = current_beijing_time.strftime('%Y-%m-%d %H:%M:%S')

# 功能跳转
def func_choice():
    choice = input()
    if choice == '1':
        os.system("python get_data.py")
        main_menu()
        return
    elif choice == '2':
        os.system("python detect.py")
        main_menu()
        return
    elif choice == 'q':
        print(f"{app_say_goodbye}")
        return
    else:
        print("输入有误，请重新输入")
        main_menu()
        return

# 菜单函数定义
def lead_in_menu():
    for i in range(cli_width):
        if i != cli_width - 1:
            print("-", end="")
        else:
            print('-')
    print(str.center(f"{app_say_hello},最近过得还好吗~无论生活怎样，请相信一切都会变好哒~", cli_width))
    print(str.center(f"现在是北京时间{current_beijing_time}", cli_width))
    print(str.center(f"欢迎您使用{app_name}!!!", cli_width))
    print(str.center(f"本软件由{app_developer}开发，期待您提出宝贵的改进意见", cli_width))
    print(str.center(f"当前版本号为：{app_version}, 最后一次更新于：{app_update_time}", cli_width))
    for i in range(cli_width):
        if i != cli_width - 1:
            print("-", end="")
        else:
            print('-')
    time.sleep(2)
    print(str.center("* * * * * * Now Loading * * * * * *", cli_width))
    for i in range(cli_width):
        if i != cli_width - 1:
            print("-", end="")
        else:
            print('-')



def main_menu():
    print(str.center(f"===人脸识别基础功能==", cli_width))
    print(str.center(f"1.录入人脸数据", cli_width))
    print(str.center(f"2.识别人脸信息", cli_width))
    print(str.center(f"===人脸识别拓展功能==", cli_width))
    print(str.center(f"  404 NOT FOUND", cli_width))
    print(f"请输入您需要的功能对应的序号（输入q以退出程序）：")
    for i in range(cli_width):
        if i != cli_width - 1:
            print("-", end="")
        else:
            print('-')
    func_choice()



# 程序流程
path = os.getcwd()
os.chdir(path)
lead_in_menu()
time.sleep(5)
main_menu()