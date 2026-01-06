"""
title : 손실함수 실습
생성자 : 임용우
생성일 : 26.01.06
최종수정일 : 26.01.06
"""
#1. mse 구현
import numpy as np

def mse(y_t, y_p):
  return np.mean((y_t - y_p)**2)

y_t = np.array([1, 2, 3])
y_p = np.array([1, 2, 4])
print(mse(y_t, y_p))

