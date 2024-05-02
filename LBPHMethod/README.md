# 基于LBPH的人脸识别实现

## 简介

本部分是《人脸识别系统的设计与实现》项目的Demo1，基于Harr级联检测器实现

## 结构

- main.py 程序菜单
- get_data.py 已有人脸数据采集
- load.py 加载已有人脸数据
- detect.py 新人脸识别
- images文件夹 存储采集的人脸照片
  - 序号_姓名.jpg 格式

- features文件夹 存储采集的人脸特征
  - harr.yaml 特征
  - name.txt 姓名

- classifier文件夹 存储OpenCV训练好的级联器模型

## 原理

1. 采集人脸信息模块

   - 采集已有人脸数据集

     - 调用摄像头拍摄

     - 按格式存储图片

   - 加载已有人脸数据集
     - Harr级联分类器人脸检测
     - LBPH人脸识别

2. 识别人脸信息模块

   - 加载检测和识别模型并识别
   - 将姓名锚框打印在图像上


## 使用

1. 环境配置
   - Python + requirements.txt
2. 运行main.py

​		





​			
