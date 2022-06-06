import unittest
import filecmp
import os


class MyTestCase(unittest.TestCase):
    def test_details(self):
        file1 = "C:/Users/HP/nlptools/output.json"
        file2 = "C:/Users/HP/nlptools/check_output.json"
        os.system("python -Wignore extract_details.py")
        if filecmp.cmp(file1, file2):
            print(str(file1) + " is correct")
        else:
            print(str(file1) + " is incorrect")
        print("--------------------------------------------------------------------------------")


if __name__ == '__main__':
    unittest.main()
