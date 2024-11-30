# Anki Parser

In this repository you find a parser that will transform your Anki cards into a JSON format.

## Dependencies

* [CrowdAnki](https://ankiweb.net/shared/info/1788670778) to get the Anki Deck as JSON
* [Click](https://click.palletsprojects.com/en/stable/) for argument parsing

## Usage

Use the CrowdAnki plugin to obtain your deck in a JSON format.

```
$ python3 src/parser.py -f deck.json -o output.json
Processed 1337 records.
```

Parameters:

* `-i` - File for the JSON input, obtained from CrowdAnki's export
* `-o` - File to write the output to, the file will be overwritten

## Output

The parser accesses only minimal information from the Anki JSON.
Moreover certain HTML tags are removed.
To see the details of what tags get removed from the fields, please look into `src/deck_operations.py`.
As you may notice, the linebreak tag `<br>` is not removed.
This is by intention.
Moreover it is assumed that any `note` may only have 2 entries (it will ignore entries that have more and print a warning).

The output is of the form (compacted):

```
[
    { "source": "word", "target": "sana" },
    ...
]
```
