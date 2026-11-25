# SPDX-License-Identifier: MIT
"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the word the entrant's ex
would use to describe them. 'Layaway' — she put a little down, kept him
on hold in the back, and never came back to pick him up. It won a
16-candidate criteria-ordered tournament (judge criteria in order:
one real word an ex would use, laugh, sting of recognition, instant,
relatable) across 4 weight-perturbation iterations plus a round-robin,
and a refinement round picked it over the raw finalists 'Tutorial' and
'Understudy' because those words already appear in the field and
byte-identical entries share one rate with the earlier receipt placing
first — while 'Layaway' has zero field presence and the maximum
laugh+sting score in the pool.

The output is byte-exact: 7 UTF-8 bytes, no trailing newline, well
inside the gate of 1 to 24 characters of UTF-8 text.
"""

from pathlib import Path

WORD = "Layaway"
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()
