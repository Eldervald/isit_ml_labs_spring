# Конкурентность, параллельность, многопоточность, многозадачность и прочие страшные заклинания

## Материалы для изучения
В этой лабе вы столкнётесь с параллельностью, многопоточностью и асинхронным программированием. Если впервые столкнулись с асинхронным программированием, то вам предстоит немного изучить его. Полезные материалы:
- [Асинхронный python без головной боли (часть 1)](https://habr.com/ru/articles/667630/)
- [Асинхронный python без головной боли (часть 2)](https://habr.com/ru/articles/671798/)
- [Асинхронный python без головной боли (часть 3)](https://habr.com/ru/articles/774582/)
- Оффициальная документация по модулям `concurrent.futures` и `asyncio` из стандартной библиотеки Python.

## О задаче
Задание предполагает последовательное решение 3 подзадач:
1. Реализовать класс `TaskPoolExecutor`, который будет ограничивать количество одновременно выполняемых корутин. Его поведение должно быть аналогичным по сути поведению классов `ThreadPoolExecutor` и `ProcessPoolExecutor` из стандартной библиотеки Python. Смотрите на комментарии и тайпинги в исходниках. 
    - Имейте ввиду, что класс `TaskPoolExecutor` должен поддерживать выполнение корутин в других потоках, а не только в текущем.
    - Не забываем обрабатывать исключения.
2. Реализовать класс `DaemonTaskExecutor`, который будет выполнять корутины в отдельном потоке. Помимо этого он должен использовать класс `TaskPoolExecutor` для ограничения количества одновременно выполняемых корутин.
    - Класс должен быть [контекстным менеджером](https://book.pythontips.com/en/latest/context_managers.html). Внутри него должен быть запущен отдельный поток, в котором будут выполняться корутины. При выходе из контекстного менеджера поток должен быть остановлен.
3. Написать тест, используя в качестве вводных корутину `busy_task`. В рамках выполнения теста вы должны отправить в `DaemonTaskExecutor` (c ограничением в 3 одновременно выполняемых корутины) 10 корутин `busy_task` и проверить, что они выполняются в отдельном потоке. Futures ожидаем последовательно в порядке выполнения. 
    - Для наглядности конкурентного исполнения кода ожидайте результат `Future` с таймаутом в 1 секунду. Если прошла 1 секунда, выводим лог (ожидаем результат такой-то задачи из потока такого-то) и повторяем проверку, пока не получим результат или исключение. Воспользуйтесь документацией для `concurrent.futures.Future`. Функцию `sleep` из модуля `time` не использовать. 
    - Не забываем обрабатывать исключения.
    - DaemonTaskExecutor - контекстный менеджер, поэтому должен быть вызван в блоке `with` и должен быть закрыт при выходе из блока. 
- Подсказка: все импорты прописаны в исходниках не просто так.

## Примерный вывод правильного решения

```
concurrency_lab/test_daemon_executor.py::test_daemon_executor 
-------------------------------- live log call --------------------------------
13:22:25 [    INFO] DaemonTaskExecutor is starting...
13:22:25 [   DEBUG] Using proactor: IocpProactor
13:22:25 [    INFO] DaemonTaskExecutor is started
13:22:25 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 1.
13:22:25 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 2.
13:22:25 [    INFO] Task 0 executing in DaemonThread...
13:22:25 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 3.
13:22:25 [    INFO] Task 1 executing in DaemonThread...
13:22:25 [    INFO] Task 2 executing in DaemonThread...
13:22:26 [    INFO] Waiting for task 0 from MainThread
13:22:27 [    INFO] Waiting for task 0 from MainThread
13:22:28 [    INFO] Waiting for task 0 from MainThread
13:22:29 [    INFO] Waiting for task 0 from MainThread
13:22:30 [    INFO] Task 2 successfully finished
13:22:30 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 3.
13:22:30 [    INFO] Task 3 executing in DaemonThread...
13:22:30 [    INFO] Waiting for task 0 from MainThread
13:22:31 [    INFO] Task 1 successfully finished
13:22:31 [    INFO] Task 0 successfully finished
13:22:31 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 3.
13:22:31 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 3.
13:22:31 [    INFO] Result of task 0: KEK
13:22:31 [    INFO] Result of task 1: KEK
13:22:31 [    INFO] Task 4 executing in DaemonThread...
13:22:31 [    INFO] Result of task 2: KEK
13:22:31 [    INFO] Task 5 executing in DaemonThread...
13:22:32 [    INFO] Waiting for task 3 from MainThread
13:22:33 [    INFO] Waiting for task 3 from MainThread
13:22:34 [    INFO] Waiting for task 3 from MainThread
13:22:35 [    INFO] Task 3 successfully finished
13:22:35 [    INFO] Waiting for task 3 from MainThread
13:22:35 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 3.
13:22:35 [    INFO] Result of task 3: KEK
13:22:35 [    INFO] Task 6 executing in DaemonThread...
13:22:36 [    INFO] Waiting for task 4 from MainThread
13:22:37 [    INFO] Task 5 successfully finished
13:22:37 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 3.
13:22:37 [CRITICAL] Task 4 failed
13:22:37 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 3.
13:22:37 [    INFO] Result of task 5: KEK
13:22:37 [    INFO] Task 7 executing in DaemonThread...
13:22:37 [    INFO] Task 8 executing in DaemonThread...
13:22:38 [    INFO] Waiting for task 6 from MainThread
13:22:39 [    INFO] Waiting for task 6 from MainThread
13:22:40 [    INFO] Waiting for task 6 from MainThread
13:22:41 [    INFO] Waiting for task 6 from MainThread
13:22:41 [    INFO] Task 6 successfully finished
13:22:41 [   DEBUG] TASK POOL: Sending task to execute. Number of active tasks: 3.
13:22:41 [    INFO] Result of task 6: KEK
13:22:41 [    INFO] Task 9 executing in DaemonThread...
13:22:42 [    INFO] Task 7 successfully finished
13:22:42 [    INFO] Result of task 7: KEK
13:22:43 [    INFO] Task 8 successfully finished
13:22:43 [    INFO] Result of task 8: KEK
13:22:44 [    INFO] Waiting for task 9 from MainThread
13:22:45 [    INFO] Waiting for task 9 from MainThread
13:22:46 [    INFO] Waiting for task 9 from MainThread
13:22:46 [    INFO] Task 9 successfully finished
13:22:46 [    INFO] Result of task 9: KEK
13:22:46 [    INFO] DaemonTaskExecutor is stopping...
13:22:46 [    INFO] DaemonTaskExecutor is stopped
PASSED                                                                   [100%]

============================= 1 passed in 21.28s ==============================
Finished running tests!
```