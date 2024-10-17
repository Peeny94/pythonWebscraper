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
    /Library/Frameworks/Python.framework/Versions/3.9/Resources/Python.app
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

# 웹스크래퍼는 순수 파이썬만 사용하므로 기본 제공되는 Venv 사용, 향후 다른 프로젝트에서는 아나콘다를 활용해 보자.
gyoungminlee@Gyoungminui-MacBookAir pythonWebscraper % python -m venv webScraper
gyoungminlee@Gyoungminui-MacBookAir pythonWebscraper % source webScraper/bin/activate 
deactivate
가상환경 삭제 : sudo rm -rf 가상환경이름

패키지 버전 관리 
pip freeze > requirements.txt 명령으로 현재 환경의 패키지 목록을 저장
pip install -r requirements.txt 다른 환경에서 명령으로 동일한 환경을 구축가능
pip uninstall -r requirements.txt 전부 삭제

모듈 설치 후 깃 push 오류를 위해 용량을 늘려줌, .gitignore 파일도 만들어줌.(사이트 사용)
git config --global http.postBuffer 524288000    

