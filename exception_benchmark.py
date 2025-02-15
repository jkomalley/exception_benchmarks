# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///
from contextlib import suppress
import timeit

def foo():
    1 / 0

def bench_suppress():
    with suppress(ZeroDivisionError):
            foo()

def bench_tryexcept():
    try:
        foo()
    except ZeroDivisionError:
        pass

def main() -> None:
    runs = 10_000_000
    suppress_time = timeit.Timer("bench_suppress()", globals=globals()).timeit(runs)

    suppress_time_per_execution = suppress_time / runs

    print("Suppress:")
    print(f"Number of executions: {runs}")
    print(f"Total time: {suppress_time} seconds")
    print(f"Time per execution: {suppress_time_per_execution} seconds")

    tryexcept_time = timeit.Timer("bench_suppress()", globals=globals()).timeit(runs)

    tryexcept_time_per_execution = tryexcept_time / runs

    print("Try/Except:")
    print(f"Number of executions: {runs}")
    print(f"Total time: {tryexcept_time} seconds")
    print(f"Time per execution: {tryexcept_time_per_execution} seconds")

    if suppress_time_per_execution < tryexcept_time_per_execution:
         print(f"suppress beat try/except by {tryexcept_time_per_execution - suppress_time_per_execution} seconds")
    else:
         print(f"try/except beat suppress by {suppress_time_per_execution - tryexcept_time_per_execution} seconds")


if __name__ == "__main__":
    main()
