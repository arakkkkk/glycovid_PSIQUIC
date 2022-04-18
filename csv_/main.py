import csv

def main():
    covid_genus_protein_path = "covid_genus_protein.csv"
    psicquic_uniprot_chebi_path = "psicquic_uniprot_chebi.csv"
    with open(covid_genus_protein_path, newline='') as csvfile:
        covid_genus_proteins = csvfile.readlines()
    with open(psicquic_uniprot_chebi_path, newline='') as csvfile:
        psicquic_uniprot_chebi = csvfile.readlines()

    

    res = "uniprot_id\ttaxon\tinteractor\tother_interactor\n"
    for crow in covid_genus_proteins:
        crow = crow.rstrip().split(",")
        if crow[0] == "child_taxon":
            continue
        taxon = crow[0]
        protein = crow[1]
        uniprot_id = crow[1].split("/uniprot/")[1]
        # print(uniprot_id)

        for prow in psicquic_uniprot_chebi:
            prow = prow.rstrip().split(",")
            interactor = prow[0]
            if prow[0] == "interactor":
                continue
            other_interactor = prow[1]
            interactor_uniprot_id =  interactor.split("/uniprot/")[1]
            # print(interactor_uniprot_id)
#

            # print(uniprot_id, interactor_uniprot_id)
            # if uniprot_id == "Q6SRT6":
            #     print(uniprot_id)
            #
            if uniprot_id == interactor_uniprot_id:
                res += uniprot_id + "\t" + taxon + "\t" + interactor +"\t" + other_interactor + "\n"

    f = open("out.tsv", "w")
    f.write(res)
    f.close

if __name__ == "__main__":
    main()
