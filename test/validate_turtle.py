import csv
import glob
import os
import re
import shutil
import sys

sys.path.append('/Users/kouiti/localfile/glycovid_PSIQUIC')
from mylib import general_method as gm


def toURI(text:str, prefix) -> str:
    if text[0:1] == "<" and text[-1:] == ">":
        return text
    else:
        for key in prefix:
            if re.match(r"^"+key, text):
                text = text.replace(key, prefix[key][:-1], 1)
                text += ">"
                return text
    print("error: in toURI: ", text)
    sys.exit()

def validata_uri(uri: str, uri_patterns: list) -> bool:
    isCorrect = False
    for uri_pattern in uri_patterns:
        if re.match(uri_pattern, uri):
            isCorrect = True
            # print(uri)
            # uri_patterns.remove(uri_pattern)
            # return isCorrect
    if not isCorrect:
        # print("Error wrong uri :", uri)
        if uri != "<http://rdf.glycoinfo.org/dbid/taxonomy/-2>"\
                and not re.match(r"<http://rdf.glycoinfo.org/dbid/taxonomy/-1>", uri)\
                and not re.match(r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/uniprot\/[A-Z0-9]+#PRO_\d+>", uri)\
                and not re.match(r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/uniprot\/[A-Z0-9]+-\d+>", uri)\
                and not re.match(r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/pubmed\/unassigned\d+>", uri)\
                and not re.match(r"<http:\/\/rdf\.glycoinfo\.org\/dbid\/mpid\/MPIDB-INT-\d{3,4}>", uri):
            print("failed in ", uri)
            sys.exit()
    return isCorrect


def validata_turtle(file: str, uri_pattern: list) -> None:
    with open(file) as f:
        prefix = dict()
        for line in f:
            if line == "\n":
                break
            cols = line.split(" ")
            prefix[cols[1]] = cols[2]

    with open(file) as f:
        isRdf = False
        for line in f:
            if line == "\n":
                isRdf = True
                continue
            if isRdf:
                col = re.split(r"\s+", line)
                if(col[-1] == ""):
                    col.pop(-1)
                if col[-1][-1] == ",":
                    col[-1] = col[-1][0:-1]
                    col.append(",")
                if len(col) == 4:
                    if col[0] != "":
                        uri = toURI(col[0], prefix)
                        validata_uri(uri, uri_pattern)
                        uri = toURI(col[2], prefix)
                        validata_uri(uri, uri_pattern)
                    else:
                        uri = toURI(col[2], prefix)
                        validata_uri(uri, uri_pattern)
                # po
                elif len(col) == 3:
                    uri = toURI(col[1], prefix)
                else:
                    uri = toURI(line[0], prefix)


def main():
    services_list = gm.list_serveice()
    uri_pattern = list()
    with open("uri_list/object_uri_list2.csv") as f1:
        reader = csv.reader(f1, delimiter="\t")
        for row in reader:
            # uri_pattern.append("<" + row[1] + ".+" + ">")
            uri_pattern.append("<" + row[1] + row[2] + ">")

    for service in services_list:
        dir_list = glob.glob("turtle/" + service + "/*.ttl", recursive=True)
        for i in range(len(dir_list)):
            print(dir_list[i], "checking ...")
            validata_turtle(dir_list[i], uri_pattern)


if __name__ == "__main__":
    main()
