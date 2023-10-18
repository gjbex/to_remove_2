def handle_cla():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('name', help='name to say hello to')
    arg_parser.add_argument('--type',help='message type')
    return arg_parser.parse_args()

