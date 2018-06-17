# coding=utf-8
"""
The main interface that will be exported for use
"""
from kangradb.binary_tree import BinaryTree
from kangradb.physical_storage import Storage


class KangraDB(object):
    """
    KangraDB interface that will be used to do stuff
    """

    def __init__(self, f):
        self._storage = Storage(f)
        self._tree = BinaryTree(self._storage)

    def _assert_not_closed(self):
        if self._storage.closed:
            raise ValueError('Database closed.')

    def close(self):
        """
        close storage
        """
        self._storage.close()

    def commit(self):
        """
        commit data from tree to storage
        """
        self._assert_not_closed()
        self._tree.commit()

    def __getitem__(self, key):
        """
        invoked when called like this: db[key]
        :param key:
        :return:
        """
        self._assert_not_closed()
        return self._tree.get(key)

    def __setitem__(self, key, value):
        """
        invoked when called like this: db[key] = value
        :param key:
        :return:
        """
        self._assert_not_closed()
        return self._tree.set(key, value)

    def __delitem__(self, key):
        self._assert_not_closed()
        return self._tree.pop(key)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __len__(self):
        return len(self._tree)
