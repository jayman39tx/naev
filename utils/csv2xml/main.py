#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=80:

import os, sys
import csv
from lxml import etree
from argparse import ArgumentParser


def main(config):
    xmlReader = etree.parse(config.xmlfile)

    # TODO define appropriate dialect (excel, excel-tab or own)
    # see http://docs.python.org/library/csv.html#csv-fmt-params
    csvReader = csv.DialectReader(open(config.csvfile,'rU'))
    for cLine in self.csv:
        if config.outfit:
            ename = xmlReader.find('outfit[@name="{1}]"'.format(cLine['name']))


__version__ = '1.0'

if __name__ == '__main__':
    parser = ArgumentParser(description="""
        Naev csc to xml tool v%s.
    """ % __version__)
    parser.add_argument('--version', action='version',
                        version='%(prog)s '+__version__)
    parser.add_argument('--verbose', action='store_true', default=False,
                        help='Going verbose to see hidden secrets')
    parser.add_argument('csvfile',
                        help='Path to csv files directory')
    parser.add_argument('xmlfile',
                        help='Path to xml file')
    args = parser.parse_args()

    args.csvfile = os.path.abspath(args['csvfile'])
    args.xmlfile = os.path.abspath(args['xmlfile'])
