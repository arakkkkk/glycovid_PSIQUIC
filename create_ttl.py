import csv
import rdflib
from rdflib import Graph
from rdflib import Namespace
from rdflib.namespace import RDF, RDFS
from rdflib.namespace import XSD
from rdflib import URIRef, Literal


def main(dir_name, file_name):
    g = Graph()
    # predicate
    detected_by = URIRef("http://www.bioassayontology.org/bao#BAO_0002875")
    author_is = URIRef(
        "http://www.biopax.org/release/biopax-level3.owl#author")
    pub_id = URIRef("http://purl.obolibrary.org/obo/IAO_0000119")

    has_interaction_type_obo = URIRef(
        "http://purl.obolibrary.org/obo/INO_0000154")
    has_interaction_type_bp = URIRef(
        "http://www.biopax.org/release/biopax-level3.owl#interactionType"
    )
    souce_db = URIRef("http://purl.org/dc/elements/1.1/source")
    has_interaction_id_bao = URIRef(
        "http://www.bioassayontology.org/bao#BAO_0000383")
    has_interaction_id_obo = URIRef("http://purl.obolibrary.org/obo/id")
    has_interaction_id_lim = URIRef(
        "http://www.linkedmodel.org/schema/vaem#hasIdentifier"
    )
    ##########################################
    data_xref_obo = URIRef("obolnOwl:hasDbXref")
    # 3
    data_xref_bp = URIRef(
        "http://www.biopax.org/release/biopax-level3.owl#xref")
    interaction_annotate = URIRef("http://www.w3.org/2004/02/skos/core#note")
    organizm = URIRef(
        "http://www.biopax.org/release/biopax-level3.owl#organism")
    interaction_param_pos = URIRef(
        "http://rds.posccaesar.org/2008/02/OWL/ISO-15926-2_2003#hasParameters"
    )
    # interaction_param_bm = URIRef(
    # "http://www.biomodels.net/kisao/KISAO#KISAO_0000259 (has parameter) "
    # )

    # subject
    interactor_ab = rdflib.Namespace(
        "https://identifiers.org/matrixdb.association:")

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

        for row in reader:
            # データの加工
            for i in range(len(row)):
                if 'psi-mi:"' in row[i]:
                    row[i] = row[i].split('"')[1].split('"')[
                        0].replace(":", "_")
                elif ":" in row[i] and "(" in row[i]:
                    row[i] = row[i].split(":")[1].split("(")[0]
                elif ":" in row[i]:
                    row[i] = row[i].split(":")[1].split("|")[0]

            # URIの作成
            Interactor_ab = URIRef(interactor_ab + row[0] + "_" + row[1])
            Detection_method = URIRef(obo + row[6])
            First_aouthor = Literal(row[7], datatype=XSD.string)
            Publication_id = URIRef(publication_id + row[8])
            Interaction_type = URIRef(obo + row[11])
            Source_database = URIRef(obo + row[12])
            Interaction_id = URIRef(intact + row[13])
            # Confidence value
            # Expansion_method = URIRef(obo + row[])
            # Interaction_xref = URIRef(obo + row[])
            # Interaction_annotation = URIRef(obo + row[]) MatrixDBにはなにが入ってる？？
            Taxon_id = URIRef(taxon_id + row[9])
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

            g.serialize(destination="turtle/rdf_" +
                        file_name + ".ttl", format="turtle")


if __name__ == "__main__":
    dir_name = "data/IntAct/IntAct0.tsv"
    file_name = "IntAct0"
    main(dir_name, file_name)
