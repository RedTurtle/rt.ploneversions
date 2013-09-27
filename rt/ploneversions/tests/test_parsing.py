# -*- coding: utf-8 -*-
import os
from rt.ploneversions.ploneversions import (CFGParser,
                                            merge_versions,
                                            sort_versions)
from rt.ploneversions.tests import __path__ as test_path

mock_path = os.path.join(test_path[0], 'mocks')
os.chdir(mock_path)

fake_main = 'file:main.cfg'
cfgparser = CFGParser(fake_main)

# we cd in to the mock folder


def test_merge_versions():
    ''' Test the function that will merge the versions
    '''
    observed = merge_versions([('a', 1)], [('a', '2'), ('b', '1')])
    observed = sort_versions(observed)
    expected = [('a', '2'), ('b', '1')]


def test_get_extends_urls():
    ''' Test parsing
    '''
    observed = cfgparser.get_extends_urls()
    expected = ['file:sub2.cfg', 'file:sub1.cfg']
    assert (observed == expected)


def test_get_versions():
    ''' Test parsing
    '''
    expected = [('file:main.cfg', [('a', '1')]),
                ('file:sub2.cfg', [('a', '2'), ('c', '2')]),
                ('file:sub1.cfg', [('a', '3'), ('b', '1')]),
                ('file:subsub.cfg', [('a', '4'), ('d', '1.1')])
                ]

    observed = cfgparser.get_merged_versions()
    assert (observed == expected)


def test_call():
    ''' Call the cfgparser, should print something
    '''
    cfgparser()
