from PIL import Image
import matplotlib.pyplot as plt

def show_image(image_path: str, figsize: tuple[float, float]=(8, 6)) -> None:
  """
  PIL과 matplotlib를 사용하여 이미지를 표시하는 함수입니다.
  :param image:
  :return:
  """
  image = Image.open(image_path)
  plt.figure(figsize=figsize)
  plt.imshow(image)
  plt.axis('off')
  plt.show()

