from concurrent.futures import ThreadPoolExecutor, as_completed
import math
import random


TASKS = 20
THREAD_POOL = 8


def math_calculation():
    for i in range(random.randint(10000000, 30000000)):
        final_sqrt = math.sqrt(i)
    return final_sqrt


def main():
    # Create process pool
    pool = ThreadPoolExecutor(max_workers=THREAD_POOL)
    futures = []

    # Submit work to process pool
    for _ in range(TASKS):
        futures.append(pool.submit(math_calculation))

    # Show results as the work completes
    for task_result in as_completed(futures):
        print(task_result.result())


if __name__ == "__main__":
    main()
