import cowsay, sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])