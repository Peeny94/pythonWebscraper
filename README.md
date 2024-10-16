파이썬 데이터 끌어오기 2번째 프로젝트강의

주요 conda 명령어 정리

conda env list

conda env remove -name 

conda install 패키지

conda list

#파이썬을 위한 가상환경에 대한 명령어
pip install 패키지
pip list

# 맥에 깔린 파이썬 확인 및 정리하기
ls -l /usr/local/bin/python*
# sudo 를 붙여서 강제로 삭제가능, 비밀번호 입력 필요함.
sudo rm {삭제할 파이썬 명 입력<- 날짜 다음부터 '->' 나오기 전까지 전부 입력할 것, 띄어쓰기로 삭제할 파일 경로포함 해서 복수 삭제 가능하다.}

# 기본 환경변수 설정필요.(터미널 창에 아래를 순서대로 입력하기)
export PATH=%PATH:/bin:/usr/local/bin:/usr/bin
echo $PATH  
vim ~/.zshrc
    1. 환경변수 필요한 거 입력하기
    2. esc 누르고 :eq     
source ~/.zshrc 
    
<!-- 
    저장된 환경변수
    # 3.9.13 python env setting
    alias python=python3
    export PATH="/Library/Frameworks/Python.framework/Versions/3.9/bin"
    # PATH - path지정을 안 해주면 .zshrc 자체를 들어갈 수 없다.
    export PATH=%PATH:/bin:/usr/local/bin:/usr/bin
-->

## 기본 맥 환경변수 설정하기
i — vim 편집기에서 i를 눌러 insert 모드로 진입
export 환경변수명=환경변수값 — 환경변수 입력
ESC 키 — ESC 키를 눌러 insert모드 종료
:q    // 종료
:w    // 저장
:wq   // 저장 후 종료
:q!   // 저장하지 않고 종료
:wq!  // 강제로 저장 후 종료

source ~/.zshrc — 환경변수 등록
echo $환경변수명 — 환경변수 등록 확인


