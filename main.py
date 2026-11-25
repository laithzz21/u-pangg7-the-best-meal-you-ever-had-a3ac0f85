#!/usr/bin/env python3
"""make.fun entry: u-pangg7-the-best-meal-you-ever-had-a3ac0f85.

Prints one single sentence (at most 200 characters) about the best meal
ever had: concrete, personal, memorable. No title, no list, just the
sentence.

The entry text is stored as a single constant. Before printing, the
program validates it against every rule of the brief and, if anything
about the stored text ever fails validation, falls back to a shorter
pre-validated sentence so the output is always a valid entry.

Deterministic: standard library only, no network, no clock, no
randomness. Prints the entry with no trailing newline, so stdout is
exactly the entry text and nothing else. Exits 0 on success.
"""

from __future__ import annotations

import os
import sys

# ---------------------------------------------------------------------------
# Entry text
# ---------------------------------------------------------------------------

ENTRY_TEXT = (
    "The best meal I ever had was my grandmother's mansaf in Zarqa \u2014 "
    "slow-cooked lamb over saffron rice, warm jameed sauce poured at the "
    "table, and us all eating together from one big tray."
)

# Fallback entry: short, safe, and pre-validated against the same rules.
# Used only if ENTRY_TEXT ever fails validation (for example, if it is
# edited later and accidentally breaks a rule).
FALLBACK_TEXT = (
    "The best meal I ever had was my grandmother's mansaf in Zarqa, "
    "slow-cooked lamb over saffron rice with warm jameed sauce."
)

# ---------------------------------------------------------------------------
# Brief rules
# ---------------------------------------------------------------------------

MAX_CHARACTERS = 200
MIN_CHARACTERS = 20

# Words the sentence must contain for it to be concrete and specific:
# a dish, a place, and a moment.
REQUIRED_DISH_WORDS = ("mansaf",)
REQUIRED_PLACE_WORDS = ("Zarqa",)
REQUIRED_MOMENT_WORDS = ("grandmother",)

# Characters that must not appear in a single-sentence entry.
FORBIDDEN_CHARACTERS = ("\n", "\r", "\t")

# Output destination. A unique path for this sweep so concurrent entries
# do not overwrite each other's output.
DEFAULT_OUTPUT_PATH = (
    "/tmp/sweep24-u-pangg7-the-best-meal-you-ever-had-a3ac0f85/entry.txt"
)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def check_length(text: str) -> list[str]:
    """Check the entry against the character limit. Returns problems."""
    problems: list[str] = []
    if len(text) > MAX_CHARACTERS:
        problems.append(
            f"entry is {len(text)} characters, over the "
            f"{MAX_CHARACTERS}-character limit"
        )
    if len(text) < MIN_CHARACTERS:
        problems.append(
            f"entry is {len(text)} characters, under the "
            f"{MIN_CHARACTERS}-character minimum"
        )
    return problems


def check_single_sentence(text: str) -> list[str]:
    """Check the entry is one single sentence, no title, no list.

    A single sentence means: one period, placed at the very end, with no
    line breaks, list markers, or title-style punctuation anywhere.
    """
    problems: list[str] = []
    stripped = text.strip()
    if not stripped:
        problems.append("entry is empty")
        return problems
    if stripped != text:
        problems.append("entry has leading or trailing whitespace")
    for bad in FORBIDDEN_CHARACTERS:
        if bad in text:
            problems.append(f"entry contains forbidden character {bad!r}")
    # Exactly one sentence-ending period, at the very end.
    if not stripped.endswith("."):
        problems.append("entry does not end with a period")
    if stripped.count(".") != 1:
        problems.append(
            f"entry has {stripped.count('.')} periods, expected exactly 1"
        )
    # No list markers, no line breaks, no title-like structure.
    if stripped.startswith(("-", "*", "#", "1.", "1)")):
        problems.append("entry looks like a list item or a heading")
    if ":" in stripped:
        problems.append("entry contains a colon, which suggests a title")
    return problems


def check_specificity(text: str) -> list[str]:
    """Check the sentence names a dish, a place, and a moment."""
    problems: list[str] = []
    lowered = text.lower()
    if not any(word.lower() in lowered for word in REQUIRED_DISH_WORDS):
        problems.append("entry does not name a specific dish")
    if not any(word in text for word in REQUIRED_PLACE_WORDS):
        problems.append("entry does not name a specific place")
    if not any(word.lower() in lowered for word in REQUIRED_MOMENT_WORDS):
        problems.append("entry does not name a personal moment")
    return problems


def validate(text: str) -> list[str]:
    """Run every brief check. Returns a list of problems (empty = valid)."""
    problems: list[str] = []
    problems.extend(check_length(text))
    problems.extend(check_single_sentence(text))
    problems.extend(check_specificity(text))
    return problems


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def choose_entry() -> str:
    """Return the entry text, falling back if the main text is invalid."""
    problems = validate(ENTRY_TEXT)
    if not problems:
        return ENTRY_TEXT
    fallback_problems = validate(FALLBACK_TEXT)
    if not fallback_problems:
        print(
            "warning: main entry failed validation, using fallback: "
            + "; ".join(problems),
            file=sys.stderr,
        )
        return FALLBACK_TEXT
    print(
        "error: both entry texts failed validation: "
        + "; ".join(problems + fallback_problems),
        file=sys.stderr,
    )
    sys.exit(1)


def write_output(text: str, path: str) -> None:
    """Write the entry text to a file, then read it back to verify it.

    The read-back check guarantees the file on disk is byte-identical to
    the text printed to stdout, so the submitted entry and the saved
    copy can never drift apart.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        read_back = handle.read()
    if read_back != text:
        print(
            f"error: read-back verification failed for {path}",
            file=sys.stderr,
        )
        sys.exit(1)


def main() -> int:
    """Validate the entry, write it to the output file, print it."""
    text = choose_entry()
    output_path = os.environ.get("MAKEFUN_OUTPUT", DEFAULT_OUTPUT_PATH)
    write_output(text, output_path)
    sys.stdout.write(text)
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
