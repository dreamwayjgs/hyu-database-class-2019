# Lecture 0: 실행 환경 준비

## 목표
1. 실행환경 준비
    1. Docker 설치
    1. VScode 설치
1. postgresql Docker 컨테이너 실행
    1. docker-compose.yml 살펴보기
    1. 실행
1. Python Docker 컨테이너 실행
    1. docker-compose.yml 살펴보기
    1. devcontainer.json 살펴보기
    1. VSCode remote development 살펴보기
    1. 실행
1. Hello, world!

## 들어가기 전에
### Docker를 꼭 사용해야 하나요?
그럴 필요는 없습니다. 다만 이 학습서를 따라하지 않더라도 [Python 3.8](https://www.python.org/downloads/) 과 [Postgresql 12](https://www.postgresql.org/download/) 을 참조하여 자신의 운영체제에 맞는 형태로 설치해두어야 이 저장소가 제공하는 코드를 실행할 수 있습니다.

만약 올바르게 설치가 완료되었다면, 자신의 PC 콘솔 (Windows: cmd, powershell / Linux, MacOS: Terminal) 에서 다음의 코드를 통해 Python 과 Postgresql 이 설치되었고 실행가능한지 확인해봅시다.

#### Python 설치 확인
```bash
# 입력
python --version
# 출력 예시
Python 3.8.5
```
#### Postgresql 설치 확인
```bash
# 입력: Debian, Ubuntu, Centos 7 이상
systemctl status postgresql #또는 postgresql-12
# 출력 예시
● postgresql.service - PostgreSQL RDBMS
   Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
   Active: active (exited) since Mon 2020-04-06 10:21:48 KST; 3 months 24 days ago
 Main PID: 1152 (code=exited, status=0/SUCCESS)
    Tasks: 0
   Memory: 0B
      CPU: 0
```
```bash
# 입력
psql --version
# 출력 예시
psql (PostgreSQL) 12.3 (Debian 12.3-1.pgdg100+1)
```
### VSCode를 꼭 사용해야 하나요?
마찬가지로 그럴 필요는 없습니다. 그러나 Docker를 사용할 경우 VSCode 사용을 매우 추천드립니다.

VScode 없이도 작성한 코드를 Docker 컨테이너 위에서 동작하게 할 수 있으나 코드 에디터가 지원하는 여러 기능 (Linting, Formatting 등)을 지원하지 않을 수 있습니다.

### WSL2 (Windows Subsystem for Linux) 를 꼭 사용해야 하나요?
그렇지 않지만, Windows home 버전에서는 WSL2 를 사용하지 않고 Docker for windows 를 사용할 수 없습니다 (Docker Toolbox 사용 가능). 