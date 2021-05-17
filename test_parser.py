import unittest
from parser import Parser, LaboratoryTestResult


class TestParser(unittest.TestCase):

    # tests that mapped_results returns correct array
    def test_mapped_results(self):

        test_result = []
        test_result.append(LaboratoryTestResult(
            "C100", 20.0, "float", "Comment for C100 result"))

        test_parser = Parser("")
        self.assertEqual(test_parser.mapped_results(), None)
        test_parser = Parser("lab1.txt")
        self.assertEqual(test_parser.mapped_results(), test_result)

        test_result = []
        test_result.append(LaboratoryTestResult(
            "A250", -1.0, "boolean", "Comment for NEGATIVE result"))
        test_result.append(LaboratoryTestResult(
            "B250", -2.0, "nil_3plus", "Comment 1 for ++ result\nComment 2 for ++ result"))
        test_parser = Parser("lab2.txt")
        self.assertEqual(test_parser.mapped_results(), test_result)

    # runs a tests the parsing for all the possible combinations of test results
    def test_init(self):
        test_parser = Parser("test.txt")
        test_result = []
        # these are the expected results from the parsing
        test_result.append(LaboratoryTestResult(
            "A250", -1.0, "boolean", "Comment for NEGATIVE result"))
        test_result.append(LaboratoryTestResult(
            "A250", -2.0, "boolean", "Comment for POSITIVE result"))
        test_result.append(LaboratoryTestResult(
            "B250", -3.0, "nil_3plus", "Comment 1\nComment 2"))
        test_result.append(LaboratoryTestResult(
            "B250", -2.0, "nil_3plus", "Comment 1\nComment 2"))
        test_result.append(LaboratoryTestResult(
            "B250", -2.0, "nil_3plus", "Comment 1\nComment 2"))
        test_result.append(LaboratoryTestResult(
            "B250", -1.0, "nil_3plus", "Comment 1\nComment 2"))
        test_result.append(LaboratoryTestResult(
            "C100", 20.0, "float", "Comment for C100 result"))
        test_result.append(LaboratoryTestResult(
            "C100", -20.0, "float", "Comment for C100 result"))
        test_result.append(LaboratoryTestResult(
            "C200", 20.0, "float", "Comment for C200 result"))
        test_result.append(LaboratoryTestResult(
            "C200", 20, "float", "Comment for C200 result"))
        test_result.append(LaboratoryTestResult(
            "C200", -20.0, "float", "Comment for C200 result"))
        self.assertEqual(test_parser.mapped_results(), test_result)


class TestLaboratoryTestResult(unittest.TestCase):

    def test_init(self):
        test_result = LaboratoryTestResult("C100", 20.0, "float")

        self.assertEqual(test_result.code, "C100")
        self.assertEqual(test_result.result, 20.0)
        self.assertEqual(test_result.format, "float")
        self.assertEqual(test_result.comment, "")

    def test_add_comment(self):
        test_result = LaboratoryTestResult("C100", 20.0, "float")
        self.assertEqual(test_result.comment, "")
        test_result.add_comment("Comment 1 for ++ result")
        self.assertEqual(test_result.comment, "Comment 1 for ++ result")
        test_result.add_comment("Comment 2 for ++ result")
        self.assertEqual(test_result.comment,
                         "Comment 1 for ++ result\nComment 2 for ++ result")


if __name__ == '__main__':
    unittest.main()
