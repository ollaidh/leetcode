import unittest
import os
import dataclasses


@dataclasses.dataclass
class User:
    _: dataclasses.KW_ONLY
    user_id: int
    username: str
    user_type: str


def get_final_line(filename: str) -> str:
    last_line = ''
    with open(filename) as f:
        for line in f:
            last_line = line
    return last_line


def password_to_dict(filename: str) -> list:
    users = []
    with open(filename) as f:
        for line in f:
            if not line.startswith(('#', '\n')):
                curr_data = line.split(':')
                users.append(User(user_id=int(curr_data[2]), username=curr_data[0], user_type=curr_data[7]))

    return users


def sort_by_shells(filename: str) -> dict:
    shells = {}
    with open(filename) as f:
        for line in f:
            if not line.startswith(('#', '\n')):
                curr_data = line.split(':')
                if curr_data[-1].rstrip('\n') not in shells:
                    shells[curr_data[-1].rstrip('\n')] = []
                shells[curr_data[-1].rstrip('\n')].append(curr_data[0])

    return shells


class TestFileActions(unittest.TestCase):
    def test_get_final_line(self):
        file_path = f'{os.getcwd()}/files/sentences.txt'
        self.assertEqual('Go away.', get_final_line(file_path))

    def test_password_to_dict(self):
        file_path = f'{os.getcwd()}/files/passwds.txt'
        users = password_to_dict(file_path)
        self.assertEqual('nobody', users[0].username)
        self.assertEqual(77, users[26].user_id)
        self.assertEqual('FTP Daemon', users[42].user_type)
        self.assertEqual('_launchservicesd', users[75].user_type)

    def test_sort_by_shells(self):
        file_path = f'{os.getcwd()}/files/passwds.txt'
        shells_data = sort_by_shells(file_path)
        self.assertEqual(['root'], shells_data['/bin/sh'])
        self.assertEqual(74, len(shells_data['/usr/bin/false']))
        self.assertEqual(3, len(shells_data))


if __name__ == '__main__':
    unittest.main()
