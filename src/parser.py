from deck_operations import deck_to_output_notes
from models import CrowdAnkiJson

import click


@click.command()
@click.option("-i", "--inputfilename", required=True, type=str)
@click.option("-o", "--outputfilename", required=True, type=str)
def main(inputfilename, outputfilename):
    with open(inputfilename, "r") as deck_file:
        deck = deck_file.read()
        typed_deck = CrowdAnkiJson.model_validate_json(deck)
    parsed_deck = deck_to_output_notes(typed_deck)
    stringified_notes = [note.toOutputString() for note in parsed_deck]

    # Easy workaround to not deal with encoding/escaping of JSON Dumps
    string_output = "[" + ",".join(stringified_notes) + "]"

    with open(outputfilename, "w") as file:
        file.write(string_output)

    print(f"Processed {len(stringified_notes)} notes.")


if __name__ == "__main__":
    main()
