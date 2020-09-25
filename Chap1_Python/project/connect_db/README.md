# 2. Connect to Database

## 목차
1. psycopg2 설치하기
1. 코드 설명
1. 실행
1. 실습 종료

## psycopg2 설치하기

Docker 를 통해 새로운 환경을 만들었다면 Python 에서 postgresql DB에 연결할 수 있는 기능을 설치해야 한다.

Psycopg 는 가장 많이 쓰이는 PostgreSQL adapter 이다.
```bash
pip install psycopg2-binary
```
⚠️참고: <code>pip install psycopg2</code>로 설치할 경우 의존 패키지를 모두 설치하지 않고 단독 설치 시에는 동작하지 않는다.

## 코드 설명
DB와 연결하기 위해서는 DB 접속 정보를 입력해야 한다.

<code>db_connection_info</code> 라는 변수를 만들어 정보를 저장해 둔다.

연결 설정
```python
# default postgres settings
db_connection_info = {"host": "localhost", "user": "postgres", "dbname": "postgres", "port": 5432}
```
- 위의 값은 postgresql 의 기본 설정이다.

추가 연결 설정 (덮어쓰기)
```python
# TODO: Override connection info
# when postgres runs on docker container
db_connection_info["host"] = "host.docker.internal"
db_connection_info["port"] = 54320
db_connection_info["password"] = 1234
```
- docker를 사용할 경우 [postgres docker의 설정](https://github.com/dreamwayjgs/hyu-database-class-2019/blob/master/postgres/README.md)에 따라 호스트의 54320 에 expose 된 postgres 에 연결하기 위해 <code>host</code> 와 <code>port</code> 값을 지정한다.
- Windows 에서 Postgres를 직접 설치하였을 경우, 설치 과정에서 지정한 <code>user</code>와 <code>password</code>를 지정하면 된다.
- Linux, Mac 에서 Postgres를 설치하였을 경우, 기본값으로 로그인해보고 (상단의 코드를 전부 지우거나 주석 처리), 안될 경우 password 로그인 설정으로 변경한다.
    - [createuser 명령어](https://www.postgresql.org/docs/current/app-createuser.html) 또는 psql 로 접속하여 SQL 쿼리를 통해 새 유저를 생성한다.: [CREATE USER 문 예제 - 구루비](http://www.gurubee.net/lecture/2939)
    - [pg_hba.conf 파일을 변경하여 아이디/패스워드 로그인을 허용한다.](https://stackoverflow.com/questions/4328679/how-to-configure-postgresql-so-it-accepts-loginpassword-auth)


## 실행

```bash
# 입력
python app.py 
# 출력
Connecting To:  host=host.docker.internal user=postgres dbname=postgres password=1234 port=54320
Current database: ('postgres',)
```
