# Requirements Setup: 실행 환경 준비

본 강좌에서 사용하기 위한 개발/실행 환경을 준비합니다.

아래의 Docker Desktop 개발 환경 또는 직접 설치 중 한 가지 환경을 선택하여 따라하고 Python 과 Postgresql 이 실행 가능한 환경을 준비해야합니다.

## 목표
1. 공통
    1. Git 설치
1. Docker Desktop 개발 환경
    1. Docker Desktop 설치
    1. VScode 설치    
    1. postgresql Docker 컨테이너 실행
        1. docker-compose.yml 살펴보기    
    1. Python Docker 컨테이너 실행
        1. docker-compose.yml 살펴보기
        1. devcontainer.json 살펴보기
        1. VSCode remote development 살펴보기            
1. 직접 설치

## 들어가기 전에
### 자신의 사양을 확인해 주세요
Windows 환경에서 Docker는 가상화 기능을 사용합니다. 따라서 가상화 기능을 지원하지 않거나 RAM이 부족한 환경에서는 올바르게 동작하지 않을 수 있습니다.

Docker Desktop 의 [최소 지원 사양](https://docs.docker.com/docker-for-windows/install-windows-home/#system-requirements)을 살펴보세요.

단, RAM은 최소 8GB 이상, 16GB 이상을 권장합니다.

### 최소 사양을 만족하지 못하는 경우

두가지 해결 방법이 있습니다.

1. Linux 환경에서 실행하기
1. Python과 Postgresql 직접 설치하기

### Docker를 꼭 사용해야 하나요?
그럴 필요는 없습니다. 다만 이 학습서를 따라하지 않더라도 [Python 3.8](https://www.python.org/downloads/) 과 [Postgresql 12](https://www.postgresql.org/download/) 을 참조하여 자신의 운영체제에 맞는 형태로 설치해두어야 이 저장소가 제공하는 코드를 실행할 수 있습니다.

### VSCode를 꼭 사용해야 하나요?
마찬가지로 그럴 필요는 없습니다. 그러나 Docker를 사용할 경우 VSCode 사용을 추천드립니다.

VScode 없이도 작성한 코드를 Docker 컨테이너 위에서 동작하게 할 수 있으나 코드 에디터가 지원하는 여러 기능 (Linting, Formatting 등)을 지원하지 않을 수 있습니다.

### WSL2 (Windows Subsystem for Linux) 를 꼭 사용해야 하나요?
그렇지 않지만, Windows home 버전에서는 WSL2 를 사용하지 않고 Docker for windows 를 사용할 수 없습니다 (Docker Toolbox 사용 가능). 

## Docker Desktop 개발 환경

### Docker Desktop 설치와 주의사항

[공식 홈페이지](https://docs.docker.com/desktop/)를 참조하여 자신의 OS에 맞는 형태로 설치합시다.

#### Windows 주의 사항

#### Linux - Docker Engine

배포판 별로 설치 방법이 다를 수 있습니다.

Docker-compose 를 따로 설치해야 할 수 있습니다.

docker 와 docker-compose 모두 설치 후 심볼릭 링크 및 실행 권한(Permission)을 설정해주세요.

특히 non-root user 로 docker를 실행하기 위해서는 아래의 설치 후 작업(post-installation steps)을 반드시 실행해야합니다.

[docker post-installaiton steps](https://docs.docker.com/engine/install/linux-postinstall/)

[docker-compose post-installation steps](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)

## 직접 설치
