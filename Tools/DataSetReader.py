from typing import List
from Grapher.MultiAxesGraph import MultiAxesGraph
from DataBases.DataManagerCSV import DataManagerCSV, process_data


def read_dataset(path: str, is_digital: List[bool], verbose: bool = False):
    with open(path) as file:
        fieldnames = [key.replace("\n", "") for key in file.readline().split(",")]

    print("Reading dataset...")
    collector = DataManagerCSV(
        path=path,
        fieldnames=fieldnames,
    )

    read_data = collector.read()
    if verbose:
        print(*read_data, sep="\n")

    if not len(read_data):
        raise ValueError("No data has been found!")

    print("Processing data...")
    data = process_data(read_data=read_data, is_digital=is_digital)
    if verbose: print(*data, sep="\n")

    print("Initialising graph...")
    graph = MultiAxesGraph(
        fieldnames=fieldnames,
        data=data,
        title=path,
    )

    print("Plotting graph...")
    graph.show(can_save=True, path="Output")

    print("Graph successfully generated!")
    print("Look for it in the `Output` directory!")
