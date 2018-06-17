# coding=utf-8
"""
Storage class
"""

import os
import struct

import portalocker


class Storage(object):
    """
    Storage class that saves data in a file
    """
    SUPERBLOCK_SIZE = 4096
    INTEGER_FORMAT = "!Q"
    INTEGER_LENGTH = 8

    def __init__(self, f):
        self._file = f
        self.locked = False
        self._ensure_superblock()

    def _ensure_superblock(self):
        self.lock()
        self._seek_end()
        end_address = self._file.tell()
        if end_address < self.SUPERBLOCK_SIZE:
            self._file.write(b'\x00' * (self.SUPERBLOCK_SIZE - end_address))
        self.unlock()

    def lock(self):
        """
        lock file
        :return:
        """
        if not self.locked:
            portalocker.lock(self._file, portalocker.LOCK_EX)
            self.locked = True
            return True
        else:
            return False

    def unlock(self):
        """
        unlock file
        """
        if self.locked:
            self._file.flush()
            portalocker.unlock(self._file)
            self.locked = False

    def _seek_end(self):
        self._file.seek(0, os.SEEK_END)

    def _seek_superblock(self):
        self._file.seek(0)

    def _bytes_to_integer(self, integer_bytes):
        return struct.unpack(self.INTEGER_FORMAT, integer_bytes)[0]

    def _integer_to_bytes(self, integer):
        return struct.pack(self.INTEGER_FORMAT, integer)

    def _read_integer(self):
        return self._bytes_to_integer(self._file.read(self.INTEGER_LENGTH))

    def _write_integer(self, integer):
        self.lock()
        self._file.write(self._integer_to_bytes(integer))

    def write(self, data):
        """
        write to file
        :param data:
        :return:
        """
        self.lock()
        self._seek_end()
        object_address = self._file.tell()
        self._write_integer(len(data))
        self._file.write(data)
        return object_address

    def read(self, address):
        """
        read from file at given address
        :param address:
        :return:
        """
        self._file.seek(address)
        length = self._read_integer()
        data = self._file.read(length)
        return data

    def commit_root_address(self, root_address):
        """
        commit root address of a tree
        :param root_address:
        """
        self.lock()
        self._file.flush()
        self._seek_superblock()
        self._write_integer(root_address)
        self._file.flush()
        self.unlock()

    def get_root_address(self):
        """
        get root address
        :return:
        """
        self._seek_superblock()
        root_address = self._read_integer()
        return root_address

    def close(self):
        """
        Close file
        """
        self.unlock()
        self._file.close()

    @property
    def closed(self):
        """
        check if closed
        :return:
        """
        return self._file.closed
