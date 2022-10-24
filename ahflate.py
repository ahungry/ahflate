#!/usr/bin/env python3

import re
import sys
import tarfile
import zipfile

def inflate_zip(filename):
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall()

def inflate_tar(filename):
  tar = tarfile.open(filename)

  for t in tar:
    if t.isdir():
      t.mode = 0o0755
    else:
      t.mode = 0o0644
  tar.extractall()
  tar.close()

def main():
    if len(sys.argv) != 2:
        print("Please enter one arg only (the file to decompress).")
        sys.exit(1)

    filename = sys.argv[1]

    if re.search('.*\.zip$', filename):
        print("zipfile")
        inflate_zip(filename)
        return

    if re.search('.*\.tar.gz$', filename):
        print("tarball")
        inflate_tar(filename)
        return

if __name__ == '__main__':
    main()
