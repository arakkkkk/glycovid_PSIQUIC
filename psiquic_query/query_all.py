from urllib.request import urlopen
from glob import glob
import xml.etree.ElementTree as ET
import os
import shutil

# ------------------ FUNCTIONS ------------------


class PsicquicService:
    def __init__(self, name, restUrl):
        self.name = name
        self.restUrl = restUrl


def readURL(url):
    try:
        fileHandle = urlopen(url)
        content = fileHandle.read()
        fileHandle.close()
    except IOError as e:
        # print('Cannot open URL ' + url)
        import traceback

        error_point = traceback.format_exc().split("\n")[1]
        error_message = traceback.format_exc().split("\n")[-2]
        content = ""
        print(error_message)
    return content


def readActiveServicesFromRegistry():
    registryActiveUrl = "http://www.ebi.ac.uk/Tools/webservices/psicquic/registry/registry?action=ACTIVE&format=xml"

    content = readURL(registryActiveUrl)

    # Create the XML reader
    root = ET.fromstring(content)
    xmlns = "{http://hupo.psi.org/psicquic/registry}"

    services = []

    for service in root.findall(xmlns + "service"):
        name = service.find(xmlns + "name")
        restUrl = service.find(xmlns + "restUrl")

        service = PsicquicService(name.text, restUrl.text)
        services.append(service)

    return services


def queryPsicquic(service_name, psicquicRestUrl, query, offset, maxResults, init):
    dirname = "data/" + service_name
    if init:
        try:
            shutil.rmtree(dirname)
        except:
            pass
    try:
        os.mkdir(dirname)
    except:
        pass

    for i in range(100):
        filename = dirname + "/" + service_name + str(i) + ".tsv"
        if glob(filename):
            offset += 100000
            maxResults += 100000
            continue
        f = open(filename, "w")
        f.write(
            "Unique identifier for interactor A"
            + "\tUnique identifier for interactor B"
            + "\tAlternative identifier for interactor A"
            + "\tAlternative identifier for interactor B"
            + "\tAliases for A"
            + "\tAliases for B"
            + "\tInteraction detection methods"
            + "\tFirst author"
            + "\tIdentifier of the publication"
            + "\tNCBI Taxonomy identifier for interactor A"
            + "\tNCBI Taxonomy identifier for interactor B"
            + "\tInteraction types"
            + "\tSource databases"
            + "\tInteraction identifier(s)"
            + "\tConfidence score"
        )
        f.close()
        for j in range(10):
            psicquicUrl = (
                psicquicRestUrl
                + "query/"
                + query
                + "?firstResult="
                + str(offset)
                + "&maxResults="
                + str(maxResults)
            )
            # print("URL: " + psicquicUrl)
            print("loading ", service_name, "...\t", offset, "~", maxResults)
            psicquicResultLines = readURL(psicquicUrl).splitlines()

            content = ""
            for line in psicquicResultLines:
                line = str(line, encoding="utf8")
                # content = arrangeData(line)
                content += line + "\n"
            if len(psicquicResultLines) == 0:
                return

            f = open(filename, "a")
            f.write(content)
            f.close()

            offset += 10000
            maxResults += 10000


def main(query):
    services = readActiveServicesFromRegistry()
    services_list = [
        # "BioGrid",
        # "bhf-ucl",
        # "ChEMBL",
        # "DIP",
        # "HPIDb",
        "IntAct",
        # "IMEx",
        # "mentha",
        # "MPIDB",
        # "iRefIndex",
        # "MatrixDB",
        # "MINT",
        # "Reactome",
        # "Reactome-FIs",
        # "EBI-GOA-miRNA",
        # "UniProt",
        # "MBInfo",
        # "BindingDB",
        # "VirHostNet",
        # "BAR",
        # "EBI-GOA-nonIntAct",
        # "tfact2gene",
    ]
    import os

    path = os.getcwd()

    print(path)

    for service in services:
        if service.name in services_list:
            queryPsicquic(service.name, service.restUrl,
                          query, 1, 10000, False)


if __name__ == "__main__":
    queryes = ["*"]

    for query in queryes:
        main(query)
