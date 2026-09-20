import unittest

from grades import average_grade, letter_grade


class GradeTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average_grade([80, 90, 100]), 90)

    def test_rejects_out_of_range_score(self):
        for scores in ([101], [-1, 75]):
            with self.subTest(scores=scores):
                with self.assertRaisesRegex(ValueError, "between 0 and 100"):
                    average_grade(scores)

    def test_rejects_empty_scores(self):
        with self.assertRaisesRegex(ValueError, "at least one"):
            average_grade([])

    def test_grade_boundaries(self):
        for average, expected in [(89.9, "B"), (90, "A"), (59.9, "F"), (60, "D")]:
            with self.subTest(average=average):
                self.assertEqual(letter_grade(average), expected)


if __name__ == "__main__":
    unittest.main()
