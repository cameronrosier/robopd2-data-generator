import argparse
import json
import logging
from app.generator.runeword import RunewordGenerator
from app.generator.unique import UniqueGenerator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: [%(levelname)s] %(message)s",
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Item Data for Project Diablo 2"
    )
    parser.add_argument("--text-files", help="Path to .txt files")
    parser.add_argument("--table-files", default=".", help="Path to .tbl files")
    parser.add_argument("--output", default=".", help="Path to output folder")
    parser.add_argument(
        "--uniques", "-u", action="store_true", help="Generate unique item data"
    )
    parser.add_argument(
        "--sets", "-s", action="store_true", help="Generate full set data"
    )
    parser.add_argument(
        "--set-items", "-si", action="store_true", help="Generate set item data"
    )
    parser.add_argument(
        "--runewords", "-rw", action="store_true", help="Generate runeword item data"
    )
    parser.add_argument(
        "--cube-recipes",
        "-c",
        action="store_true",
        help="Generate cube recipe item data",
    )
    parser.add_argument(
        "--storage-engine",
        "-e",
        choices=["mongo", "cosmos"],
        default="mongo",
        help="Storage engine to use (cosmos or mongo)",
    )
    parser.add_argument(
        "--dry-run",
        "-d",
        action="store_true",
        default=False,
        help="Run the generator without writing to the database"
    )

    args = parser.parse_args()

    if args.uniques:
        unique_gen = UniqueGenerator(
            output_dir=args.output,
            text_files=args.text_files,
            table_files=args.table_files,
        )
        unique_items = unique_gen.generate_unique_item_data()

    if args.runewords:
        runeword_gen = RunewordGenerator(
            output_dir=args.output,
            text_files=args.text_files,
            table_files=args.table_files,
        )
        runeword_items = runeword_gen.generate_runeword_item_data()
        with open('runewords.json', 'w') as f:
            json.dump(runeword_items, f, indent=4)
