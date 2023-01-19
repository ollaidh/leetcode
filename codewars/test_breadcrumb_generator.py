# KUY 4
# purpose is to create a function that takes a url, strips the first part (labelling it always HOME)
# and then builds it making each element but the last a <a> element linking to the relevant path;
# last has to be a <span> element getting the active class.
# All elements need to be turned to uppercase and separated by a separator,
# given as the second parameter of the function; the last element can terminate in some common extension like
# .html, .htm, .php or .asp; if the name of the last element is index.something, you treat it as if it wasn't there,
# sending users automatically to the upper level folder.
# If one element (other than the root/home) is longer than 30 characters, you have to shorten it, acronymizing it;
# ignore words in this array while acronymizing: ["the","of","in","from","by","with","and","or","for","to", "at", "a"];
# a url composed of more words separated by - and equal or less than 30 characters long needs to be just uppercased
# with hyphens replaced by spaces.
# Ignore anchors (www.url.com#lameAnchorExample) and parameters (www.url.com?codewars=rocks&pippi=rocksToo) when present.


import unittest
import re


def split_url(line: str) -> list[str]:
    line1 = line.split('://')
    if len(line1) == 1:
        return line1[0].split('/')
    else:
        line2 = line1[1].split('/')
        line2[0] = line1[0] + '://' + line2[0]
        return line2


def cut_endings(elements: list[str]) -> list[str]:
    if elements[-1] == '':
        elements.pop()

    # if last element is 'index.smth', it is deleted:
    pattern = 'index.'
    match = re.match(pattern, elements[-1])
    if match:
        elements.pop()

    # if last element terminate in some common extension like .html, .htm, .php or .asp we ignore (delete) it:
    pattern = r'\..*'
    match = re.search(pattern, elements[-1])
    if match:
        elements[-1] = elements[-1][:match.start()]

    # ignore (delete) anchors and parameters:
    pattern = r'#|\?'
    match = re.search(pattern, elements[-1])
    if match:
        elements[-1] = elements[-1][:match.start()]

    return elements


def alterate_home(elements: list[str]) -> list[str]:
    elements[0] = 'HOME'
    return elements


def paths_gen(elements: list[str]) -> list[str]:
    paths = ['' for _ in range(0, len(elements))]
    for i in range(1, len(paths) - 1):
        paths[i] = '/'.join(elements[j] for j in range(1, i + 1))

    return paths


def abbreviate(line: str) -> str:
    ignored = {"the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"}
    abbreviations = []

    for word in line.split('-'):
        if word.lower() not in ignored:
            abbreviations.append(word[0].upper())

    return ''.join(abbreviations)


def change_length_dashes_case(elements: list[str]) -> list[str]:
    for i in range(1, len(elements)):
        elements[i] = elements[i].upper()
        if len(elements[i]) > 30:
            elements[i] = abbreviate(elements[i])
        else:
            elements[i] = elements[i].replace('-', ' ')

    return elements


def wrap_url_elements(elements: list[str], paths: list[str]) -> list[str]:
    result = []
    end = '<span class="active">' + elements[-1] + '</span>'
    if len(elements) > 1:
        result.append('<a href="/">' + elements[0] + '</a>')
        result = result + ['<a href="/' + paths[i] + '/">' + elements[i] + '</a>' for i in range(1, len(elements) - 1)]
    result.append(end)
    return result


def generate_bc(url: str, separator: str) -> str:
    elements = split_url(url)

    elements = cut_endings(elements)
    elements = alterate_home(elements)
    paths = paths_gen(elements)
    elements = change_length_dashes_case(elements)

    breadcut = separator.join(wrap_url_elements(elements, paths))

    return breadcut


class TestGenerator(unittest.TestCase):

    def test_url_splitter(self):
        self.assertEqual(split_url('http://agcpartners.co.uk/index.html'),
                         ['http://agcpartners.co.uk', 'index.html'])
        self.assertEqual(split_url('mysite.com/pictures/holidays.html'),
                         ['mysite.com', 'pictures', 'holidays.html'])

    def test_abbreviate(self):
        self.assertEqual(abbreviate('very-long-url-to-make-a-silly-yet-meaningful-example'), 'VLUMSYME')

    def test_wrapper(self):
        elements = ['FIRST', 'SECOND', 'THIRD', 'FOURTH']
        paths = ['', 'second', 'second/third', '']
        self.assertEqual(' : '.join(wrap_url_elements(elements, paths)),
                         '<a href="/">FIRST</a> : <a href="/second/">SECOND</a> : <a href="/second/third/">THIRD</a> : '
                         '<span class="active">FOURTH</span>')

        elements = ['FIRST', 'SECOND']
        paths = ['', '']
        self.assertEqual(' : '.join(wrap_url_elements(elements, paths)),
                         '<a href="/">FIRST</a> : <span class="active">SECOND</span>')

        elements = ['FIRST']
        paths = ['']
        self.assertEqual(' : '.join(wrap_url_elements(elements, paths)),
                         '<span class="active">FIRST</span>')

    def test_generate_bc(self):
        self.assertEqual(generate_bc("mysite.com/pictures/holidays.html", " : "),
                         '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span '
                         'class="active">HOLIDAYS</span>')
        self.assertEqual(generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars", " / "),
                         '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>')
        self.assertEqual(generate_bc("www.microsoft.com/important/confidential/docs/index.htm#top", " * "),
                         '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * '
                         '<a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>')
        self.assertEqual(generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp", " > "),
                         '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example'
                         '/">VLUMSYME</a> > <span class="active">EXAMPLE</span>')
        self.assertEqual(generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi", " + "),
                         '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO '
                         'SORBI</span>')
        self.assertEqual(generate_bc("http://agcpartners.co.uk/index.html", " : "), '<span class="active">HOME</span>')


if __name__ == '__main__':
    unittest.main()



