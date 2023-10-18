#!/usr/bin/env python

import argparse


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('name', help='name to say hello to')
arg_parser.add_argument('--type', choices=['hello', 'bye'], help='message type')
args = arg_parser.parse_args()

if args.type == 'hello':
    print(f'hello {args.name}!')
else:
print(f'bye {args.name}!')
