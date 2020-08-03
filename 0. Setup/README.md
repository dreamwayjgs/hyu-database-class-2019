# Requirements Setup: 실행 환경 준비

본 강좌에서 사용하기 위한 개발/실행 환경을 준비합니다.

아래의 Docker Desktop 개발 환경 또는 직접 설치 중 한 가지 환경을 선택하여 따라하고 Python 과 Postgresql 이 실행 가능한 환경을 준비해야합니다.

## 목표
1. 들어가기 전에    
1. Docker Desktop 개발 환경
    1. Docker Desktop 설치
    1. VScode 설치     
1. 직접 설치

## 들어가기 전에
### 자신의 사양을 확인해 주세요
Windows 환경에서 Docker는 가상화 기능을 사용합니다. 따라서 가상화 기능을 지원하지 않거나 RAM이 부족한 환경에서는 올바르게 동작하지 않을 수 있습니다.

Docker Desktop 의 [최소 지원 사양](https://docs.docker.com/docker-for-windows/install-windows-home/#system-requirements)을 살펴보세요.

단, RAM은 최소 8GB 이상, 16GB 이상을 권장합니다.

### 최소 사양을 만족하지 못하는 경우

두가지 해결 방법이 있습니다.

1. Linux 환경에서 실행하기: 개발 전용 PC를 구축할 수 있을 때
1. Python과 Postgresql 직접 설치하기: 윈도우를 꼭 사용해야할 떄

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

Windows Home 의 경우 WSL2 가 필수적입니다.

[해당 자습서](https://docs.docker.com/docker-for-windows/wsl/)를 통해 WSL2 활성화와 드라이버 설치 등을 수행해주세요.

#### Linux - Docker Engine

배포판 별로 설치 방법이 다를 수 있습니다.

Docker-compose 를 따로 설치해야 할 수 있습니다.

docker 와 docker-compose 모두 설치 후 심볼릭 링크 및 실행 권한(Permission)을 설정해주세요.

특히 non-root user 로 docker를 실행하기 위해서는 아래의 설치 후 작업(post-installation steps)을 반드시 실행해야합니다.

- [docker post-installaiton steps](https://docs.docker.com/engine/install/linux-postinstall/)
- [docker-compose post-installation steps](https://docs.docker.com/compose/install/#install-compose-on-linux-systems)

여기까지 완료하면 자신 환경의 명령줄 인터페이스(이하 터미널)로 docker 동작을 확인합니다.

```bash
# 입력
docker --version
# 출력 예시
Docker version 19.03.12, build 48a66213fe
```

## VS Code 설치

[공식 홈페이지](https://code.visualstudio.com/)에서 자신의 환경에 맞게 설치합니다.

또한, [Remote Development Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)을 설치합니다. [자습서도 참조](https://code.visualstudio.com/docs/remote/remote-overview)하세요.

참고: 각 플랫폼 별 터미널 
  - Windows: cmd, powershell, [windows terminal](https://www.microsoft.com/ko-kr/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab), git bash
  - Linux: bash, dash, zsh ...
  - MacOS: iTerminal

[VSCode + WSL2 + Docker 자습서](https://code.visualstudio.com/blogs/2020/07/01/containers-wsl)

여기까지 완료하면 VSCode를 실행하였을 때 좌측 하단에 다음 사진과 같은 Remote Development 아이콘이 추가되고, 누르면 여러 옵션이 나타나게 됩니다.

#### Remote Development Icon 
![Cap 2020-08-03 13-58-44-757](https://user-images.githubusercontent.com/32762296/89147397-764db600-d591-11ea-9e7e-f0c3c4876e30.png)

#### Remote Development Dropdown
![Cap 2020-08-03 14-00-09-815](https://user-images.githubusercontent.com/32762296/89147464-ad23cc00-d591-11ea-92ef-2e09b031d3ff.png)



## 직접 설치

2019 데이터베이스 시스템 수업 관련 [재생 목록](https://www.youtube.com/channel/UC-BfZXnoOCOF9FxNrbubR0w/videos)을 참조하실 수 있습니다.

  1. [Python 설치, VSCode 설치](https://www.youtube.com/watch?v=dhszWSXRfWo)
  1. Postgresql 설치 [1편](https://www.youtube.com/watch?v=V_22GkBc_ss), [2편](https://www.youtube.com/watch?v=uFup6zQG2tE)
     - ERWin 설치는 생략 바랍니다.