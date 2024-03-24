import pytest

from jrnl.journals.Entry import Entry
from jrnl.journals.Journal import Journal


@pytest.mark.parametrize(
    "text, tag_symbols, expected_tags",
    [
        ("This has no tag symbols", "", []),
        ("This has no tags and a single tag symbol", "@", []),
        ("This has no tags and multiple tag symbols", "@#", []),
        ("This has a @simple tag", "@", ["@simple"]),
        ("Tag can contain some punctuation @simple-tag.", "@", ["@simple-tag"]),
        ("This has a tag at the end of a sentence @simple.", "@", ["@simple"]),
        ("This has an empty @ tag", "@", []),
        ("This text has @multiple @tags", "@", ["@multiple", "@tags"]),
        ("@@@@ This text has no tags", "@", []),
        ("@@@# This text has no @### tags", "@#", []),
        ("@@@#tag1 This text has two #@#@tags", "@#", ["@@@#tag1", "#@#@tags"]),
        (
            "@prefix#tag1 This text has two #prefix@tag2",
            "@#",
            ["@prefix#tag1", "#prefix@tag2"],
        ),
    ],
)
def test_tag_extraction(text, tag_symbols, expected_tags):
    jrnl = Journal()
    jrnl.config["tagsymbols"] = tag_symbols

    entry = Entry(jrnl, date=None, text=text)
    if entry.tags != expected_tags:
        pass

    assert sorted(entry.tags) == sorted(expected_tags)
