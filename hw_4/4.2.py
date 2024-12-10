import math
import time
import logging
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os

logging.basicConfig(filename="./artifacts/task_4_2_logs.txt", level=logging.INFO, format="%(asctime)s - %(message)s")


def integrate_part(f, a, b, n_iter):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_type="thread"):
    step = (b - a) / n_jobs
    ranges = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]

    if executor_type == "thread":
        executor_class = ThreadPoolExecutor
    else:
        executor_class = ProcessPoolExecutor

    start_time = time.time()
    with executor_class(max_workers=n_jobs) as executor:
        futures = []
        for r in ranges:
            logging.info(f"Запуск задачи для диапазона {r} с {executor_type}")
            futures.append(executor.submit(integrate_part, f, r[0], r[1], n_iter // n_jobs))
        results = [f.result() for f in futures]
    total_time = time.time() - start_time

    return sum(results), total_time


if __name__ == "__main__":
    a = 0
    b = math.pi / 2
    n_iter = 10000000
    cpu_num = os.cpu_count()

    results = []

    for n_jobs in range(1, cpu_num * 2 + 1):
        for executor_type in ["thread", "process"]:
            result, exec_time = integrate(math.cos, a, b, n_jobs=n_jobs, n_iter=n_iter, executor_type=executor_type)
            results.append(f"{executor_type}: n_jobs={n_jobs}, time={exec_time:.2f} сек")
            print(f"{executor_type}: n_jobs={n_jobs}, time={exec_time:.2f} сек")

    with open("./artifacts/task_4_2_results.txt", "w") as f:
        f.write("\n".join(results))
