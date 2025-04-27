import os


def main():
    min_file_size = int(
        input("You want to find file sizes larger than...(numbers only)? "))
    what_metric = input("Is that in b, kb, mb, gb, or tb? Choose one: ")
    if what_metric == 'b':
        divisor = 1  # bytes to bytes
    elif what_metric == 'kb':
        divisor = 1000
    elif what_metric == 'mb':
        divisor = 1000000
    elif what_metric == 'gb':
        divisor = 1000000000
    elif what_metric == 'tb':
        divisor = 1000000000000
    else:
        print("Invalid metric. Please choose b, kb, mb, gb, or tb.")
        return

    if min_file_size:
        for root, directories, files in os.walk('/Users/van/Documents'):
            for _file in files:
                full_path = os.path.join(root, _file)
                size = os.path.getsize(full_path)
                if what_metric == 'b':
                    size = size / divisor
                elif what_metric == 'kb':
                    size = size / divisor
                elif what_metric == 'mb':
                    size = size / divisor
                elif what_metric == 'gb':
                    size = size / divisor
                elif what_metric == 'tb':
                    size = size / divisor
                else:
                    print(
                        f"{what_metric} is an invalid metric. Please choose b, kb, mb, gb, or tb.")
                    return

                if size > min_file_size:

                    print(
                        f"Size: {int(size)} {what_metric} - File: {full_path}")


main()
