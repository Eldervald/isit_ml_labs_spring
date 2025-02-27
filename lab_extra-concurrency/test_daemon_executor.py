import asyncio
import logging
from concurrent.futures import Future
from threading import current_thread
from typing import Any

import numpy as np

from .daemon_executor import DaemonTaskExecutor


async def busy_task(task_id: int):
    logging.info(f"Task {task_id} executing in {current_thread().name}...")
    await asyncio.sleep(2 + np.random.randint(3,5))

    if np.random.rand() < 0.2:
        raise Exception(f"Task {task_id} failed")

    logging.info(f"Task {task_id} successfully finished")
    return "KEK"


def test_daemon_executor():
    ...


if __name__ == "__main__":
    test_daemon_executor()
