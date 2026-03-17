import cv2
import torch
import numpy as np

# 打印 PyTorch 版本，确认深度学习库就绪
print(f"PyTorch Version: {torch.__version__}")

# 调用 Mac 的默认摄像头
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: 无法打开摄像头，请检查 Mac 的隐私权限设置。")
    exit()

print("摄像头已启动！请在弹出的画面窗口中按 'q' 键退出。")

while True:
    # 逐帧读取画面
    ret, frame = cap.read()

    if not ret:
        print("Error: 无法读取画面帧。")
        break

    # 在屏幕上弹窗显示这一帧画面
    cv2.imshow('Robotic Sorting - Camera Test', frame)

    # 监听键盘输入，按 'q' 打破循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源并关闭所有窗口
cap.release()
cv2.destroyAllWindows()
