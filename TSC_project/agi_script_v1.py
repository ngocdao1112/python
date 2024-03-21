#!/usr/bin/env python

import sys

def main():

    sys.stderr.write("Hello world!\n")

    # Get value DYNAMIC_FEATURES
    dynamic_features = sys.argv[1] if len(sys.argv) > 1 else ""

    sys.stderr.write(sys.argv[1])

    # Check string dynamic_features contain 'apprecord' ?
    if "apprecord" in dynamic_features:
        sys.stderr.write("apprecord found in DYNAMIC_FEATURES\n")
    else:
        sys.stderr.write("apprecord not found in DYNAMIC_FEATURES\n")

if __name__ == "__main__":
    main()