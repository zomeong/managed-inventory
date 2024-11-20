# MARKCLOUD MANAGED-INVENTORY

> Initial written at Nov 20, 2024 <br>

## 1. 프로그램 설명

- 본 프로그램은 ubuntu OS 기준으로 작성되었습니다.
- 본 프로그램은 마크 클라우드 그룹웨어 - 재고 관리 시스템의 백엔드 서버입니다.

## 2. Prerequestie

- 본 프로그램은 Docker 환경 기반으로 구현되어 있습니다.
- `.env` 파일 작성이 필요합니다.

## 3. 구동 방법

1. `.env.template` 파일을 참고하여 `.env` 파일을 작성합니다.

```
API_PORT = 서버 포트 번호
DB_PORT = DB 포트 번호
MARIADB_ID = MariaDB 사용자 이름
MARIADB_PASSWORD = MariaDB 패스워드
DB_NAME = DB 이름
```

2. 도커 컴포즈를 실행합니다.

```shell
(sudo) docker compose up
```
