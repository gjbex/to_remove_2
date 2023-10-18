#!/usr/bin/env python

import argparse


def say_hello(name):
    print(f'hello {name}!')

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('name', help='name to say hello to')
args = arg_parser.parse_args()
say_hello(args.name)
