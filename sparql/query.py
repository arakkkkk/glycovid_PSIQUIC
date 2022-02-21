import json
from glob import glob

from SPARQLWrapper import JSON, SPARQLWrapper


def sparql(endpoint: str, sparqlist_dir: str):
    sparql = SPARQLWrapper(endpoint)
    dir_list = glob(sparqlist_dir + "/**.txt", recursive=True)
    with open(sparqlist_dir + "/../out/out.md", "w") as f:
        f.write("")
    for i in range(len(dir_list)):
        print(str(i + 1) + "/" + str(len(dir_list)), "\texecute: ", dir_list[i])
        with open(dir_list[i]) as f:
            query = f.read()
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        with open(sparqlist_dir + "/../out/out.md", "a") as f:
            f.write("\n--- \n")
            f.write("## SPARQL query\n")
            f.write(dir_list[i].split("/")[-1].split(".")[0] + "\n")
            f.write("```\n")
            f.write(query)
            f.write("```\n")
        try:
            results = sparql.queryAndConvert()
            with open(sparqlist_dir + "/../out/out.md", "a") as f:
                f.write("## RESULTS\n")
                f.write("```\n")
                f.write(json.dumps(results) + "\n")
                f.write("```\n")
            # for head in results["head"]["vars"]:
            #     print("\t", head, end="")
            # print()
            # count = 0
            # for row in results["results"]["bindings"]:
            #     print(count, end="")
            #     for key in row:
            #         print("\t", row[key]["value"], end="")
            #     print()
            #     count += 1
        except Exception as e:
            print(e)


if __name__ == "__main__":
    endpoint = "http://localhost:3030/psicquic_2_15_22/sparql"
    sparqlist_dir = "/Users/kouiti/localfile/glycovid/glycovid_PSIQUIC/sparql/sparqlist"
    sparql(endpoint, sparqlist_dir)
