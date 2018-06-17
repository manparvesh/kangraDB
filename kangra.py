# coding=utf-8
"""
The CLI
"""
import sys

import click

import kangradb

OK = 0
BAD_ARGS = 1
BAD_VERB = 2
BAD_KEY = 3
VALUE_NOT_SPECIFIED = 5


@click.group()
def cli():
    """
    A simple key/value database implementation in Python, based on a chapter from the book "500 Lines or less"
    """


@cli.command()
@click.argument('db_name')
@click.argument('verb')
@click.argument('key')
@click.argument('value', required=False)
def query(db_name, verb, key, value):
    """
    Enter query for the DB

    The query should be in the following form:
    kangra query get
    """
    if verb in {'get', 'set', 'delete'}:
        db = kangradb.connect(db_name)
        try:
            if verb == 'get':
                sys.stdout.write(db[key])
            elif verb == 'set':
                if value is None:
                    print("Value not specified", file=sys.stderr)
                    sys.exit(VALUE_NOT_SPECIFIED)
                db[key] = value
                db.commit()
            else:
                del db[key]
                db.commit()
        except KeyError:
            print("Key not found", file=sys.stderr)
            sys.exit(BAD_KEY)
    else:
        sys.exit(BAD_VERB)
