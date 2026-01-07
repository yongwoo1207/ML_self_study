
"""
title : 손실함수 실습
생성자 : 임용우
생성일 : 26.01.06
최종수정일 : 26.01.07
"""

# 패키지 import 
import numpy as np

#1. mse 구현
def mse(y_t, y_p):
  return np.mean((y_t - y_p)**2)

#2. RMSE 구현
def rmse(y_t, y_f):
  return mse(y_t, y_f) ** (1/2)

def main():
  y_t = np.array([1, 2, 3])
  y_p = np.array([1, 2, 10])
  print("mse 실습 결과 :", mse(y_t, y_p))
  print("RMSE 실습 결과 :", rmse(y_t, y_p))
  return 0

if __name__ == '__main__':
  main()


