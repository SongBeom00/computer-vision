# computer_vision

컴퓨터비전 수업 실습 프로젝트입니다. 실습 단위별로 하위 폴더를 나누고, 가상환경과 의존성은 저장소 루트에서 하나로 관리합니다.

## 실습 환경

| 구분 | 내용 |
|---|---|
| Python | 3.11 (`.python-version`) |
| 패키지 관리 | [uv](https://docs.astral.sh/uv/) + `pyproject.toml` / `uv.lock` |
| IDE | PyCharm (인터프리터: 루트의 `.venv`) |
| 주요 라이브러리 | numpy, opencv-python, matplotlib, Pillow, ipykernel, pytest |

## 폴더 구조

```
computer_vision/
├── .python-version            # 3.11
├── pyproject.toml             # 의존성 목록 (모든 실습 공용)
├── uv.lock                    # 설치 버전 잠금 파일
├── .venv/                     # uv가 만든 가상환경 (git 제외)
├── check_env.py               # 설치된 라이브러리 버전 확인 스크립트
└── 01_computer_vision_cnn/    # 실습 : 이미지 기초 → CNN
```

새 실습은 `02_xxx/` 처럼 번호를 붙인 폴더로 추가합니다. 패키지는 루트 `pyproject.toml`에 한 번만 설치하면 모든 실습 폴더에서 같은 `.venv`를 사용합니다.

| 번호 | 폴더 | 내용 | 참조 |
|:---:|---|---|:---:|
| 1 | `01_computer_vision_cnn/` | 이미지 불러오기, numpy 변환, 픽셀 값과 RGB 채널 분리, CNN 기초 구현 | [코드 보기](https://github.com/SongBeom00/computer-vision/tree/main/01_computer_vision_cnn) |