# coding=utf-8
"""
test everything
"""

import os
from pathlib import Path
from unittest import TestCase

from click.testing import CliRunner

from kangra import cli


class TestKangraDB(TestCase):
    """
        Test Kangra DB
    """

    def __init__(self, methodName='runTest'):
        super(TestKangraDB, self).__init__()
        self.runner = CliRunner()

    def runTest(self):
        """
        run the test
        """
        result = self.runner.invoke(cli)
        self.assertEqual(0, result.exit_code)

        result = self.runner.invoke(cli, ['query'])
        self.assertEqual(2, result.exit_code)

        db_name = 'mp'
        file_name = db_name + '.kng'
        if Path(file_name).is_file():
            os.remove(file_name)

        result = self.runner.invoke(cli, ['query', db_name, 'get', 'pappu'])
        output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        self.assertEqual(3, result.exit_code)
        self.assertEqual("Key not found\n", output_string)

        result = self.runner.invoke(cli, ['query', db_name, 'set', 'pappu', 'Haye rabba'])
        self.assertEqual(0, result.exit_code)

        result = self.runner.invoke(cli, ['query', db_name, 'get', 'pappu'])
        output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        self.assertEqual(0, result.exit_code)
        self.assertEqual("Haye rabba", output_string)

        result = self.runner.invoke(cli, ['query', db_name, 'delete', 'pappu'])
        self.assertEqual(0, result.exit_code)

        result = self.runner.invoke(cli, ['query', db_name, 'get', 'pappu'])
        output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        self.assertEqual(3, result.exit_code)
        self.assertEqual("Key not found\n", output_string)

        result = self.runner.invoke(cli, ['query', db_name, 'set', 'pappu1', 'Haye rabba1'])
        self.assertEqual(0, result.exit_code)

        result = self.runner.invoke(cli, ['query', db_name, 'set', 'pappu2', 'Haye rabba2'])
        self.assertEqual(0, result.exit_code)

        result = self.runner.invoke(cli, ['query', db_name, 'set', 'pappu3', 'Haye rabba3'])
        self.assertEqual(0, result.exit_code)

        result = self.runner.invoke(cli, ['query', db_name, 'get', 'pappu1'])
        output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        self.assertEqual(0, result.exit_code)
        self.assertEqual("Haye rabba1", output_string)

        result = self.runner.invoke(cli, ['query', db_name, 'get', 'pappu2'])
        output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        self.assertEqual(0, result.exit_code)
        self.assertEqual("Haye rabba2", output_string)

        result = self.runner.invoke(cli, ['query', db_name, 'get', 'pappu3'])
        output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        self.assertEqual(0, result.exit_code)
        self.assertEqual("Haye rabba3", output_string)

        result = self.runner.invoke(cli, ['query', db_name, 'get', 'pappu4'])
        output_string = str(result.output.encode('ascii', 'ignore').decode("utf-8"))
        self.assertEqual(3, result.exit_code)
        self.assertEqual("Key not found\n", output_string)

        self.assertTrue(Path(file_name).is_file())

        # clean up
        if Path(file_name).is_file():
            os.remove(file_name)
