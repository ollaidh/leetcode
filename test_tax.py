import unittest


# split income into parts corresponding with tax categories:
def split_income_by_tax_categories(income: int, tax_rates: dict[str, int]) -> dict[str, int]:
    income_tax_categorized = {}
    start = 0
    for key, _ in tax_rates.items():
        if key.startswith(">"):
            income_tax_categorized[key] = income
            break
        income_tax_categorized[key] = min((int(key) - start), income)
        income -= income_tax_categorized[key]
        start = int(key)
    return income_tax_categorized


def calc_tax(income: int, tax_rates: dict[str, int]):
    tax_pay = 0
    income_by_tax_cat = split_income_by_tax_categories(income, tax_rates)
    for key, value in income_by_tax_cat.items():
        tax_pay += value * tax_rates[key] * 0.01
    return tax_pay


class TestTax(unittest.TestCase):
    def test_split_income_by_tax_categories(self):
        tax_cat = {"10000": 0, "40000": 20, "100000": 40, ">100000": 45}

        income1 = 120000
        expected1 = {"10000": 10000, "40000": 30000, "100000": 60000, ">100000": 20000}
        self.assertEqual(expected1, split_income_by_tax_categories(income1, tax_cat))

        income2 = 5000
        expected2 = {"10000": 5000, "40000": 0, "100000": 0, ">100000": 0}
        self.assertEqual(expected2, split_income_by_tax_categories(income2, tax_cat))

        income3 = 55000
        expected3 = {"10000": 10000, "40000": 30000, "100000": 15000, ">100000": 0}
        self.assertEqual(expected3, split_income_by_tax_categories(income3, tax_cat))

    def test_calc_tax(self):
        tax_cat = {"20000": 0, "40000": 20, "100000": 40, ">100000": 50}

        tax_pay1 = calc_tax(50000, tax_cat)
        self.assertEqual(8000, tax_pay1)

        tax_pay2 = calc_tax(140000, tax_cat)
        self.assertEqual(48000, tax_pay2)

        tax_pay3 = calc_tax(5000, tax_cat)
        self.assertEqual(0, tax_pay3)


if __name__ == '__main__':
    unittest.main()
