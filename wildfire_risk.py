#!/usr/bin/env python3

import argparse
from argparse import Namespace

from Tools.SerialReader import SerialReader
from DataBases.DataManagerCSV import DataManagerCSV, process_data
from Grapher.MultiAxesGraph import MultiAxesGraph
from Tools.DataSetReader import read_dataset


def main():
    parser = argparse.ArgumentParser(
        description="Program that calculates the Wildfire risk."
    )

    parser.add_argument(
        "-m", "--mode",
        choices=["realtime", "simulation"],
        default="realtime",
        required=False,
        help="Select the mode (realtime or simulation)"
    )

    parser.add_argument(
        "-d", "--dataset",
        type=str,
        help="Dataset file used in simulation mode"
    )

    parser.add_argument(
        "-i", "--interval",
        type=int,
        default=24,
        help="Sampling interval in hours (default: 24)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    if args.mode == "simulation" and args.dataset is None:
        parser.error("--dataset is required when mode is 'simulation'")

    if args.verbose:
        print("Verbose mode enabled")
        print(f"Current mode is {args.mode}")


    print(f"Sampling interval: {args.interval} hours")

    if args.mode == "realtime":
        fieldnames = ["utc", "temperature", "moisture", "risk"]
        is_digital = [None, False, True, False]

        try:
            serial_reader = SerialReader(period=10, epsilon=4, fieldnames=list(zip(fieldnames, is_digital)), expr=r"^[0-9]+,[0-9]+$", verbose=args.verbose)
        except ValueError:
            print("The embedded system (micro:bit) has not been connected.")
        else:
            print("The program has been initialised as RealTime mode. Press CTRL+C to quit.")
            if args.verbose:    print("Database is being initialised...")
            database = DataManagerCSV(path="data.csv", fieldnames=fieldnames, verbose=args.verbose)

            print("Reading database previous records...")
            read_data = database.read()
            data = None
            if len(read_data):
                print("Processing data...")
                data = process_data(read_data=read_data, fieldnames=fieldnames, is_digital=is_digital)

            if args.verbose:    print("Grapher is being initialised...")
            grapher = MultiAxesGraph(fieldnames=fieldnames, data=data, verbose=args.verbose)

            serial_reader.attach(observer=database)
            serial_reader.attach(observer=grapher)

            serial_reader.read()
    else:
        start_simulation_mode(args)


def start_simulation_mode(args: Namespace):
    print("The program has been initialised as Simulation mode.")
    print(f"Reading data from: {args.dataset}")
    try:
        read_dataset(path=args.dataset, is_digital=[None, False, True, False], verbose=args.verbose)
    except FileNotFoundError:
        print("Your file has not been found, please, make sure that it exists!")
    except ValueError:
        print("Your file is empty, please, fill anything!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
    print("Program finished!")
