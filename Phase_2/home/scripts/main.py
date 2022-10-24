import glob
import json


def print_notebook(file_path):
    try:
        with open(file_path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        error = f"Didn't find an index.ipynb in {file_path}."
        return error
    else:
        result = []
        for cell in data['cells']:
            last = ""
            if cell['cell_type'] == "code":
                first = "```python"
                last = "```"
                yield first
            for line in cell['source']:
                line = line.rstrip()
                line = line.encode(encoding='ascii', errors='namereplace')
                line = line.decode()
                yield line
            yield last

def main():

    targets = []
    for n in glob.iglob('C:/Users/Drew Alderfer/code/flatiron/NYC-DS-091922/Phase_2//**/*.ipynb', recursive=True):
        targets.append(n)
    lines = []
    for topic in targets:
        print(topic)
        for line in print_notebook(topic):
            lines.append(line)
            lines.append("\n")
        lines.append("\n-----File-Boundary-----\n")

    # for x in lines:
    #     print(x)
    with open('../home.md', 'w', encoding='UTF-8') as index:
        index.writelines(lines)

if __name__ == '__main__':
    main()
