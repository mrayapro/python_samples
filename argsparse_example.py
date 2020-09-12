import argparse
import oci
import os
import string
import time
import sys

def main(args):
      my_tenancy=args.tenancy
      stacks=args.stacks
      print(f"mytenancy = {my_tenancy}")
      print(f"Stacks = {stacks}")


if __name__ == '__main__':
    '''
    This is executed when run from the command line
    '''
    parser = argparse.ArgumentParser()

    parser.add_argument('-sts', '--stacks',
                        default='None',
                        help='Number of stacks to have Grid patching <all/one>')

    # Optional arguments with defaults
    parser.add_argument('-t', '--tenancy',
                        default='None',
                        help='Which tenancy to run the precheck')

    args = parser.parse_args()

    main(args)
