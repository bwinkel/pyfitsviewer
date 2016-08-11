#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main(args=None):
    '''Launch pyfitsviewer.'''
    if args is None:
        args = sys.argv[1:]

    from pyfitsviewer import start_fitsviewer
    start_fitsviewer()


if __name__ == '__main__':
    main()
