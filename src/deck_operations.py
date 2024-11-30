from typing import List
from models import CrowdAnkiJson, OutputNote


def html_remove(text: str) -> str:
    # Note: It does not remove img nor span, this is by design.
    # Some cards would have an empty source/target otherwise.
    return (
        text.replace("&nbsp;", "")
        .replace("<i>", "")
        .replace("</i>", "")
        .replace("<b>", "")
        .replace("</b>", "")
        .replace("<u>", "")
        .replace("</u>", "")
        .replace("<ol>", "")
        .replace("</ol>", "")
        .replace("<li>", "")
        .replace("</li>", "")
        .replace("&gt;", ">")
        .replace("&lt;", "<")
        .replace('"', "")
    )


def deck_to_output_notes(json: CrowdAnkiJson) -> List[OutputNote]:
    output_notes = []

    for child in json.children:
        output_notes = output_notes + deck_to_output_notes(child)

        for note in child.notes:
            if len(note.fields) != 2:
                print("Warn - This note has more than 2 fields!")
            else:
                fields = note.fields
                output_notes.append(
                    OutputNote(
                        source=html_remove(fields[0]), target=html_remove(fields[1])
                    )
                )

    return output_notes
