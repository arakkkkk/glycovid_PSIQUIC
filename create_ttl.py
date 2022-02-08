import csv
import glob
import os
import re
import shutil
import sys
from copy import copy

import rdflib
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, XSD

from mylib import general_method as gm
from mylib.expansion_tsv import expansion_tsv_row


def treat_data(column_data: str):
    column_data = re.sub('[\"\']', "", column_data)
    ## protein ontology:PR(000027395)
    column_data = re.sub(r"PR\((?P<id>(.*))\)", r"\g<id>", column_data)
    # psi-mi:ENSG00000109819.(display_long)         intact2.tsv
    column_data = re.sub(r"doi:https://doi\.org/(?P<id>(.+))", r"doi:\g<id>", column_data)
    # doi:https://doi.org/10.1038/nature12162
    column_data = re.sub(r"ensembl:(?P<id>(.+?))\.", r"ensembl:\g<id>", column_data)

    column_data = re.sub(r"\(.*\)", "", column_data)

    db_name = column_data.split(":")[-2]
    identifier = column_data.split(":")[-1]\
                            .replace(" ", "-")\

    ## MI_MI-0915　→　MI_0915
    identifier = re.sub(r"MI-(?P<id>(\d*))", r"\g<id>", identifier)
    # データベース固有のデータ変更
    ## P39060-PRO_000005794 → P39060#PRO_000005794
    if db_name == "uniprotkb":
        identifier = re.sub(r"(?P<uniprotid>(.+?))-PRO_(?P<proid>(.+))", r"\g<uniprotid>#PRO_\g<proid>", identifier)

    # 余分な文字列データの消去
    # identifier = re.sub(r"\(.*\)", "", identifier)
    # print(column_data)
    return db_name.lower(), identifier

def treat_sub_dbname(column: str):
    column = column.lower()
    column = column.split("/")[-1]
    column = column.replace(" ", "-")
    return column

def create_subject_uri(column1: str, column2: str):
    # subject
    # interactor_ab = rdflib.Namespace("https://identifiers.org/matrixdb.association:")
    interactor_ab = rdflib.Namespace("https://rdf.glycoinfo.org/matrixdb.association:")
    # issue uriの正当性の確認文字列チェック
    db_name1, identifier1 = treat_data(column1)
    db_name2, identifier2 = treat_data(column2)
    db_name1 = treat_sub_dbname(db_name1)
    db_name2 = treat_sub_dbname(db_name2)
    Interactor_ab = URIRef(
            interactor_ab +
            db_name1 +"_" +identifier1 +
            "__" +
            db_name2 +"_" +identifier2
            )
    return Interactor_ab


def create_object_uri(column: str, db_list: dict):
    #############################
    # uri definition
    #############################

    db_name, identifier = treat_data(column)
    try:
        createdURI = URIRef(db_list[db_name] + identifier)
        return createdURI
    except:
        print(db_name, identifier)
        sys.exit()



def except_columns(row):
    except_list = [2,3,4,5,10,14]
    for i in range(len(row)):
        if i in except_list:
            row[i] = ""
    return row


def create_ttl(dir_name, file_name, service):
    # print("create", file_name + ".ttl", "from", dir_name)
    g = Graph()
    #############################
    # predicate
    #############################
    detected_by = URIRef("http://www.bioassayontology.org/bao#BAO_0002875")
    # author_is = URIRef("http://www.biopax.org/release/biopax-level3.owl#author")
    pub_id = URIRef("http://purl.obolibrary.org/obo/IAO_0000119")

    has_interaction_type_obo = URIRef("http://purl.obolibrary.org/obo/INO_0000154")
    has_interaction_type_bp = URIRef(
        "http://www.biopax.org/release/biopax-level3.owl#interactionType"
    )
    souce_db = URIRef("http://purl.org/dc/elements/1.1/source")
    # has_interaction_id_bao = URIRef("http://www.bioassayontology.org/bao#BAO_0000383")
    # has_interaction_id_obo = URIRef("http://purl.obolibrary.org/obo/id")
    # has_interaction_id_lim = URIRef(
    #     "http://www.linkedmodel.org/schema/vaem#hasIdentifier"
    # )
    has_interaction_id = URIRef("http://purl.org/dc/elements/1.1/identifier")
    # data_xref_obo = URIRef("obolnOwl:hasDbXref")

    # data_xref_bp = URIRef("http://www.biopax.org/release/biopax-level3.owl#xref")
    # interaction_annotate = URIRef("http://www.w3.org/2004/02/skos/core#note")
    organizm = URIRef("http://semanticscience.org/resource/SIO_000253")
    in_vitro = URIRef("http://www.bioassayontosiyousuru.org/bao#BAO_0020008")
    chemical_synthesis = URIRef("http://semanticscience.org/resource/SIO_000559")
    # interaction_param_pos = URIRef(
    #     "http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#hasParameters"
    # )

    has_interactorA = URIRef("http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A")
    has_interactorB = URIRef("http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B")

    ############################
    # code
    ############################

    # object
    db_list = dict()
    # key = dbname, value = uriの辞書を作成
    with open("uri_list/object_uri_list2.csv") as f1:
        reader = csv.reader(f1, delimiter="\t")
        for row in reader:
            db_list[row[0]] = rdflib.Namespace(row[1])
            if " " in row[0]:
                db_list[row[0].replace(" ","")] = rdflib.Namespace(row[1])

    with open(dir_name) as f1:
        reader = csv.reader(f1, delimiter="\t")
        next(reader)
        for row_bef in reader:
            row_bef = except_columns(row_bef)
            row_list = expansion_tsv_row([row_bef])
            for row in row_list:

                if row[0] == "-" or row[1] == "-" or row[0] == "" or row[1] == "":
                    continue

                Interactor_ab = create_subject_uri(row[0], row[1])

                Interactor_a = create_object_uri(row[0], db_list)
                g.add((Interactor_ab, has_interactorA, Interactor_a))
                Interactor_b = create_object_uri(row[1], db_list)
                g.add((Interactor_ab, has_interactorB, Interactor_b))

                if row[6] != "-" and row[6] != "":
                    Detection_method = create_object_uri(row[6], db_list)
                    g.add((Interactor_ab, detected_by, Detection_method))

                # if row[7] != "-" and row[7] != "":
                #     First_aouthor = Literal(row[7], datatype=XSD.string)
                #     g.add((Interactor_ab, author_is, First_aouthor))

                if row[8] != "-" and row[8] != "":
                    Publication_id = create_object_uri(row[8], db_list)
                    g.add((Interactor_ab, pub_id, Publication_id))

                if row[9] != "-" and row[9] != "":
                    Taxon_id = create_object_uri(row[9], db_list)
                    # taxid:-2(chemical synthesis), taxid:-1(in vitro)
                    if(Taxon_id == "-1"):
                        g.add((Interactor_ab, organizm, in_vitro))
                    elif(Taxon_id == "-2"):
                        g.add((Interactor_ab, organizm, chemical_synthesis))
                    else:
                        g.add((Interactor_ab, organizm, Taxon_id))

                if row[11] != "-" and row[11] != "":
                    Interaction_type = create_object_uri(row[11], db_list)
                    g.add((Interactor_ab, has_interaction_type_bp, Interaction_type))
                    g.add((Interactor_ab, has_interaction_type_obo, Interaction_type))

                if row[12] != "-" and row[12] != "":
                    Source_database = create_object_uri(row[12], db_list)
                    g.add((Interactor_ab, souce_db, Source_database))

                if row[13] != "-" and row[13] != "":
                    Interaction_id = create_object_uri(row[13], db_list)
                    g.add((Interactor_ab, has_interaction_id, Interaction_id))
                    # g.add((Interactor_ab, has_interaction_id_bao, Interaction_id))
                    # g.add((Interactor_ab, has_interaction_id_lim, Interaction_id))
                    # g.add((Interactor_ab, has_interaction_id_obo, Interaction_id))


        g.serialize(
            destination="turtle/" + service + "/" + file_name + ".ttl",
            format="turtle",
        )


def main(dir_name: str):
    services_list = gm.list_serveice()
    for service in services_list:
        try:
            shutil.rmtree("turtle/" + service)
        except:
            pass
        try:
            os.mkdir("turtle/" + service)
        except:
            pass
        dir_list = glob.glob(dir_name + service + "/*.tsv", recursive=True)
        for i in range(len(dir_list)):
            print("... create ttl from", dir_list[i], "\t", i+1, "/", len(dir_list))
            create_ttl(dir_list[i], service + str(i), service)


if __name__ == "__main__":
    print("start create ttl")
    dir_name = "data/"
    main(dir_name)
