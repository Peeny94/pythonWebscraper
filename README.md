파이썬 데이터 끌어오기 2번째 프로젝트강의

주요 conda 명령어 정리

conda env list

conda env remove -name 

conda install 패키지

conda list

#파이썬을 위한 가상환경에 대한 명령어
pip install 패키지
pip list


1.만약 conda 명령어가 실행이 되지 않는 경우 환경 변수에 Anaconda를 추가해야 하는 작업이 필요합니다.

쉘 설정파일 열기
nano ~|.zshrc
파일 맨 아래에 추가하기
export Path="경로 입력"

3 . 변경사항을 저장하려면 Ctrl + X를 누르고 Y를 누르고 Enter를 누릅니다.
콘다 실행 확인하기
conda --version 
터미널 열때마다 가상환경 자동 활성화 on/off 기능
conda config --set auto_activate_base false  #off 상태

우선 로컬에 설치된 모든 파이썬의 버전을 확인해보자
ls -l /usr/local/bin/python*