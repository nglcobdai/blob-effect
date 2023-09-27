# blob-effect

## 1. Clone & Prepare .env

```
git clone XXX
```

## 2. Create .env

- copy .env.example to .env

```bash
cp .env.example .env
```

## 3. Docker Build & Run

```sh
docker-compose build --no-cache
docker-compose up -d
docker-compose exec project bash
```
