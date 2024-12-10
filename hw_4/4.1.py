import time
import threading
import multiprocessing


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def run_sync(n, repeat):
    for _ in range(repeat):
        fibonacci(n)


def run_threads(n, repeat):
    threads = []
    for _ in range(repeat):
        t = threading.Thread(target=fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def run_processes(n, repeat):
    processes = []
    for _ in range(repeat):
        p = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


if __name__ == "__main__":
    n = 35
    repeat = 10

    start = time.time()
    run_sync(n, repeat)
    sync_time = time.time() - start

    start = time.time()
    run_threads(n, repeat)
    thread_time = time.time() - start

    start = time.time()
    run_processes(n, repeat)
    process_time = time.time() - start

    with open("./artifacts/task_4_1_results.txt", "w") as f:
        f.write(f"Синхронный запуск: {sync_time:.2f} секунд\n")
        f.write(f"Запуск с потоками: {thread_time:.2f} секунд\n")
        f.write(f"Запуск с процессами: {process_time:.2f} секунд\n")

    print("Результаты сохранены в task_4_1_results.txt")
