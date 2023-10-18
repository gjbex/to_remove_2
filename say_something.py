#!/usr/bin/env python

import argparse


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('name', help='name to say hello to')
args = arg_parser.parse_args()

print(f'hello {args.name}!')
