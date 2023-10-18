#!/usr/bin/env python

import argparse


def say_hello(name):
    print(f'hello {name}!')

def say_bye(name):
    print(f'bye {name}!')

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('name', help='name to say hello to')
arg_parser.add_argument('--msg',help='message type')
args = arg_parser.parse_args()

if args.msg == 'hello':
    say_hello(args.name)
elif args.msg == 'bye':
    say_bye(args.name)
else:
    print('unknown message')
