import logging
import os
import shutil

import click
import requests


logging.basicConfig(level=logging.INFO)


@click.command(context_settings=dict(max_content_width=120))
@click.option("--year", type=str, default="2018", show_default=True, help="Year number to retrieve input for")
@click.option("--session", type=str, help="Cookie session ID", default=lambda: os.environ.get("AOC_SESSION", ""))
@click.argument("day")
def main(year, day, session):
    if not session:
        raise ValueError("Must set session ID (AOC_SESSION)!")

    logging.info(f"Retrieving input data for {year} day {day}")
    input_response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session})

    try:
        input_response.raise_for_status()
    except requests.exceptions.HTTPError:
        logging.error("Failed to download input")
        return

    input_filepath = f"./{year}/{day}/input.txt"
    input_filepath_backup = f"./{year}/{day}/input_backup.txt"
    os.makedirs(os.path.dirname(input_filepath), exist_ok=True)

    with open(input_filepath, mode="wb") as fp:
        fp.write(input_response.content)

    logging.info(f"Dumped input to {input_filepath}")
    logging.info(f"Copying stub file")
    shutil.copyfile("./stub.py", f"./{year}/{day}/{day}a.py")
    shutil.copyfile(input_filepath, input_filepath_backup)


if __name__ == '__main__':
    main()
