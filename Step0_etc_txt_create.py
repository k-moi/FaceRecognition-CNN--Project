################################################################
## 해당 파일은 haarcascades 알고리즘으로 얼굴을 촬영하고 저장하였을 때,
## 각 이미지 파일 이름에 맞추어 txt 파일을 생성합니다.
################################################################

import os
import glob

## 이미지 파일이 있는 경로
folder_path = './my_face/images'

## YOLO 형식의 annotation (class, x, y, w, h)



## 이미지 파일 확장자 목록
img_extensions = ['.jpg', '.jpeg', '.png']

## 이미지 파일 목록 생성
img_files = []
for ext in img_extensions :
    img_files.extend( glob.glob(os.path.join(folder_path, f'*{ext}')) )
    
## 이미지 파일별로 동일한 이름의 txt 파일 생성
for img_file in img_files :
    ## 이미지 파일 이름에서 확장자를 제거하고 .txt 확장자로 변환
    txt_file = os.path.splitext(img_file)[0] + '.txt'
    
    ## 이미지 파일 이름에서 클래스를 추출(13~18 중 하나)
    ## 파일명 앞의 두 글자에 따라 클래스를 구분
    ## gh 13, jh 14, js 15, mj 16, sw 17, yc 18
    class_num = 0
    if 'gh' in os.path.basename(img_file) :
        class_num = 13
    elif 'jh' in os.path.basename(img_file) :
        class_num = 14
    elif 'js' in os.path.basename(img_file) :
        class_num = 15
    elif 'mj' in os.path.basename(img_file) :
        class_num = 16
    elif 'sw' in os.path.basename(img_file) :
        class_num = 17
    elif 'yc' in os.path.basename(img_file) :
        class_num = 18
    else :
        print('해당하는 클래스가 없습니다.')
        continue
    
    annotation = f'{class_num} 0.5 0.5 1 1'
    
    ## 해당 txt 파일에 YOLO annotation 내용 작성
    with open(txt_file, 'w') as f :
        f.write(annotation + '\n')
        
    print(f'{txt_file} 파일 생성 완료')
print('모든 txt 파일이 생성되었습니다.')