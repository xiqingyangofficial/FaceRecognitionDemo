import cv2

# 基本参数
flag = 1
id = 1
max = 50000

# 导入摄像头
try:
    cap_video = cv2.VideoCapture(0)
except:
    print("摄像头存在问题，请检查后重新执行程序")
    exit()

# 姓名读取
name = []
for i in range(max):
    name.append(0)
print("请输入将要读取的对象的姓名：")
name[id] = input()

# 姓名检测
def name_detect():
    if name[id] == 0:
        print("请输入新人的姓名：")
        name[id] = input()

# 图片读取
while cap_video.isOpened():
    ret_value, video_input = cap_video.read()
    cv2.imshow(f"Now:{id}, Press S to Save, B to back, N to continue, Q to quit", video_input)
    key = cv2.waitKey(1)
    if key == ord('s'):
        if cv2.imwrite("./dataset/" + str(id) + "_" + str(name[id]) + ".jpg", video_input):
            print("当前对象图片采集成功")
        else:
            print("当前对象图片无法保存，请检查程序权限")
    elif key == ord('n'):
        if id + 1 < max:
            id = id + 1
            cv2.destroyAllWindows()
            name_detect()
            continue
        else:
            print("当前已达到可存储数据的上限，请联系管理员修改上限")
    elif key == ord('b'):
        if id - 1 > 0:
            id = id - 1
            cv2.destroyAllWindows()
            name_detect()
            continue
        else:
            print("已是第一个人脸数据")
    elif key == ord('q'):
        break
    else:
        continue

# 释放摄像头与内存
cap_video.release()
cv2.destroyAllWindows()


