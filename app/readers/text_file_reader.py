from pathlib import Path


def read_tsv_to_dict(fp: Path) -> dict:
    with open(fp, "r") as f:
        file_lines = f.readlines()
        header = file_lines[0].strip().split("\t")
        data_rows = file_lines[1:]

    table = []
    for value_line in data_rows:
        values = value_line.strip().split("\t")
        row = {}
        for i in range(len(values)):
            row[header[i]] = values[i]
        table.append(row)

    return table
