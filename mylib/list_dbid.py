import os
import re
import csv
import sys
from copy import copy
import shutil
import glob

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))


def get_column_ids(reader):
    num_column = len(gm.list_column_label())
    id_list = [[] for i in range(num_column * 2)]
    for row in reader:
        for i in range(num_column):
            for data in row[i].split("|"):
                data_id = data.split(":")[0]
                if data_id not in id_list[i] and i != 7:
                    id_list[i * 2 - 1].append(data_id)
                    id_list[i * 2].append(data)
    return id_list


def join_id_list(id_list1, id_list2):
    for i in range(int((len(id_list2) - 1) / 2)):
        for j in range(len(id_list2[i * 2 - 1])):
            if id_list2[i * 2 - 1][j] not in id_list1[i * 2 - 1]:
                id_list1[i * 2 - 1].append(id_list2[i * 2 - 1][j])
                id_list1[i * 2].append(id_list2[i * 2][j])
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
def list_dbid(dirname):
    services_list = gm.list_serveice()
    column_label = gm.list_column_label()
    whole_id_list = [[] for _ in range(len(column_label) * 2)]
    for service in services_list:
        service_id_list = [[] for _ in range(len(column_label) * 2)]
        path = dirname + service + "/*.tsv"
        source_dir_name_list = glob.glob(path)
        if len(source_dir_name_list) == 0:
            print(path, "not defined")
            return
        try:
            shutil.rmtree(dirname + "/" + service + "/info")
        except:
            pass
        try:
            os.mkdir(dirname + "/" + service + "/info")
        except:
            pass
        out_dir_name = dirname + "/" + service + "/info/" + service + "_list_id.tsv"
        for i in range(len(source_dir_name_list)):
            print(source_dir_name_list[i], "reading ..")
            source_dir_name = source_dir_name_list[i]
            with open(source_dir_name) as f1:
                reader = csv.reader(f1, delimiter="\t")
                next(reader)
                id_list = get_column_ids(reader)
                join_id_list(service_id_list, id_list)
        write_id_list(service_id_list, out_dir_name)
        whole_id_list = join_id_list(whole_id_list, service_id_list)
    write_id_list(whole_id_list, dirname + "/whole_id_list.tsv")


def all_dbid_by_wholelist(dirname):
    dbid_list = []
    file_path = dirname + "/whole_id_list.tsv"
    black_list = [1, 2, 3, 4, 5, 6, 15]
    # black_list = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    with open(file_path) as f1:
        reader = csv.reader(f1, delimiter="\t")
        j = 0
        for row in reader:
            j += 1
            if j not in black_list:
                i = 0
                for r in row:
                    i += 1
                    if i != 1:
                        if r not in dbid_list:
                            dbid_list.append(r)
    for t in dbid_list:
        if t == "-":
            continue
        cont = True
        services_list = gm.list_serveice()
        for service in services_list:
            path = dirname + service + "/*.tsv"
            source_dir_name_list = glob.glob(path)
            for i in range(len(source_dir_name_list)):
                source_dir_name = source_dir_name_list[i]
                with open(source_dir_name) as f1:
                    reader = csv.reader(f1, delimiter="\t")
                    for row in reader:
                        for r in row:
                            if t in r:
                                print(t, r)
                                cont = False
                                break
                        if not cont:
                            break

                if not cont:
                    break
            if not cont:
                break


if __name__ == "__main__":
    from mylib.psiquic_class import PQdataList, PQdata
    from mylib import general_method as gm

    dirname = "data/"
    list_dbid(dirname)
    # all_dbid_by_wholelist(dirname)
