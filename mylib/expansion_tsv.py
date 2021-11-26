import os
import re
import csv
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from mylib import general_method as gm
from mylib.psiquic_class import PQdataList, PQdata
import glob

from copy import copy

def get_target_id(column_data: str, db_name: str):
    if db_name in column_data:
        return (
            column_data.split(db_name + ":")[1]
            .split("(")[0]
            .split("|")[0]
            .replace('"', "")
        )
    else:
        False


def has_bar_in_row(row):
    for column in row:
        if "|" in column:
            return True
    return False


def has_bar_in_row_list(row_list: list):
    for row in row_list:
        if has_bar_in_row(row):
            return True
    return False


def expansion_tsv_row(row_list: list):
    result_list = []
    for row in row_list:
        if has_bar_in_row(row):
            for i in range(len(row)):
                if "|" in row[i]:
                    row_a = copy(row)
                    row_a[i] = re.split("|", row[i])[0]
                    row_b = copy(row)
                    row_b[i] = re.split("[|\t$]", row[i])[1]
                    result_list.append(row_a)
                    result_list.append(row_b)
                    break
        else:
            result_list.append(row)

    if has_bar_in_row_list(result_list):
        result_list = expansion_tsv_row(result_list)
    return result_list


def list2tsv(data: list):
    result = ""
    for i in range(len(data)):
        if i != 0:
            result += "\t"

        if "psi-mi" in data[i]:
            result += data[i].split('"')[1].split(":")[1]
        elif ":" in data[i]:
            result += data[i].split(":")[1].split("(")[0]
        else:
            result += data[i]
    return result


# barで分けて展開したものをファイルの保存
def expansion_tsv(dirname):
    services_list = gm.list_serveice()
    column_label = gm.list_column_label()
    pqdatalist = PQdataList()

    for service in services_list:
        dir_name = dirname + "/" + service
        file_list = glob.glob(dir_name + "/*.tsv", recursive=True)
        for i in range(len(file_list)):
            os.mkdir(dirname + "/" + service + "/" + service + str(i))

            with open(dir_name + ".tsv") as f1:
                reader = csv.reader(f1, delimiter="\t")
                header = next(reader)
                for row in reader:
                    if has_bar_in_row(row):
                        # |で区切られてるrow dataを展開
                        row_list = expansion_tsv_row([row])
                        for devided_row in row_list:
                            pqdatalist.add(devided_row)
            # ファイルへの出力
            for i in range(len(pqdatalist.data)):
                pqdata = pqdatalist.data[i]
                f = open(dir_name + "_s" + str(i) + ".tsv", "w")
                f.write(list2tsv(column_label))
                f.close()
                for row in pqdata.row_list:
                    f = open(dir_name + "_s" + str(i) + ".tsv", "a")
                    f.write("\n" + list2tsv(row))
                    f.close()
                print(pqdata.id_set)
                print("created ", dir_name + "_s" + str(i) + ".tsv")


if __name__ == "__main__":
    dirname = "test_data/"
    # dirname = "data/"
    # main1(dirname)
    expansion_tsv(dirname)
