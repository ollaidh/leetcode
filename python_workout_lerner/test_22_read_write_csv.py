import pathlib
import csv
import os
import tempfile
import unittest


def passwd_to_csv(input_file: pathlib.Path, output_file) -> None:

    with open(input_file, 'r') as scvinp, open(output_file, 'w') as csvout:
        inp_reader = csv.reader(scvinp, delimiter=':')
        inp_writer = csv.writer(csvout, delimiter='\t')
        for row in inp_reader:
            if row[0].startswith('#'):
                continue
            inp_writer.writerow((row[0], row[2]))


class TestCsv(unittest.TestCase):
    def test_passwd_to_csv(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            filepath_inp = pathlib.Path(__file__).parent.resolve() / '22_read_write_csv' / 'input.csv'
            filepath_out = pathlib.Path(tmpdirname) / 'output.csv'
            passwd_to_csv(filepath_inp, filepath_out)
            with open(filepath_out, 'r', newline='') as f:
                file_lines = f.readlines()
                self.assertEqual(3, len(file_lines))
                self.assertEqual(2, len(file_lines[0].split('\t')))
                self.assertEqual('root', file_lines[0].split('\t')[0])
                self.assertEqual('0', file_lines[0].split('\t')[1].rstrip())
                self.assertEqual(2, len(file_lines[2].split('\t')))
                self.assertEqual('_ftp', file_lines[2].split('\t')[0])
                self.assertEqual('98', file_lines[2].split('\t')[1].rstrip())


if __name__ == '__main__':
    unittest.main()
