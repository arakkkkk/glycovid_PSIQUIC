from log.log import init_log, log
from datetime import datetime
import shutil
import os
import xml.etree.ElementTree as ET
from glob import glob
from urllib.request import urlopen
from lib import general_method as gm


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
        exit()
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
    dirname = "test_data/" + service_name
    if init:
        try:
            shutil.rmtree(dirname)
        except:
            pass
    try:
        os.mkdir(dirname)
    except:
        pass

    psicquicUrl = (
        psicquicRestUrl
        + "query/"
        + query
        + "?firstResult="
        + str(offset)
        + "&maxResults="
        + str(maxResults)
        + "&format=count"
    )
    max_count = str(readURL(psicquicUrl)).split("'")[1].split("'")[0]
    filename = dirname + "/" + service_name + "0.tsv"
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
    if max_count == "0":
        # print(service_name, "data not found")
        print(0)
        return
    print_text = (
        ""
        # + str(datetime.now())
        # + "\t>\tloading "
        # + service_name
        # + "...\t"
        # + str(offset)
        # + "~"
        # + str(maxResults)
        # + "\t/ "
        + str(max_count)
        # + "\t"
        # + str(int(int(maxResults) / int(max_count) * 100))
        # + "%"
    )
    print(print_text)
    psicquicResultLines = readURL(psicquicUrl).splitlines()
    content = ""
    max_count = 0
    for line in psicquicResultLines:
        line = str(line, encoding="utf8")
        # content = arrangeData(line)
        # if "9606" in line.split("\t")[9]:
        content += line + "\n"
    if len(psicquicResultLines) == 0:
        return

    f = open(filename, "a")
    f.write(content)
    f.close()


def main(query):
    services = readActiveServicesFromRegistry()
    services_list = gm.list_serveice()
    import os

    path = os.getcwd()

    print(path)

    for service in services:
        # print(service.name, "\t", end="")
        if service.name in services_list:
            queryPsicquic(service.name, service.restUrl, query, 1, 100, True)


if __name__ == "__main__":
    queryes = ["*"]
    # queryes = ["species:human"]
    # queryes = ["species:9606"]
    # queryes = ["taxidA:human"]
    # queryes = ["taxidA:9606"]

    # queryes = [
    #     "(species:human OR species:9606 OR taxidA:human OR taxidA:9606 OR taxidB:human OR taxidA:9606)"
    #     + " AND NOT interaction_id:phosphorylation reaction"
    #     + " AND NOT interaction_id:dephosphorylation reaction"
    #     + " AND NOT interaction_id:predicted interaction"
    # ]
    # queryes = [
    #     "((((species:human OR species:9606 OR taxidA:human OR taxidA:9606 OR taxidB:human OR taxidA:9606)"
    #     + " NOT interaction_id:phosphorylation reaction)"
    #     + " NOT interaction_id:dephosphorylation reaction)"
    #     + " NOT interaction_id:predicted interaction)"
    # ]
    # queryes[0] = queryes[0].replace(" ", "%20")

    for query in queryes:
        main(query)
