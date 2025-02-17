import asyncio
import logging
from collections.abc import Awaitable
from concurrent.futures import Future
from threading import Thread
from typing import Any, Self

from .task_pool_executor import TaskPoolExecutor


class DaemonTaskExecutor:
    def __init__(self, max_active_tasks: int = 2):
        self.max_active_tasks = max_active_tasks

    def __enter__(self) -> Self:
        # Здесь вам необходимо создать поток и запустить его
        # Вы должны создать цикл событий и дать ему старт внутри потока, в который будут отсылаться задачи (корутины)
        # Фоновое выполнение цикла событий будет держать поток в работе
        # Используем также TaskPoolExecutor, ограничивая количество активных задач
        logging.info("DaemonTaskExecutor is starting...")

        ...

        logging.info("DaemonTaskExecutor is started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        # Здесь вам нужно запросить остановку цикла событий. Ну и дождаться остановки потока конечно!
        logging.info("DaemonTaskExecutor is stopping...")

        ...

        logging.info("DaemonTaskExecutor is stopped")

    def submit(self, task: Awaitable[Any]) -> Future[Any]:
        future: Future = self.task_pool_executor.submit(task)
        return future
