import os


def move_file(command: str) -> None:
    parts = command.split()
    src = parts[1]
    dst = parts[2]

    print(parts)

    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    dir_path = os.path.dirname(dst)

    if dir_path:
        sub_dirs = dir_path.split("/")
        current_path = ""
        for folder in sub_dirs:
            if folder:
                current_path = os.path.join(current_path, folder)\
                    if current_path else folder
                if not os.path.exists(current_path):
                    os.mkdir(current_path)

    with open(src, "r") as f_src:
        content = f_src.read()

    with open(dst, "w") as f_dst:
        f_dst.write(content)

    os.remove(src)


print(move_file("mv file.txt first_dir/second_dir/third_dir/file2.txt"))
