import os
import re
import csv
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from mylib import general_method as gm
from mylib.psiquic_class import PQdataList, PQdata
import glob
import expantion_tsv_row from expantion_tsv

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
def list_dbid(dirname):
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






if __name__ == "__main__":
    dirname = "test_data/"
    list_dbid(dirname)
