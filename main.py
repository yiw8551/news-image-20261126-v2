#!/usr/bin/env python3
"""news-image-20261126 entry: copy the pre-rendered entry.png to the
output directory. Standard library only.

Usage: python3 main.py [output-dir]
The output directory is argv[1], else $MAKEFUN_OUTPUT_DIR, else /output.
The copy is verified byte-for-byte against entry.png next to this file.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

# First 8 bytes every valid PNG must start with (RFC 2083).
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_png(path):
    """Fail loudly if the source is not a valid PNG, before copying."""
    if not os.path.isfile(path):
        print("error: source PNG not found: %s" % path, file=sys.stderr)
        return False
    with open(path, "rb") as f:
        header = f.read(len(PNG_SIGNATURE))
    if header != PNG_SIGNATURE:
        print("error: %s is not a valid PNG (bad signature)" % path,
              file=sys.stderr)
        return False
    return True


def main():
    outdir = None
    if len(sys.argv) > 1 and sys.argv[1]:
        outdir = sys.argv[1]
    elif os.environ.get("MAKEFUN_OUTPUT_DIR"):
        outdir = os.environ["MAKEFUN_OUTPUT_DIR"]
    else:
        outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    if not validate_png(SRC):
        return 1
    dst = os.path.join(outdir, "entry.png")
    shutil.copyfile(SRC, dst)
    if sha256_of(SRC) != sha256_of(dst):
        print("error: copied entry.png does not match the source", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes)" % (dst, os.path.getsize(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
