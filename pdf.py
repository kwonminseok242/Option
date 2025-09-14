from PIL import Image
import os

# 스크린샷이 들어있는 폴더 경로
img_dir = "/Users/kwonminseok/Desktop/2025y/9m/KT Cloud Basic/Part2_KT Cloud/2-1 Kt Cloud 선택의 이유"

# PNG 파일만 가져오기
files = [os.path.join(img_dir, f) for f in os.listdir(img_dir) if f.endswith(".png")]

# 생성시간 순으로 정렬
files.sort(key=lambda x: os.path.getmtime(x))

# 이미지 열어서 PDF로 저장
images = [Image.open(f).convert("RGB") for f in files]
if images:
    output_path = os.path.join(img_dir, "output.pdf")  # 같은 폴더에 저장
    images[0].save(output_path, save_all=True, append_images=images[1:])
    print(f"PDF 저장 완료: {output_path}")
