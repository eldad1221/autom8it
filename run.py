import argparse
from autom8it import run_yaml


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="Path to YAML file")
    args = parser.parse_args()
    file_path = args.file
    if file_path is None:
        file_path = 'run.yaml'

    run_yaml(file_path=file_path)
