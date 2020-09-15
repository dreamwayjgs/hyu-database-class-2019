# 1. Hello, world

## 목차
1. 폴더 구성
1. Python 을 직접 설치한 경우
1. Docker 에 관하여
1. Docker Remote Container 에서 Python 환경 열기
    1. VSCode: Remote-Container 이해하기
        1. devcontainer.json 살펴보기
        1. docker-compose.yml 살펴보기
        1. Remote-Container 실행하기        
1. 실행: Hello, world!

## 폴더 구성

```
1. hello-world
├── docker-compose.yml
├── project
│   ├── app.py
│   ├── requirements.txt
│   └── .vscode
│       └── settings.json
├── python
│   └── .devcontainer
│       └── devcontainer.json
└── README.md
```

앞으로 모든 프로젝트는 이를 기반으로 한 폴더 구조를 따릅니다.

## 직접 설치한 경우

바로 ['실행'](#Run) 파트로 넘어갑니다.

## Docker는 꼭 사용하지 않아도 됩니다

Docker 를 사용하게 되면 다음과 같은 장점이 있습니다.

- 각 프로젝트의 실행 환경이 독립적으로 유지됩니다.
    - 본 저장소의 코드의 실행 환경과 실습자의 실행 환경이 동일함을 보장할 수 있습니다.
- 현재 사용하고 있는 PC의 다른 개발 환경에 영향을 주지 않습니다.

그러나 다음과 같은 단점이 있습니다.

- Docker 의 동작과 실행을 익혀야합니다.
- Windows 환경에서 가상화 기능으로 인해 저사양 환경에서는 사용이 어렵습니다.

따라서 본인이 실습에 집중하고 싶다면 Python 과 Postgresql 을 직접 설치하여 빠르게 진행할 수 있습니다.

그러나 다음과 같은 경우는 Docker 사용을 추천합니다.

- 다른 실습, 개발 등으로 인해 설치되어 있는 환경이 복잡할 때
- 어떤 이유로 구 버전의 Python 을 사용할 때

## Docker Remote Container 에서 Python 환경 열기
### VSCode: Remote-Container 이해하기

기본적인 내용은 [공식 자습서](https://code.visualstudio.com/docs/remote/containers)를 참조하세요.

VSCode의 Remote-Container 기능은 .devcontainer 폴더 내의 devcontainer.json 을 참조하여 Docker 가상 환경과 VSCode 를 연결합니다.

이 과정을 통해 Docker Container 내부 환경에서 동작하는 VSCode를 호스트 PC에서 사용할 수 있습니다. 즉, VSCode의 UX를 그대로 사용하면서 동작 환경은 가상 환경으로 독립되어 실행할 수 있다는 것입니다.


### devcontainer.json 살펴보기
VSCode는 먼저 이 파일을 해석하여, Docker 컨테이너를 새로 만들거나, 기존에 존재하는 컨테이너에 연결하여 호스트 PC와 독립된 환경의 워크스페이스를 엽니다.

```json
"dockerComposeFile": [
    "../../docker-compose.yml"
],
```
- 연결하게 될 Docker container 정보를 담은 docker-compose file 의 위치를 참조합니다.
- docker-compose 에 대해서는 [이 포스트](https://www.44bits.io/ko/post/almost-perfect-development-environment-with-docker-and-docker-compose)를 참조하세요.
```json
"service": "python",
```
- docker-compose 파일 안에 있는 서비스를 참조합니다.
- 여기서의 python 은 docker-compose 내의 services 의 하위 객체로 이름만 같으면 되며 꼭 python 을 치징하는 것은 아닙니다.
```json
"workspaceFolder": "/workspace/project",
```
- docker 컨테이너 내부에서 작업할 위치를 지정합니다.
- docker-compose.yml의 설정에 따라 본 프로젝트의 부모 폴더 (1. hello-world) 는 docker container 내에서 /workspace 와 폴더를 공유하게 됩니다.
```json
"settings": {
    ...
}
```
- 컨테이너 내부에서 VSCode 를 실행할 때, 그 컨테이너에서만 적용할 VSCode 설정입니다.
- 컨테이너 밖 (호스트 PC) 의 설정과 별개로 지정됩니다.
- 현재 Python 관련 설정이 미리 지정되어있습니다.
```json
"extensions": {
    ...
}
```
- 컨테이너 내부에서 VSCode 를 실행할 때, 설치할 VSCode 확장 기능의 ID 입니다.
- 컨테이너가 새로 생성되면 해당 Extension 을 설치하므로 처음 열 때는 시간이 걸릴 수 있습니다.
```json
"postCreateCommand": "pip install -r requirements.txt"
```
- 컨테이너 실행 이후, 컨테이너 내부에서 실행하는 shell 명령어입니다.
- 만약 올바르게 동작하지 않을 경우 해당 명령어를 컨테이너 내부에서 새로 실행해 주세요.

### docker-compose.yml 살펴보기

실제로 docker를 실행하는 설정 파일입니다.

docker-compose.yml 이 존재하는 디렉토리에서 <code>docker-compose up -d</code> 명령어로 실행하며, <code>docker-compose down</code> 명령어로 실행된 컨테이너를 지울 수 있습니다.

단, 이 경우에는 컨테이너는 실행되지만 VSCode 가 수행하는 확장 기능 설치, 설정 적용 등은 진행되지 않습니다.

이렇게 컨테이너를 별도로 실행하고 <code>Remote-Containers: Attach to Running Container</code> 로 환경만 연결할 수도 있습니다.

```yml
services:
```
- 실행할 docker 컨테이너들을 명시합니다.

```yml
python:
```
- 실행할 docker 컨테이너의 이름입니다.
- devcontainer.json 이 참조하게 될 컨테이너의 이름입니다. 자유롭게 이름을 작성할 수 있습니다.
```yml
image: python:3.8
```
- 실행할 컨테이너의 기반이 될 docker 이미지의 이름입니다.
- 저장소를 지정하지 않았으므로 [docker hub](https://hub.docker.com/)의 [python 이미지](https://hub.docker.com/_/python)를 사용하게 됩니다.
```yml
volumes:
    - .:/workspace
```
- 호스트 PC와 공유할 디렉토리를 지정합니다.
- 호스트의 docker-compose.yml 이 있는 현재 위치(.)와 가상 컨테이너의 /workspace 가 같은 파일을 공유하게 됩니다.
```yml
tty: true    
stdin_open: true
```
- <code>docker run</code> 의 <code>-it</code> 옵션과 같습니다.
```yml
ports:
    - "5000:5000"
```
- 호스트 PC(좌측)의 5000 번 포트와 컨테이너의 5000 번 포트를 연결합니다.
- 단, 외부에는 노출되지 안습니다. expose 를 사용해야 합니다.

### Remote-Container 실행하기: 방법 1

VSCode 좌측 하단의 Remote Development 버튼 ![Cap 2020-08-03 13-58-44-757](https://user-images.githubusercontent.com/32762296/89147397-764db600-d591-11ea-9e7e-f0c3c4876e30.png) 을 클릭하고, <code>Open Folder in Container</code> 를 클릭합니다.

파일/폴더 선택 대화상자가 열리면 본 프로젝트 폴더 내의 <code>python</code> 폴더를 선택하고 열기를 누릅니다.

그러면 현재 창이 닫히고 새 창이 열리며, 좌측 하단에 <code>Starting with dev container</code> 의 팝업이 생기며 여러 과정이 수행됩니다.

처음 실행한다면 Python 이미지를 받고 실행하느라 과정이 오래 길 수 있습니다..

실행에 문제가 없다면 좌측하단의 Remote Development 버튼이 아래 그림과 같이 바뀌어 있는 새 창이 실행됩니다.

![Cap 2020-08-03 15-54-58-742](https://user-images.githubusercontent.com/32762296/89154406-c59be280-d5a1-11ea-89c5-ca7d4dbe0d4b.png)

새 창에서 터미널 <code>(Ctrl + Shift + `)</code> 을 실행하고 Python 버전을 확인합니다.

```bash
# 입력
python --version
# 출력 예시
python 3.8.5
```
- 예시 화면
![Cap 2020-08-03 15-57-48-733](https://user-images.githubusercontent.com/32762296/89154578-17dd0380-d5a2-11ea-88dc-d49fb4adef91.png)

### Remote-Container 실행하기: 방법 2 - 별도로 실행하기

자신 환경에 맞는 터미널에서 <code>docker-compose.yml</code> 가 있는 프로젝트 폴더로 이동합니다.

다음 명령어로 직접 docker 컨테이너를 실행합니다.

```bash
docker-compose up -d
```

컨테이너가 잘 실행됐다면 <code>docker ps</code> 명령어로 실행된 컨테이너들을 볼 수 있습니다. 프로젝트상위 폴더명_python_1 형태와 비슷한 컨테이너가 생성된 것을 알 수 있습니다.

VSCode 좌측 하단의 Remote Development 버튼 ![Cap 2020-08-03 13-58-44-757](https://user-images.githubusercontent.com/32762296/89147397-764db600-d591-11ea-9e7e-f0c3c4876e30.png) 을 클릭하고, <code>Attach to running container</code> 를 클릭합니다.

<code>docker ps</code> 명령어로 위에서 알아낸 컨테이너 이름을 골라 클릭하여 연결합니다.


## [실행](#Run)
Python 이 올바르게 설치되어있다면 app.py 를 실행해봅니다.

```bash
# 입력
python app.py
# 출력
Hello world!
```

## 실행 후
실습이 끝나면 VSCode 창을 닫고 호스트 PC에서 각 챕터 디렉토리 (여기서는 1. hello-world) 로 이동하여 모든 컨테이너를 종료해줍니다.

```bash
docker-compose down
```

### 실행이 되지 않을 경우
#### 직접 설치했을 때
- Path 등록을 확인합니다.
    - [Windows에서 Python Path 등록하기](https://wxmin.tistory.com/121)
