import threading
import math
from time import sleep


class ProgressBar:
    def __init__(self,
                 capacity: int,
                 start_sym: str = "[",
                 full_sym: str = "=",
                 empty_sym: str = " ",
                 load_loop: list[str] = ["|", "/", "-", "\\"],
                 end_sym: str = "]",
                 bar_length: int = 10,
                 tick_rate: int = 2):
        # not (directly) from params
        self.curr_value: int = 0
        self.num_full_syms: int = 0
        self.num_empty_syms: int = bar_length - 1
        self.progress: float = 0
        self.tick_count: int = 0

        # from params
        self.capacity: int = capacity
        self.start_sym: str = start_sym
        self.full_sym: str = full_sym
        self.empty_sym: str = empty_sym
        self.load_loop: list[str] = load_loop
        self.end_sym: str = end_sym
        self.length: int = bar_length
        self.tick_rate: int = tick_rate  # in Hz

    def increment_progress(self) -> None:
        self.update_progress(self.curr_value + 1)

    def update_progress(self, new_value: int) -> None:
        self.curr_value = new_value
        self.progress = new_value / self.capacity
        self.num_full_syms = math.floor(self.progress * self.length) if new_value < self.capacity else self.length
        self.num_empty_syms = self.length - self.num_full_syms - 1

    def __str__(self) -> str:
        return self.start_sym + (self.num_full_syms * self.full_sym) \
            + (self.load_loop[self.curr_value % len(self.load_loop)] if self.curr_value < self.capacity else "") \
            + (self.num_empty_syms * self.empty_sym) + self.end_sym

    def demo(self) -> None:
        print("\033[?25l", end="")
        for _ in range(self.capacity):
            print(f"{self}\033[1A")
            self.increment_progress()
            sleep(0.5)

        print(self)
        print("\033[?25h", end="")


def main() -> None:
    bar: ProgressBar = ProgressBar(40)
    bar.demo()

    bar2 = ProgressBar(40, start_sym="<", full_sym="-", end_sym=">", load_loop=[".", ",", "*", "o", "O", "@"])
    bar2.demo()

    bar3 = ProgressBar(40, bar_length=30)
    bar3.demo()


if __name__ == "__main__":
    main()

