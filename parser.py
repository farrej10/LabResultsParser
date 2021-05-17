#!/usr/bin/python
import sys
from enum import Enum
import pdb

resultvalue = {

    "NEGATIVE": -1.0,
    "POSITIVE": -2.0,
    "NIL": -1.0,
    "+": -2.0,
    "++": -2.0,
    "+++": -3.0,

}


class ResultFormat(Enum):
    C100 = "float"
    C200 = "float"
    A250 = "boolean"
    B250 = "nil_3plus"


class LaboratoryTestResult:
    def __init__(self, code, result, format, comment=None):
        self.code = code
        self.result = result
        self.format = format
        if comment != None:
            self.comment = comment
        else:
            self.comment = ""

    def __str__(self):
        return "\nLaboratoryTestResult(code: '{}', result: {}, format: '{}', comment: '{}')".format(self.code, self.result, self.format, self.comment)

    def __repr__(self):
        return "\nLaboratoryTestResult(code: {}, result: {}, format: {}, comment: {})".format(repr(self.code), repr(self.result), repr(self.format), repr(self.comment))

    def __eq__(self, other):
        return self.code == other.code and \
            self.result == other.result and \
            self.format == other.format and \
            self.comment == other.comment

    def add_comment(self, additional_comment):
        if self.comment != "":
            self.comment += "\n" + additional_comment
        else:
            self.comment = additional_comment


class Parser:
    def __init__(self, file_path):

        self.results = []
        try:
            f = open(file_path, 'r')
        except Exception as e:
            print(e)
            self.results = None
            return

        lines = f.readlines()
        f.close()

        index = "1"
        code = result = format = None

        for line in lines:

            split_line = line.split("|")

            if split_line[0] == "OBX":
                index = split_line[1]
                code = split_line[2]
                format = ResultFormat[code].value
                if format == "float":
                    result = float(split_line[3])
                else:
                    result = resultvalue[split_line[3]]
                self.results.append(LaboratoryTestResult(
                    code, result, format))
            if split_line[0] == "NTE":
                self.results[int(split_line[1])-1].add_comment(split_line[2])

    def mapped_results(self):

        return self.results


parser = Parser("lab2.txt")
print(parser.mapped_results())
