import os
import shutil
import threading


def sort_files(directory):
    def move_files(files, extension):
        folder_path = os.path.join(directory, extension[1:])
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            src = os.path.join(directory, file)
            dst = os.path.join(folder_path, file)
            try:
                shutil.move(src, dst)
                print(f"Moved {len(files)} files with extension {extension}.")
            except Exception as e:
                print(f"Error moving files: {e}")

    extensions = {}
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            extension = os.path.splitext(filename)[1]
            if extension:
                if extension not in extensions:
                    extensions[extension] = []
                extensions[extension].append(filename)

    threads = []
    for extension, files in extensions.items():
        t = threading.Thread(target=move_files, args=(files, extension))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    sort_files("Temp")
