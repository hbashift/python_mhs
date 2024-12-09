import sys


def wc_command():
    files = sys.argv[1:]
    total_lines, total_words, total_bytes = 0, 0, 0

    def count_file(file_content):
        lines = file_content.splitlines()
        words = file_content.split()
        return len(lines), len(words), len(file_content.encode())

    if not files:
        file_content = sys.stdin.read()
        lines, words, bytes_ = count_file(file_content)
        print(f"{lines}\t{words}\t{bytes_}")
        return

    for file_name in files:
        try:
            with open(file_name, "r") as f:
                content = f.read()
        except FileNotFoundError:
            print(f"wc: cannot open '{file_name}' for reading: No such file")
            continue

        lines, words, bytes_ = count_file(content)
        total_lines += lines
        total_words += words
        total_bytes += bytes_

        print(f"{lines}\t{words}\t{bytes_}\t{file_name}")

    if len(files) > 1:
        print(f"{total_lines}\t{total_words}\t{total_bytes}\ttotal")


if __name__ == "__main__":
    wc_command()
