import sys
import random
import cv2


# 영상 불러오기
src = cv2.imread('namecard1.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

# 입력 영상을 그레이스케일 영상으로 변환
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 자동 이진화
_, src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 외곽선 검출 및 명함 검출
contours, _ = cv2.findContours(src_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 이진 영상을 컬러 영상 형식으로 변환
dst = cv2.cvtColor(src_bin, cv2.COLOR_GRAY2BGR)

# 검출된 외곽선 모두 그리기
for i in range(len(contours)):
    c = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    cv2.drawContours(dst, contours, i, c, 2)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
