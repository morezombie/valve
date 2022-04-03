import matplotlib.pyplot as plt
import numpy as np
from sympy import *

def sine(degree):
    return np.sin(np.deg2rad(degree))

# 假设行程为-maxDeg度～maxDeg度
def calc(minDeg, maxDeg):
  # 定义deg为角度采样点，步长1度
  deg = np.arange(minDeg, maxDeg + 1)
  # 定义mid为连接杆水平时对应的阀杆行程，单位为百分比
  upper = sine(maxDeg)
  lower = sine(minDeg)
  mid = upper / (upper - lower)
  # 定义r为阀杆到电位计的连接杆长度
  r = mid / sine(maxDeg)
  # 定义valve为阀杆行程，单位为百分比。当阀杆处在最顶端时行程为0,最底端时为1
  valve = 100 * (mid - r * sine(deg))
  # 定义feedback为电位计反馈的位置，单位为百分比
  feedback = 100 * (deg - maxDeg) / (minDeg - maxDeg)
  # 绘制阀杆行程与反馈行程
  plt.title('feedback measurement difference')
  plt.xlabel('degree')
  plt.ylabel('%')
  plt.plot(deg, valve, color='blue', label='valve')
  plt.plot(deg, feedback, color='red', label='feedback')
  plt.axis([minDeg, maxDeg, 0, 100])
  plt.legend(['grating ruler', 'rotate feedback'], loc='upper right')
  plt.grid(True)
  plt.show()
  derive(r, mid, np.deg2rad(minDeg), np.deg2rad(maxDeg))

def derive(r, mid, min, max):
  # 计算极值位置、差异最大值
  x = symbols('x')
  y =  100 * (mid - r * sin(x) - (x - max) / (min - max))
  d = diff(y, x)
  dweller = solve(d, x)
  for di in dweller:
    if (di > np.pi):
        di -= np.pi * 2
    if (di > max or di < min):
        continue
    peak = y.evalf(subs={'x' : di})
    rad = float(di)
    degree = np.rad2deg(rad)
    print('在%f度附近取得极大差异,光栅尺行程高于电位计行程%.2f%%' % (degree, peak))