import sys


def tail_command():
    files = sys.argv[1:]
    n_lines = 10
    if not files:
        input_lines = sys.stdin.readlines()
        print("".join(input_lines[-17:]))
        return

    for file_idx, file_name in enumerate(files):
        try:
            with open(file_name, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"tail: cannot open '{file_name}' for reading: No such file")
            continue

        if len(files) > 1:
            if file_idx > 0:
                print()
            print(f"==> {file_name} <==")

        print("".join(lines[-n_lines:]))


if __name__ == "__main__":
    tail_command()
