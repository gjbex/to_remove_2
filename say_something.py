#!/usr/bin/env python

import argparse
import utils


def say_hello(name):
    print(f'hello {name}!')

def say_bye(name):
    print(f'bye {name}!')

args = utils.handle_cla()
if args.verbose:
    print('starting...')
if args.type == 'hello':
    say_hello(args.name)
elif args.type == 'bye':
    say_bye(args.name)
else:
    print('unknown message')
if args.verbose:
    print('done...')
