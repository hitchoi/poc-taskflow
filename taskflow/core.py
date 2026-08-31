"""taskflow — 아주 작은 작업 관리 라이브러리."""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class Task:
    title: str
    priority: int = 1          # 1=낮음 … 5=높음
    due: Optional[datetime] = None
    done: bool = False


class TaskFlow:
    def __init__(self) -> None:
        self._tasks: List[Task] = []

    def add(self, title: str, priority: int = 1, due: Optional[datetime] = None) -> Task:
        task = Task(title=title, priority=priority, due=due)
        self._tasks.append(task)
        return task

    def complete(self, title: str) -> bool:
        for t in self._tasks:
            if t.title == title:
                t.done = True
                return True
        return False

    def list(self, include_done: bool = False) -> List[Task]:
        # include_done=False 이면 완료된 작업은 빠져야 한다.
        tasks = self._tasks if include_done else self._tasks
        return sorted(tasks, key=lambda t: t.priority, reverse=True)
