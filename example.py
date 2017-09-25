#! /usr/bin/python -u

import os, sys, pickle, random, glob, gzip
import argparse as ap
import igraph as ig


if __name__ == '__main__':

    p = ap.ArgumentParser()

    args = p.parse_args()


    # create random graph
    # generate .tikz for the graph
    # dump it to disk.


