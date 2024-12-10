import multiprocessing
import time
from codecs import encode


def process_a(input_queue, output_queue):
    while True:
        message = input_queue.get()
        if message == "STOP":
            break
        time.sleep(5)
        output_queue.put(message.lower())


def process_b(input_queue, output_queue):
    while True:
        message = input_queue.get()
        if message == "STOP":
            break
        result = encode(message, "rot_13")
        print(f"[B]: {result}")
        output_queue.put(result)


if __name__ == "__main__":
    to_a = multiprocessing.Queue()
    from_a = multiprocessing.Queue()
    from_b = multiprocessing.Queue()

    a = multiprocessing.Process(target=process_a, args=(to_a, from_a))
    b = multiprocessing.Process(target=process_b, args=(from_a, from_b))

    a.start()
    b.start()

    while True:
        msg = input("Введите сообщение для A (или STOP для завершения): ")
        to_a.put(msg)
        if msg == "STOP":
            break

    a.join()
    b.join()

    print("Все процессы завершены.")
