def treatIRI(iri: str):
    return iri


class LibOwl:
    def __init__(self, template_file: str):
        self.owl_header = self.getOwlHeader(template_file)
        self.owl_annotation_properties = self.getOwlAnnotationProperties(template_file)
        self.owl_object_properties = self.getOwlObjectProperties(template_file)
        self.owl_classes = self.getOwlClasses(template_file)
        self.owl_individuals = self.getOwlIndividuals(template_file)
        self.owl_comment = self.getOwlComment(template_file)

    def getOwlHeader(self, file: str) -> list:
        text = list()
        with open(file) as f:
            for line in f:
                text.append(line)
                if len(line) > 3 and "#################" in line:
                    break
        assert len(text) > 0
        return text


    def getOwlAnnotationProperties(self, file: str) -> list:
        text = list()
        isTarget = False
        with open(file) as f:
            for line in f:
                if "Annotation properties" in line:
                    isTarget = True
                if not isTarget:
                    continue
                text.append(line)
                if len(line) > 3 and "#################" in line:
                    break
        assert len(text) > 0
        return text

    def getOwlObjectProperties(self, file: str) -> list:
        text = list()
        isTarget = False
        with open(file) as f:
            for line in f:
                if "Object Properties" in line:
                    isTarget = True
                if not isTarget:
                    continue
                text.append(line)
                if len(line) > 3 and "#################" in line:
                    break
        assert len(text) > 0
        return text

    def getOwlClasses(self, file: str) -> list:
        text = list()
        isTarget = False
        with open(file) as f:
            for line in f:
                if "Classes" in line:
                    isTarget = True
                if not isTarget:
                    continue
                text.append(line)
                if len(line) > 3 and "#################" in line:
                    break
        assert len(text) > 0
        return text

    def getOwlIndividuals(self, file: str) -> list:
        text = list()
        isTarget = False
        with open(file) as f:
            for line in f:
                if "Individuals" in line:
                    isTarget = True
                if not isTarget:
                    continue
                text.append(line)
                if len(line) > 3 and "#################" in line:
                    break
        assert len(text) > 0
        return text

    def getOwlComment(self, file: str) -> list:
        f = open(file, "r")
        text = f.read()
        f.close
        return [text.split("\n")[-1]]

    def inportRdf(file: str):
        """ convert rdf data to Individual instance and append in LibOwl.individuals
        """
        with open(file) as f:
            for line in f:
                print(line)




class Individual:
    def __init__(self, subject: str):
        subject = treatIRI(subject)
        self.type = None
        self.relations = list()
        self.subject = subject

    def typeIs(self, type: str):
        type = treatIRI(type)
        self.type = type

    def addRelation(self, property: str, object: str):
        property = treatIRI(property)
        object = treatIRI(object)
        self.relations.append({"property": property, "object": object})

    def toStr(self) -> list:
        """
                ###  https://identifiers.org/matrixdb.association:ensembl_ENSG00000023445__uniprotkb_Q04206
                <https://identifiers.org/matrixdb.association:ensembl_ENSG00000023445__uniprotkb_Q04206> rdf:type owl:NamedIndividual ,
                            bpo:MolecularInteraction ;
                         obo:IAO_0000119 <http://glycoinfo.org/dbid/imex/IM-23322> ;
                         obo:INO_0000154 obo:MI_0914 ;
                         bpo:interactionType obo:MI_0914 ;
                         bpo:organism <http://glycoinfo.org/dbid/taxonomy/9606> ;
                         dc:identifier <http://glycoinfo.org/dbid/imex/IM-23322-1> ;
                         dc:source obo:MI_0469 ;
                         bao:BAO_0002875 obo:MI_0402 .
        """
        assert self.type is not None
        text = [
                    "### " + self.subject,
                    self.subject + " rdf:type owl:NameIndividual ,",
                    "\t\t" + self.type + ";"
                ]
        for relation in self.relations:
            text.append("\t" + relation["property"] +  " " + relation["object"] + " ;")
        text[-1] = text[-1][:-1] + ".\n"
        text.append("")
        return text



if __name__ == "__main__":
    owl = LibOwl("owl/1_19/psicquic1_19.owl")
