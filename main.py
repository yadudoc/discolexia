import argparse
import os.path


def enumerate_files(filepath: str):

    if os.path.isdir(filepath):
        return os.listdir(filepath)
    else:
        return [filepath]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Add arguments
    parser.add_argument('-f', '--filepath', type=str, help="Filepath")

    # Parse the arguments
    args = parser.parse_args()

    print(f"Filepath = {args.filepath}")

    docs = enumerate_files(args.filepath)

    for doc in docs:
        print(f"{doc=}")


