import csv
import rdflib
from rdflib import Graph
from rdflib import Namespace
from rdflib.namespace import RDF, RDFS
from rdflib.namespace import XSD
from rdflib import URIRef, Literal
from log.log import init_log, log
from copy import copy
import re
import glob
from lib import general_method as gm
import shutil
import os
from mylib.expansion_tsv import expansion_tsv_row


def treat_data(column_data: str):
    column_data = column_data.split('"')[1]
    db_name = column_data.split(":")[0]
    identifier = (
        column_data.split(":")[1].split("(")[0].replace(" ", "-").replace("_", "-")
    )
    return db_name, identifier


def create_subject_uri(column1: str, column2: str):
    # subject
    interactor_ab = rdflib.Namespace("https://identifiers.org/matrixdb.association:")
    db_list = dict()
    with open("turtle/subject_url_list.csv") as f1:
        reader = csv.reader(f1, delimiter=",")
        for row in reader:
            db_list[row[0]] = rdflib.Namespace(row[1])
    db_name1, identifier1 = treat_data(column1)
    db_name2, identifier2 = treat_data(column2)
    # issue uriの正当性の確認文字列チェック
    # error handling
    Interactor_ab = URIRef(interactor_ab + column1.lower() + "__" + column2.lower())
    return Interactor_ab


def create_object_uri(column: str):
    #############################
    # uri definition
    #############################
    # object
    db_list = dict()
    with open("turtle/object_url_list.csv") as f1:
        reader = csv.reader(f1, delimiter=",")
        for row in reader:
            db_list[row[0]] = rdflib.Namespace(row[1])

    db_name, identifier = treat_data(column)
    createdURI = URIRef(db_list(db_name) + identifier)
    # error handling
    return createdURI


def create_ttl(dir_name, file_name, service):
    print("create", file_name + ".ttl", "from", dir_name)
    g = Graph()
    #############################
    # predicate
    #############################
    detected_by = URIRef("http://www.bioassayontology.org/bao#BAO_0002875")
    author_is = URIRef("http://www.biopax.org/release/biopax-level3.owl#author")
    pub_id = URIRef("http://purl.obolibrary.org/obo/IAO_0000119")

    has_interaction_type_obo = URIRef("http://purl.obolibrary.org/obo/INO_0000154")
    has_interaction_type_bp = URIRef(
        "http://www.biopax.org/release/biopax-level3.owl#interactionType"
    )
    souce_db = URIRef("http://purl.org/dc/elements/1.1/source")
    has_interaction_id_bao = URIRef("http://www.bioassayontology.org/bao#BAO_0000383")
    has_interaction_id_obo = URIRef("http://purl.obolibrary.org/obo/id")
    has_interaction_id_lim = URIRef(
        "http://www.linkedmodel.org/schema/vaem#hasIdentifier"
    )
    data_xref_obo = URIRef("obolnOwl:hasDbXref")

    data_xref_bp = URIRef("http://www.biopax.org/release/biopax-level3.owl#xref")
    interaction_annotate = URIRef("http://www.w3.org/2004/02/skos/core#note")
    organizm = URIRef("http://www.biopax.org/release/biopax-level3.owl#organism")
    interaction_param_pos = URIRef(
        "http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#hasParameters"
    )

    ############################
    # code
    ############################

    with open(dir_name) as f1:
        reader = csv.reader(f1, delimiter="\t")
        header = next(reader)
        progress = 0
        for row_bef in reader:
            row_list = expansion_tsv_row([row_bef])

            for row in row_list:
                progress += 1
                init_log("progress", str(progress))
                # カラムデータの取得、バリデーション
                Interactor_ab = create_subject_uri(row[0], row[1])
                Detection_method = create_object_uri(row[6])
                First_aouthor = Literal(row[7], datatype=XSD.string)
                Publication_id = create_object_uri(row[8])
                Interaction_type = create_object_uri(row[11])
                Source_database = create_object_uri(row[12])
                Interaction_id = create_object_uri(row[13])
                Taxon_id = create_object_uri(row[9])

                # URIの作成

                # RDFの作成
                g.add((Interactor_ab, detected_by, Detection_method))
                g.add((Interactor_ab, author_is, First_aouthor))
                g.add((First_aouthor, pub_id, Publication_id))
                g.add((Interactor_ab, has_interaction_type_bp, Interaction_type))
                g.add((Interactor_ab, has_interaction_type_obo, Interaction_type))
                g.add((Interactor_ab, souce_db, Source_database))
                g.add((Interactor_ab, has_interaction_id_bao, Interaction_id))
                g.add((Interactor_ab, has_interaction_id_lim, Interaction_id))
                g.add((Interactor_ab, has_interaction_id_obo, Interaction_id))
                g.add((Interactor_ab, organizm, Taxon_id))

        g.serialize(
            destination="turtle/" + service + "/rdf_" + file_name + ".ttl",
            format="turtle",
        )


def main():
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
        dir_list = glob.glob("test_data/" + service + "/*.tsv", recursive=True)
        for i in range(len(dir_list)):
            create_ttl(dir_list[i], service + str(i), service)


if __name__ == "__main__":
    main()
