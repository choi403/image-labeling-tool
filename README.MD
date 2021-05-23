# Image Labeling Tool

## Setup

1.  Python 설치

    - Python 3이 설치되어 있지 않을 경우에만 따라하세요.
    - Windows
      - https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe
      - 이 때 "Add Python 3.9 to PATH"를 체크 (중요함)
      - 맨 아래 있는거
        ![alt text](https://i.imgur.com/1Ro9wDK.png)
    - MacOS
      - https://www.python.org/downloads/ 여기 들어가서 "DOwnload Python 3.9.5 (상단 노란 버튼) 클릭 후 설치
      - 마찬가지로 Add Python 3.9 to PATH 체크

2.  압축 풀기, 라이브러리 설치

    - 압축파일을 풉니다.
    - 폴더에 들어갑니다. 그럼 파일 "requirements.txt", "run.py", "README.MD", "images"가 보여야 하는 상태입니다. (아래 이미지)
      ![alt text](https://i.imgur.com/oyDI5PJ.png)

    - images 폴더를 열고 다음처럼 이미지 파일들을 넣어줍니다.
      ![alt text](https://i.imgur.com/xVt687n.png)

    - 다시 원래 폴더로 나옵니다. (아래 이미지)
      ![alt text](https://i.imgur.com/oyDI5PJ.png)
    - 현재 폴더: 파일 "requirements.txt", "run.py", "README.MD", "images" 폴더가 보여야 함
    - 현재 폴더에서 터미널을 연다.
    - Windows

      - 윈도우 탐색기 주소창을 누름
        ![alt text](https://i.imgur.com/cCr6XSg.png)
      - 이렇게
        ![alt text](https://i.imgur.com/eJIw44I.png)
      - 그 뒤 "cmd"라고 치고 엔터 누름
        ![alt text](https://i.imgur.com/rNSJUN9.png)
      - 그럼 이런 창이 뜹니다.
        ![alt text](https://i.imgur.com/Bicad6O.png)

      - 이렇게 입력하고 엔터 누름

            pip install -r requirements.txt

      - 그럼 뭐라뭐라 뜨고 빨간 텍스트 나면 오류입니다.
      - 빨간 텍스트 안 났으면 이렇게 입력하고 엔터 누릅니다.

            python run.py

      - 그러면 Username: 이라고 나옵니다. 자기 이름 (영문, 아무거나 쳐도됨, 매번 같기만 하면됨 ex) junseok) 입력합니다.
      - 끝

    - MacOS
      - 제가 맥이 없어서 사진이 없습니다.
      - Finder-Services-New Terminal at Folder 클릭
      - Windows와 동일하게 저거 두 줄 입력함

3.  조작법

    - 0, 1, 2, 3, 4: 라벨링 (누르면 다음 사진으로 넘어감)
    - a, d: 이전 사진, 다음 사진
    - q: 종료
