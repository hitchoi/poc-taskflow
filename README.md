# taskflow

아주 작은 작업(Task) 관리 라이브러리. 작업을 추가하고, 완료 처리하고, 우선순위 순으로 목록을 본다.

## 사용법

```python
from taskflow import TaskFlow

tf = TaskFlow()
tf.add("코드 리뷰", priority=5)
tf.add("문서 작성", priority=2)

for t in tf.list():          # 우선순위 높은 순
    print(t.priority, t.title)

tf.complete("코드 리뷰")
```

## API

- `add(title, priority=1, due=None)` — 작업 추가 (priority 1=낮음 … 5=높음)
- `complete(title)` — 제목이 일치하는 작업을 완료 처리
- `list(include_done=False)` — 우선순위 높은 순으로 목록 반환. `include_done=False`면 완료 작업 제외

## 테스트

```bash
pip install pytest
PYTHONPATH=. pytest -q
```
