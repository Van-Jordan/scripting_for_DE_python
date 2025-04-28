import os
import sys


def main(path_to_search='.'):
    min_file_size = int(
        input("You want to find file sizes larger than...(numbers only)? "))
    metric = input("Is that in b, kb, mb, gb, or tb? Choose one: ")
    if metric == 'b':
        divisor = 1  # bytes to bytes
    elif metric == 'kb':
        divisor = 1000
    elif metric == 'mb':
        divisor = 1000000
    elif metric == 'gb':
        divisor = 1000000000
    elif metric == 'tb':
        divisor = 1000000000000
    else:
        print("Invalid metric. Please choose b, kb, mb, gb, or tb.")
        return

    if min_file_size:
        for root, directories, files in os.walk(path_to_search):
            for _file in files:
                full_path = os.path.join(root, _file)
                size = os.path.getsize(full_path)
                if metric in ['b', 'kb', 'mb', 'gb', 'tb']:
                    size = size / divisor
                else:
                    print(
                        f"{metric} is an invalid metric. Please choose b, kb, mb, gb, or tb.")
                    return

                if size > min_file_size:

                    print(
                        f"Size: {int(size)} {metric} - File: {full_path}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path_to_search = sys.argv[1]
    else:
        path_to_search = '.'

    main(path_to_search)
