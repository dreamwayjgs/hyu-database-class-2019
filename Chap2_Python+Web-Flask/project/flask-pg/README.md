# 5. DB Connected web server: Flask and Postgresql 

## 목차

### 폴더 구조
```bash
project/
├── app.py
├── helpers
│   ├── connect_db.py
│   └── student_query.py
├── init_student_table.py
├── requirements.txt
├── static
└── templates
    └── index.html
```

## 데이터베이스 초기화
### Student database
학생을 데이터베이스에 등록하려고 한다. 학생은 다음과 같은 데이터로 나타낸다.
  - ID: 등록된 순서로 매겨지는 순번
  - name: 이름
  - email: 이메일
  - password: 비밀번호

위를 만족하는 데이터베이스를 생성하는 SQL

```sql
CREATE TABLE student (
            id serial primary key,
            name varchar,
            email varchar unique,            
            password varchar
        )
```
- <code>serial</code> 타입으로 id 는 정수형으로 데이터가 들어올 때마다 순차적으로 증가하게 된다.
- 중복되는 <code>email</code> 이 없도록 한다.

### 데이터베이스 생성
```bash
python init_student_table.py
```

## 데이터베이스 연결 Helper 함수들
<code>helper/student_query.py</code>
```python
def insert(name, email, password): ...

def select(): ...
```
- 기본적으로는 <code>example</code> 테이블을 조작하던 지난 자습서의 함수들과 크게 다르지 않다.
- 다만, 기존 <code>select</code> 와 다른 점은 <code>print</code> 로 터미널에 출력하는 것이 아닌 결과물을 반환하는 것이다.
- <code>print(rows)</code> 부분을 통해 실제로 어떤 값이 반환되는지 터미널에서 확인할 수 있다.

## Flask 웹 서버
```python
from helpers.student_query import select, insert
```
- helpers 폴더에 있는 두 함수 <code>select</code>, <code>insert</code> 를 사용할 수 있도록 불러온다.
### DB 데이터 가져오기
```python
@app.route("/")
def index():
    rows = select()
    return render_template("index.html", rows=rows)
```
- <code>select()</code> 를 통해 현재 <code>student</code> 테이블에 저장된 모든 데이터를 받아온다.
- <code>rows=rows</code>: template에 <code>rows</code> 이름으로 전달될 변수 (왼쪽) = <code>select()</code> 리턴 값이 들어간 변수 <code>rows</code> (오른쪽)

```html
<table>
    ...
    <tbody>
        {% for row in rows %}
        <tr>
            <td>{{ row[1] }}</td>
            <td>{{ row[2] }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```
- <code>{% %}</code> 와 <code>{{ }}</code> 는 <code>jinja2</code> 문법으로 각각 Statement 와 Expression 을 의미한다.
- <code>if</code>, <code>for</code> 등의 Statement는 <code>{% %}</code> 의 쌍으로 블록을 구성한다.
- 값을 표현하는 Expression은 <code>{{ }}</code> 안에 변수명이 들어간다.
- 위의 식으로 <code>student</code> 테이블의 결과가 담긴 <code>rows</code>의 값 중, 이름과 이메일에 해당하는 값이 HTML 로 삽입되게 된다.
- 즉, <code>rows</code> 의 길이 만큼 (<code>for</code> 의 수행 횟수) 만큼 &lt;tr&gt;...&lt;/tr&gt; 블록이 반복된다.


### 새로운 데이터 삽입
```python
@app.route("/enroll", methods=["POST"])
def enroll():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    insert(name, email, password)
    return redirect("/")
```
```html
<!-- index.html -->
<form id="form" action="/enroll" method="POST">
...
```
- <code>index.html</code> 의 <code>form</code> 에 입력값을 넣고 <code>submit</code> 이벤트를 발생시키면 ('가입하기' 버튼 클릭) <code>/enroll</code> 에 <code>POST</code> 요청이 전달된다.
- <code>form</code> 에 기입된 값들은 <code>flask</code> 의 <code>request.form</code> 객체에 담겨져 있다. <code>get()</code> 메서드로 [객체의 프로퍼티를 가져온다](https://wikidocs.net/16#key-valueget).
- 이 과정으로 웹 페이지에 입력된 값이 서버를 거쳐 데이터베이스에 저장되게 된다.

## 실행
```python
python app.py
```
- 브라우저에서 localhost:5000 에 접속한다.
- 새로운 학생 값을 임의로 넣어본다.

## 실습 종료
```
docker-compose down
```