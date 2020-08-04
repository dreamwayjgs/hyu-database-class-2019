# 4. Flask

## 목차

## docker-compose의 포트 개방
docker-compose.yml
```yml
services:
    python:        
        ...
        ports: 
            - "5000:5000"
```
- 호스트의 5000 번 포트와 docker 컨테이너의 5000 번 포트를 연결
- 호스트에서 5000 번 포트에 접속하면 컨테이너의 5000 번 포트로 접속되게 된다.
- 컨테이너에서 5000 번 포트에 개발용 웹 서버를 동작시키고 접속할 때 필요

## Flask 로 웹 서버 만들기
### flask 설치
```bash
pip install flask
```

### flask 기본 폴더 구조
```bash
project/
├── app.py
├── requirements.txt
├── static
└── templates
    └── index.html
```
- <code>app.py</code> : flask 서버가 실행되는 코드를 담음
- <code>templates</code> : flask 서버가 웹 페이지를 반환할 때 템플릿이 되는 웹 페이지들의 기본 위치. HTML 코드와 더불어 <code>jinja2</code> 라는 별개의 템플릿 문법을 사용
- <code>static</code> : 이미지, 아이콘 등 정적인 리소스들이 포함되는 기본 위치

### flask 실행 기본 코드
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```
- <code>app</code> 변수에 Flask 객체를 생성한다.
- <code>@app.route</code> decorator 로 "/" 에 해당하는 HTTP <code>GET</code> 요청이 발생하면 이하의 함수 내용을 실행하게 한다. 또한 그 함수가 반환하는 값을 HTTP 응답으로 처리한다.
- 코드를 이 상태로만 시작하면 웹 브라우저를 켜고 <code>localhost:5000</code> 에 접속했을 때, <code>Hello world</code> 가 출력되는 웹 페이지를 볼 수 있다.
- <code>app.run()</code> 를 호출함으로써 서버가 실제로 시작 된다

### flask template 가져오기
#### clock 페이지
```python
# app.py
@app.route("/clock")
def clock():
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", time=t)
```

```html
<!-- index.html -->
...
<p>Time now: {{ time }}</p>
...
```
- <code>clock()</code> 페이지는 <code>/clock</code> 요청이 들어오면 실행된다.
- <code>datetime.now()</code>: 현재 시각을 담은 <code>Date</code> 객체를 얻는다
- <code>strftime("%Y-%m-%d %H:%M:%S")</code>: <code>Date</code> 객체를 '연-월-일 시:분:초' 포맷을 가진 <code>string</code>  으로 출력한다.
- <code>return render_template("index.html", time=t)</code>
  - <code>templates</code> 폴더에서 <code>index.html</code> 파일을 찾는다.
  - <code>index.html</code> 의 <code>{{ time }}</code> 에 서버에서 처리된 시간 값을 가진 <code>t</code> 를 전달한다.
  - 서버에서 계산된 값이 담겨진 웹페이지가 생성되어 HTTP 응답으로 반환된다.

## 실행
```bash
python app.py
```

웹 페이지에서 <code>localhost:5000</code> 접속

웹 페이지에서 <code>localhost:5000/clock</code> 접속

## 실습 종료
```bash
docker-compose down
```

특히 웹 서버 실습을 한 뒤에는 서버를 닫아야 다른 실습을 할 때 포트 중복으로 인한 컨테이너 생성 불가 에러가 발생하지 않는다.