# You have a browser of one tab where you start on the homepage and you can visit another url,
# get back in the history number of steps or move forward in the history number of steps.
#
# Implement the BrowserHistory class:
#
# BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
# void visit(string url) Visits url from the current page. It clears up all the forward history.
# string back(int steps) Move steps back in history. If you can only return x steps in the history
# and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
# string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and
# steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


import unittest


# two stacks solution:
class BrowserHistory:

    def __init__(self, homepage: str):
        self.forward_history = [homepage]
        self.backward_history = []

    def visit(self, url: str) -> None:
        self.forward_history.append(url)
        self.backward_history = []

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.forward_history) == 1:
                break
            self.backward_history.append(self.forward_history.pop())
        return self.forward_history[-1]

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.backward_history:
                break
            self.forward_history.append(self.backward_history.pop())
        return self.forward_history[-1]


# one list solution:
class BrowserHistoryAlternative:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr_index = 0

    def visit(self, url: str) -> None:
        if self.curr_index < len(self.history) - 1:
            del self.history[self.curr_index + 1:]
        self.curr_index += 1
        self.history.append(url)

    def back(self, steps: int) -> str:
        self.curr_index = max(0, self.curr_index - steps)
        return self.history[self.curr_index]

    def forward(self, steps: int) -> str:
        self.curr_index = min(len(self.history) - 1, self.curr_index + steps)
        return self.history[self.curr_index]


class TestBrowserHistory(unittest.TestCase):
    def test_browser_history(self):
        history = BrowserHistory('homepage.com')
        history.visit('page1.com')
        history.visit('page2.com')
        history.visit('page3.com')
        history.visit('page4.com')
        history.visit('page5.com')
        self.assertEqual('page4.com', history.back(1))
        self.assertEqual('page2.com', history.back(2))
        self.assertEqual('page3.com', history.forward(1))
        self.assertEqual('page5.com', history.forward(50))
        self.assertEqual('homepage.com', history.back(150))
        history.visit('page0.com')
        self.assertEqual('homepage.com', history.back(150))
        self.assertEqual('page0.com', history.forward(150))

    def test_browser_history_alternative(self):
        history = BrowserHistoryAlternative('homepage.com')
        history.visit('page1.com')
        history.visit('page2.com')
        history.visit('page3.com')
        history.visit('page4.com')
        history.visit('page5.com')
        self.assertEqual('page4.com', history.back(1))
        self.assertEqual('page2.com', history.back(2))
        self.assertEqual('page3.com', history.forward(1))
        self.assertEqual('page5.com', history.forward(50))
        self.assertEqual('homepage.com', history.back(150))
        history.visit('page0.com')
        self.assertEqual('homepage.com', history.back(150))
        self.assertEqual('page0.com', history.forward(150))

