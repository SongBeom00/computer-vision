"""실습 환경 확인용 스크립트.

실행: uv run python check_env.py
"""
import platform
import sys

import cv2
import matplotlib
import numpy
import PIL

print("Python     :", sys.version.split()[0])
print("OS         :", platform.platform())
print("numpy      :", numpy.__version__)
print("opencv     :", cv2.__version__)
print("Pillow     :", PIL.__version__)
print("matplotlib :", matplotlib.__version__)
