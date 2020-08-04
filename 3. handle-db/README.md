# 3. Handle database with psycopg2

## 목차
1. 데이터베이스 연결
1. 데이터베이스 읽기
1. 테이블 읽기, 만들기, 지우기
1. 레코드 읽기, 만들기, 갱신하기, 지우기
1. Command line arguments 와 같이 실행하기
1. 실행
1. 실습 종료

이번 장부터는 psycopg2 가 remote-container 연결 시 자동 설치된다.
## 데이터베이스 연결
```python
# connect_db.py
def get_db_connection():
    print("Connecting To: ", db_connection_str)
    conn = pg.connect(db_connection_str)
    return conn
```
- 2장의 데이터베이스 연결 파트를 별도의 함수로 감싸고 <code>connection</code> 객체를 반환하도록 하였다.
- 이 함수는 <code>handle_tables.py</code> 와 <code>handle_rows.py</code> 이 각각 실행될 때 사용된다.

## 데이터베이스 읽기
<code>handle_tables.py</code>

데이터베이스 목록 불러오기
```python
def get_db_list(cur):
    sql = "SELECT datname FROM pg_database"
    cur.execute(sql)
    print("=== DB LIST ===")
    for rows in cur.fetchall():
        print(rows)
```
- 현재 서버에 존재하는 데이터베이스들을 읽어온다.
- <code>CREATE DATABASE</code> 문은 현재 상황에선 작동하지 않는다. 자세한 내용은 [이 링크](https://kb.objectrocket.com/postgresql/create-a-postgresql-database-using-the-psycopg2-python-library-755)를 참조. 본 자습서에서는 DB 목록 불러오기만 실습한다.

## 테이블 읽기, 만들기, 지우기
```python
def get_table_list(cur): ...

def create_table(cur): ...

def drop_table(cur):...
```
- 읽기를 제외하고 데이터베이스가 실제로 변동이 있을 때 (삽입, 갱신, 삭제) <code>conn.commit()</code> 으로 DB에 변동사항을 적용한다.

## 레코드 읽기, 만들기, 갱신하기, 지우기
'example' 테이블에 데이터 레코드 (row, tuple, record) 입력하기
- <code>id</code> 와 <code>name</code> 컬럼을 갖는 <code>example</code> 테이블이 생성되었다고 가정하고, 데이터를 읽고, 쓰고, 갱신하고, 지워보자.

읽기 - SELECT
```python
def select(cur): ...
```

쓰기 - INSERT
```python
def insert(cur): ...

def insert_with_parameters(cur, id, name): ...
```
- 함수 <code>insert</code> 는 지정된 값 (1, 'sample')을 <code>example</code> 에 삽입한다.
- 함수 <code>insert_with_parameters</code> 는 사용자가 입력한 값을 <code>example</code> 에 삽입한다.

Parameterized query
```python
sql = "INSERT INTO example (id, name) VALUES (%s, %s)"
cur.execute(sql, (id, name))
```
- 쿼리 안에 변수를 직접 넣고 싶으면 python 의 [formatted string](https://docs.python.org/ko/3/tutorial/inputoutput.html) 을 사용할 수도 있지만 psycopg 의 parameterized query 를 사용하면 더 간편하고, 타입 적용에 있어서 안전하다.
- [더 많은 예제](https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries)

갱신 - UPDATE
```python
def update(cur): ...

def update_with_parameters(cur, id, name): ...
```

삭제 - DELETE
```python
def delete(cur): ...

def delete_with_parameters(cur, id): ...
```

- 마찬가지로 삽입, 갱신, 삭제에는 <code>conn.commit()</code> 으로 DB에 변동사항을 적용한다.


## Command line arguments 와 같이 실행하기
```python
if len(sys.argv) < 2:
        print("A command argument required.")
        return
    command = sys.argv[1]
```
- <code>main</code> 함수에 각 함수로 연결되는 분기를 만들고 사용자의 입력값에 따라 분기에 진입하도록 하였다.
- <code>import sys</code> 를 통해 <code>sys.argv[]</code> 로 실행 인자(arguments)를 받을 수 있다. 다음과 같다.
```bash
python app.py arg1 arg2
# argv[0] == 'app.py'
# argv[1] == 'arg1'
# argv[2] == 'arg2'
```

## 실행
<code>handle_tables.py</code> 실행하기
```bash
# 데이터베이스 목록 보기
python handle_tables.py dbs
# 테이블 목록 보기
python handle_tables.py tables
# 'example' 테이블 만들기
python handle_tables.py create
# 'example' 테이블 삭제하기
python handle_tables.py drop
```
<code>handle_rows.py</code> 실행하기
```bash
# 'example' 테이블의 데이터 모두 보기
python handle_rows.py select

# 'example' 테이블에 (1, 'sample') 데이터 넣기
python handle_rows.py insert

# 'example' 테이블에 argument로 데이터 넣기. 예제: (2, 'test')
python handle_rows.py insert 2 test

# 'example' 테이블에 id 가 1 인 데이터의 name 을 'updated sample' 로 바꾸기
python handle_rows.py update

# 'example' 테이블에 첫번째 argument를 id로 가진 데이터의 name을 두번째 argument로 업데이트 하기. 예제: (2, 'update_test')
python handle_rows.py update 2 update_test

# 'example' 테이블에 id 가 1 인 데이터를 삭제하기
python handle_rows.py delete

# 'example' 테이블에 첫번째 argument를 id로 가진 데이터를 삭제하기. 예제: 2
python handle_rows.py delete 2
```

## 실습 종료
실습한 컨테이너를 종료하자
```bash
# 각 강좌의 최상위 디렉토리
docker-compose down
```