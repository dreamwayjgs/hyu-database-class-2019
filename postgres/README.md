# Postgres Docker container 실행하기

실행하기
```bash
docker-compose up -d
```
- 실행 시 에러가 나는 경우, 우선 포트를 확인해주세요.
- 이미 다른 컨테이너가 실행 중일 경우 해당 컨테이너를 지워주세요.
- 이미 다른 컨테이너가 <code>python-postgres-example</code> 이름을 사용할 경우 <code>docker-compose.yml</code> 의 <code>container_name</code> 을 변경하거나 그 컨테이너를 삭제하여 이름을 확보합니다.
- 호스트의 다른 프로세스가 54320을 실행하고 있을 때, 포트 번호를 변경하거나 해당 프로세스를 중단해주세요.