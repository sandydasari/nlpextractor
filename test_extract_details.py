import unittest
import json
import re
with open("output.json") as file:
    data_dict = json.load(file)
print(data_dict)


class MyTestCase(unittest.TestCase):
    def test_result(self):
        result=data_dict["Covid-Result"]
        if type(result)!=str:
            raise TypeError("result must be a string")
        self.assertEqual(result=="Positive" or "Negative", True)

    def test_date(self):
        date=data_dict["DATE"]
        if not re.match('^ (?:(((Jan(uary)? | Ma(r(ch)? | y) | Jul(y)? | Aug(ust)? | Oct(ober)? | Dec(ember)?)\ 31) | ((Jan(uary)? | Ma(r(ch)? | y) | Apr(il)? | Ju((ly?) | (ne?)) | Aug(ust)? | Oct(ober)? | (Sept | Nov | Dec)(ember)?)\ (0?[1-9] | ([12]\d) | 30)) | (Feb(ruary)?\ (0?[1-9] | 1\d | 2[0-8] | (29(?=, \ ((1[6-9] |[2-9]\d)(0[48] | [2468][048] | [13579][26]) | ((16 | [2468][048] |[3579][26])00)))))))\, \ ((1[6 - 9] | [2 - 9]\d)\d{2}))', date):
            return False
        return True

        #self.assertEqual(data_dict["DATE"] == , True)
    def test_person(self):
        username=data_dict["PERSON"]
        minlen=3
        if type(username) != str:
            raise TypeError("username must be a string")
        if minlen < 1:
            raise ValueError("minlen must be at least 1")

        # Usernames can't be shorter than minlen
        if len(username) < minlen:
            return False
        # Usernames can only use letters, numbers, dots and underscores
        if not re.match('^[a-z0-9._]*$', username):
            return False
        # Usernames can't begin with a number
        if username[0].isnumeric():
            return False
        return True

    def test_sampleID(self):
        sampleID=data_dict["PATIENT ID"]
        if not re.match('^[a-zA-Z0-9\.\-+_]{14}',sampleID):
            return False
        return True

if __name__ == '__main__':
    unittest.main()
