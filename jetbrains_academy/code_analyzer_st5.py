import argparse
import os
from pathlib import Path
import re
import ast
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class ErrorInfo:
    line: int
    number: str
    message: str


def check_lines(file_name: str, is_valid, err_num: str, err_msg: str) -> list[ErrorInfo]:
    result = []
    with open(file_name) as file:
        current_line = 1
        for line in file:
            if not is_valid(line):
                result.append(ErrorInfo(current_line, err_num, err_msg))
            current_line += 1
    return result


class LengthChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        def is_valid(line: str) -> bool:
            return len(line) <= 79

        return check_lines(file_name, is_valid, 'S001', 'Too long')


class IndentFourChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        def is_valid(line: str) -> bool:
            indent = 0
            for letter in line:
                if letter == ' ':
                    indent += 1
                else:
                    break
            return indent % 4 == 0

        return check_lines(file_name, is_valid, 'S002', 'Indentation is not a multiple of four')


class UnnecSemicolonChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:

        def is_valid(line: str) -> bool:
            quoteopen = False
            for letter in line:
                if not quoteopen:
                    if letter == '#':
                        break
                    if letter == '\'':
                        quoteopen = True
                        pass
                    if letter == ';':
                        return False
                else:
                    if letter == '\'':
                        quoteopen = False
                        pass
            return True

        return check_lines(file_name, is_valid, 'S003', 'Unnecessary semicolon after a statement')


class TwoSpacesChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        def is_valid(line: str) -> bool:
            try:
                comment_index = line.index('#')
                if comment_index == 0:
                    return True
                if comment_index < 2:
                    return False
                if line[comment_index - 1] != ' ' or line[comment_index - 2] != ' ':
                    return False
                return True
            except ValueError:
                pass
            return True

        return check_lines(file_name, is_valid, 'S004', 'Less than two spaces before inline comments')


class TodoChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        def is_valid(line: str) -> bool:
            try:
                comment_index = line.index('#')
                if 'TODO' in line[comment_index:len(line)].upper():
                    return False
            except ValueError:
                pass
            return True

        return check_lines(file_name, is_valid, 'S005', 'TODO found')


class BlankLinesChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        result = []
        with open(file_name) as file:
            current_line = 1
            counter = 0
            for line in file:
                if line != '\n':
                    if counter > 2:
                        result.append(ErrorInfo(
                            current_line,
                            'S006',
                            'More than two blank lines preceding a code line')
                        )
                    counter = 0
                else:
                    counter += 1

                current_line += 1
        return result


class SpacesConstructionChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        result = []
        with open(file_name) as file:
            current_line = 1
            for line in file:
                if re.match(' *class  +', line):
                    result.append(ErrorInfo(
                        current_line,
                        'S007',
                        'Too many spaces after Class')
                    )
                if re.match(' *def  +', line):
                    result.append(ErrorInfo(
                        current_line,
                        'S007',
                        'Too many spaces after def')
                    )
        return result


class ClassCamelCaseChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        result = []
        with open(file_name) as file:
            tree = ast.parse(file.read())
            nodes = ast.walk(tree)
            for node in nodes:
                if isinstance(node, ast.ClassDef):
                    if re.match('[A-Z][a-zA-Z0-9]+', node.name) is None:
                        result.append(ErrorInfo(
                            node.lineno,
                            'S008',
                            f'Class name {node.name} should use CamelCase'
                        ))
        return result


class FuncSnakeCaseChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        result = []
        with open(file_name) as file:
            tree = ast.parse(file.read())
            nodes = ast.walk(tree)
            for node in nodes:
                if isinstance(node, ast.FunctionDef):
                    if re.match('_?_?[a-z0-9]+_?_?', node.name) is None:
                        result.append(ErrorInfo(
                            node.lineno,
                            'S009',
                            f'Function name {node.name} should use snake_case'
                        ))
        return result


class ArgSnakeCaseChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        result = []
        with open(file_name) as file:
            tree = ast.parse(file.read())
            nodes = ast.walk(tree)
            for node in nodes:
                if isinstance(node, ast.FunctionDef):
                    for arg in node.args.args:
                        if re.match('_?_?[a-z0-9]+_?_?', arg.arg) is None:
                            result.append(ErrorInfo(
                                node.lineno,
                                'S010',
                                f'Argument {arg.arg} should be snake_case'
                            ))
        return result


class VarSnakeCaseChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        result = []
        with open(file_name) as file:
            tree = ast.parse(file.read())
            nodes = ast.walk(tree)
            for node in nodes:
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                    if re.match('[a-z0-9]+', node.id) is None:
                        result.append(ErrorInfo(
                            node.lineno,
                            'S011',
                            f'Variable {node.id} in function should be snake_case'
                        ))
        return result


class ArgImmutabilityChecker:
    @staticmethod
    def check(file_name: str) -> list[ErrorInfo]:
        result = []
        with open(file_name) as file:
            tree = ast.parse(file.read())
            nodes = ast.walk(tree)
            for node in nodes:
                if isinstance(node, ast.FunctionDef):
                    for arg in node.args.defaults:
                        if isinstance(arg, ast.List):
                            result.append(ErrorInfo(
                                node.lineno,
                                'S012',
                                'Default argument value is mutable'
                            ))
        return result


class Analyzer:
    def __init__(self):
        self.checkers = [LengthChecker(),
                         IndentFourChecker(),
                         UnnecSemicolonChecker(),
                         TwoSpacesChecker(),
                         TodoChecker(),
                         BlankLinesChecker(),
                         SpacesConstructionChecker(),
                         ClassCamelCaseChecker(),
                         FuncSnakeCaseChecker(),
                         ArgSnakeCaseChecker(),
                         VarSnakeCaseChecker(),
                         ArgImmutabilityChecker()
                         ]

    def check_file(self, file_name):
        errors = []
        for checker in self.checkers:
            errors.extend(checker.check(file_name))

        errors.sort()
        for error in errors:
            print(f"{file_name}: Line {error.line}: {error.number} {error.message}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src_path')
    args = parser.parse_args()
    src_path = args.src_path

    if Path(src_path).is_file():
        a = Analyzer()
        a.check_file(src_path)
    else:
        a = Analyzer()
        for input_file_name in os.listdir(src_path):
            if input_file_name == 'tests.py':  # ¯\_(ツ)_/¯ JB Academy
                continue
            if input_file_name.endswith(".py"):
                a.check_file(str(Path(src_path) / input_file_name))
