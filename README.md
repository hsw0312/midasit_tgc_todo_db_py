# midasit_tgc_todo_db_py
version python.


## install
```
pip install fastapi
pip install "uvicorn[standard]"
```


## launch

```
uvicorn main:app --reload --host 0.0.0.0

uvicorn "$main위치":app --reload --host 0.0.0.0


example : main이 app 하위에 있을 경우
- uvicorn app.main:app --reload --host 0.0.0.0

```

## Swagger

뒤에 `/docs` 붙이면 됩니다

`http://localhost:8000/docs`