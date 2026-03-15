from Tools.DataCollector import DataCollector


def read_dataset(path):
    with open(path) as file:
        fieldnames = [key.replace("\n", "") for key in file.readline().split(",")]

    collector = DataCollector(
        filename=path,
        fieldnames=fieldnames,
        pairs_fieldnames=[("timestamp", "temperature"), ("timestamp", "moisture")],
        is_digital=[False, True]
    )

    print("Saving Images")
    collector.plot(can_save=True)

