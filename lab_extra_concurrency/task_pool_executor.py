import asyncio
import logging
from collections import namedtuple
from collections.abc import Coroutine
from concurrent.futures import Future
from queue import Queue

QueueItem = namedtuple("QueueItem", ["coroutine", "future"])


class TaskPoolExecutor:
    def __init__(self, loop: asyncio.AbstractEventLoop, max_active_tasks: int = 2):
        self.loop = loop
        self.max_active_tasks = max_active_tasks

    def submit(self, coroutine: Coroutine) -> Future:
        # Планирует выполнение задачи в пуле и возвращает объект Future, ассоциированный с этой задачей
        ...
