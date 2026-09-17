# 01_computer_vision_cnn

실습 1 폴더입니다. 이미지를 불러와 numpy 배열로 다루는 기초부터 시작해 CNN까지 단계별로 정리합니다.

가상환경과 패키지는 저장소 루트(`../pyproject.toml`, `../.venv`)에서 관리합니다. 환경 설정 방법은 [루트 README](../README.md)를 참고하세요.

## 폴더 구조

```
01_computer_vision_cnn/
├── data/
│   └── dog.jpg            # 실습용 이미지 (300 x 299, RGB)
├── docs/                  # 과제 문서(.docx), git 제외
├── notebooks/
│   └── 01_practice.ipynb  # 실습 1: 이미지 불러오기, 픽셀 값, 채널 분리
└── utils/
    ├── __init__.py
    └── image_utils.py     # 이미지 표시 등 공용 유틸 함수
```

## 노트북 실행

노트북은 `notebooks/` 아래에 있으므로 데이터 경로는 `../data/dog.jpg`처럼 상위 폴더 기준 상대경로를 사용합니다. `utils` 모듈을 노트북에서 쓰려면 첫 셀에 이 폴더를 경로에 추가합니다.

```python
import sys
sys.path.append("..")   # notebooks/ 의 상위 폴더 = 01_computer_vision_cnn/

from utils.image_utils import show_image
```

## 실습 목록

| 번호 | 노트북 | 내용 |
|---|---|---|
| 1 | `notebooks/01_practice.ipynb` | PIL / OpenCV로 이미지 불러오기, numpy 변환 후 shape·dtype 확인, 특정 픽셀 값 출력, RGB 채널 분리 및 시각화, BGR과 RGB 순서 비교 |

## 참고

- OpenCV(`cv2.imread`)는 채널을 BGR 순서로 읽습니다. matplotlib으로 표시하기 전에 `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`로 변환해야 색이 올바르게 나옵니다.
- numpy 배열은 `[y, x]` 순서로 인덱싱하고, PIL의 `image.size`는 `(너비, 높이)` 순서입니다.
- matplotlib 제목에 한글을 쓰려면 `plt.rc("font", family="AppleGothic")`을 먼저 실행합니다.
