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


def get_target_id(column_data: str):
    result = {"db": "", "id": ""}
    column_data = column_data.split('"')[1]
    result["db"] = column_data.split(":")[0]
    result["id"] = column_data.split(":")[1]\
    .split("(")[0]\
    .replace(" ", "-")\
    .replace("_", "-")\
    return (
            result
    )


def create_ttl(dir_name, file_name, service):
    print("create", file_name + ".ttl", "from", dir_name)
    g = Graph()
    # predicate
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
    ##########################################
    data_xref_obo = URIRef("obolnOwl:hasDbXref")

    data_xref_bp = URIRef("http://www.biopax.org/release/biopax-level3.owl#xref")
    interaction_annotate = URIRef("http://www.w3.org/2004/02/skos/core#note")
    organizm = URIRef("http://www.biopax.org/release/biopax-level3.owl#organism")
    interaction_param_pos = URIRef(
        "http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#hasParameters"
    )
    # interaction_param_bm = URIRef(
    # "http://www.biomodels.net/kisao/KISAO#KISAO_0000259 (has parameter) "
    # )

    # subject
    interactor_ab = rdflib.Namespace("https://identifiers.org/matrixdb.association:")

    # object
    obo = rdflib.Namespace("http://purl.obolibrary.org/obo/")
    publication_id = rdflib.Namespace("https://identifiers.org/pubmed:")
    intact = rdflib.Namespace("https://identifiers.org/intact:")
    taxon_id = rdflib.Namespace("http://identifiers.org/taxonomy/")
    taxon_obo = rdflib.Namespace("http://purl.obolibrary.org/obo/NCBITaxon_")
    interaction_xref = rdflib.Namespace("https://identifiers.org/pdb:")

    with open(dir_name) as f1:
        reader = csv.reader(f1, delimiter="\t")
        header = next(reader)
        progress = 0
        for row_bef in reader:
            if has_bar_in_row(row_bef):
                # |で区切られてるrow dataを展開
                row_list = expansion_tsv_row([row_bef])
            else:
                row_list = [row_bef]

            for row in row_list:
                progress += 1
                init_log("progress", str(progress))
                # カラムデータの取得、バリデーション
                Dinteractor_a = get_target_id(row[0])
                Dinteractor_b = get_target_id(row[1])
                Ddetection_method = get_target_id(row[6])
                Dpub_id = get_target_id(row[8])
                Dinteraction_type = get_target_id(row[11])
                Dsource_database = get_target_id(row[12])
                Dinteraction_id = get_target_id(row[13])
                Dtaxon_id = get_target_id(row[9])
                if (
                    not Dinteractor_a
                    or not Dinteractor_b
                    or not Ddetection_method
                    or not Dpub_id
                    or not Dinteraction_type
                    or not Dsource_database
                    or not Dinteraction_id
                    or not Dtaxon_id
                ):
                    print("failed: ", row[0], row[1])
                    log("filed_list", str(reader))
                    continue

                # URIの作成
                Interactor_ab = URIRef(
                    interactor_ab + Dinteractor_a.lower() + "__" + Dinteractor_b.lower()
                )
                Detection_method = URIRef(obo + Ddetection_method)
                First_aouthor = Literal(row[7], datatype=XSD.string)
                Publication_id = URIRef(publication_id + pub_id)
                Interaction_type = URIRef(obo + Dinteraction_type)
                Source_database = URIRef(obo + Dsource_database)
                Interaction_id = URIRef(intact + Dinteraction_id)
                # Confidence value
                # Expansion_method = URIRef(obo + row[])
                # Interaction_xref = URIRef(obo + row[])
                # Interaction_annotation = URIRef(obo + row[]) MatrixDBにはなにが入ってる？？
                Taxon_id = URIRef(taxon_id + Dtaxon_id)
                # Taxon_obo = URIRef(obo + row[])
                # Interaction_parameters = URIRef(obo + row[])
                # Creation_date = URIRef(obo + row[])
                # Updata_date = URIRef(obo + row[])
                # INteraction_checksum = URIRef(obo + row[])
                # Negative = URIRef(obo + row[])

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
        dir_list = glob.glob("data/" + service + "/*.tsv", recursive=True)
        for i in range(len(dir_list)):
            create_ttl(dir_list[i], service + str(i), service)


if __name__ == "__main__":
    main()
