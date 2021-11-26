import os
import re
import csv
from log.log import init_log, log
from lib import general_method as gm
from lib.psiquic_class import PQdataList, PQdata
import glob

from copy import copy


def get_column_ids(reader):
    num_column = len(gm.list_column_label())
    id_list = [[] for i in range(num_column)]
    for row in reader:
        for i in range(num_column):
            for data in row[i].split("|"):
                data_id = data.split(":")[0]
                if data_id not in id_list[i] and i != 7:
                    id_list[i].append(data_id)
    return id_list

    # row_list = expansion_tsv_row([row])
    # for devided_row in row_list:
    #     pqdatalist.add(devided_row)


def join_id_list(id_list1, id_list2):
    for i in range(len(id_list2)):
        for j in range(len(id_list2[i])):
            if id_list2[i][j] not in id_list1[i]:
                id_list1[i].append(id_list2[i][j])
    return id_list1


def write_id_list(id_list, out_dir_name):
    column_label = gm.list_column_label()
    text = ""
    for i in range(len(column_label)):
        text += column_label[i]
        for cid in id_list[i]:
            text += "\t" + cid
        text += "\n"

    f = open(out_dir_name, "w")
    f.write(text)
    f.close()


# id listを取得
def main1(dirname):
    services_list = gm.list_serveice()
    column_label = gm.list_column_label()
    whole_id_list = [[] for _ in range(len(column_label))]
    for service in services_list:
        service_id_list = []
        source_dir_name_list = glob.glob(
            dirname + service + "/" + service + "*.tsv", recursive=True
        )
        os.mkdir(dirname + "/" + service + "/info")
        out_dir_name = dirname + "/" + service + "/info/" + service + "_list_id.tsv"
        for i in range(len(source_dir_name_list)):
            source_dir_name = source_dir_name_list[i]
            try:
                with open(source_dir_name) as f1:
                    reader = csv.reader(f1, delimiter="\t")
                    next(reader)
                    id_list = get_column_ids(reader)
                    service_id_list = join_id_list(service_id_list, id_list)
                    write_id_list(id_list, out_dir_name)
            except:
                print("file not found ", source_dir_name)
        write_id_list(service_id_list, out_dir_name)
    write_id_list(whole_id_list, dirname + "/whole_id_list.tsv")


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
def main2(dirname):
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
    main2(dirname)
