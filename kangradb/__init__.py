# coding=utf-8
"""
__init__
"""
import os

from kangradb.interface import KangraDB

__all__ = ['KangraDB', 'connect']


def connect(db_name):
    """
    connect to db
    :param db_name:
    :return:
    """
    db_name += '.kng'
    try:
        f = open(db_name, 'r+b')
    except IOError:
        fd = os.open(db_name, os.O_RDWR | os.O_CREAT)
        f = os.fdopen(fd, 'r+b')
    return KangraDB(f)
