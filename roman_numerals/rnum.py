import sys
import re
import argparse


CHARSET: dict[int, str] = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

VAL_MAP = dict(zip(CHARSET.values(), CHARSET.keys()))

def int_to_rnum(num: int) -> str:
    rnum = ""

    while num > 0:
        for k in reversed(CHARSET):
            if num % k == 0:
                rnum += CHARSET[k]
                num -= k
                break
            elif num > k:
                rnum += CHARSET[k]
                num -= k
                break
            else:
                break_after_loop = False

                for diff in [10**i for i in range(2,-1,-1)]:
                    if k > diff and num > diff and num % (k - diff) <= diff - 1:
                        rnum += CHARSET[diff] + CHARSET[k]
                        num -= (k - diff)
                        break_after_loop = True
                        break
                
                if break_after_loop:
                    break

    return rnum


def rnum_to_int(rnum: str) -> int:
    num = 0
    prev_val = None

    for idx, char in enumerate(rnum):
        val = VAL_MAP[char]

        if prev_val != None and prev_val < val:
            val -= 2 * prev_val

        num += val
        prev_val = val
    
    return num


def int_to_rnum_range(nums: list[int], ranges: list[int]) -> None:
    idx = 0

    for low, high in zip(nums, ranges):
        for i in range(low, high + 1):
            print(f"{i} = {int_to_rnum(i)}")

        if low > high:
            print(f"ERROR: empty range: {low} > {high}" \
                   "\n                    ^   ^" \
                   "\n                    |   |" \
                   "\n          lower bound   upper bound")

        done = (idx == len(nums) - 1) or (idx == len(ranges) - 1)
        if not done:
            print()

        idx += 1

    for num in ranges[len(nums):]:
        print()
        print(f"ERROR: unpaired range with upper bound {num}")

    for num in nums[len(ranges):]:
        print()
        print(f"{num} = {int_to_rnum(num)}")


def cli_loop() -> None:
    num_regex = r"([1-9][0-9]*)"
    range_regex = f"^{num_regex}-{num_regex}$"

    num_pattern = re.compile(num_regex)
    range_pattern = re.compile(range_regex)

    cmd = input("rnum > ")
    while cmd != "exit" and cmd != "quit":
        num_match = num_pattern.fullmatch(cmd)
        range_match = range_pattern.fullmatch(cmd)

        if range_match:
            (low_bound, up_bound) = range_match.group(1,2)
            int_to_rnum_range([int(low_bound)], [int(up_bound)])
        elif num_match:
            num = int(num_match.group(1))
            int_to_rnum_range([num], [num])
        elif cmd == None or cmd == "" or cmd.isspace():
            pass
        else:
            print("Usage: NUM[-UPPER_BOUND]" \
                "\nNUM:\t\t positive int" \
                "\nUPPER_BOUND:\t positive int" \
                "\nex: 5-10" \
                "\nex: 3" \
                "\nexit or quit will end cli session\n")

        cmd = input("rnum > ")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog = "rnum",
        description = "Convert numbers to roman numerals. Use without arguments to start a cli session."
    )

    parser.add_argument(
        "numbers",
        metavar="N",
        type=int,
        nargs="*",
        help="Numbers to convert to roman numerals"
    )
    parser.add_argument(
        "-r", "--range",
        action="extend",
        nargs="+",
        type=int,
        default=[],
        metavar="UPPER_BOUND",
        help="Output a range of roman numerals. Uses N [N...] " \
            "as the lower bounds and UPPER_BOUND [UPPER_BOUND...] as upper bounds. " \
            "Bounds are matched by relative position. Both bounds are inclusive."
    )

    if len(sys.argv) == 1:
        cli_loop()
        exit(0)

    args = parser.parse_args()
    int_to_rnum_range(args.numbers, args.range)


if __name__ == "__main__":
    main()

