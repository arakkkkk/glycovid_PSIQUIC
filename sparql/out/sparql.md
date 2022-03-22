



# query_by_glycan
### SPARQL query
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX chebi: <https://www.ebi.ac.uk/rdf/services/sparql>
PREFIX glycan: <http://purl.jp/bio/12/glyco/glycan#>
SELECT distinct ?glytoucan_url ?chebi_uri

WHERE {
  BIND("chebi" as ?database)
  BIND("100408" as ?id)

  ?interaction a <http://biomodels.net/SBO/SBO_0000344> .
  BIND(?database + "_" + ?id as ?interactor)
  FILTER CONTAINS (str(?interaction), ?interactor)

  ?interaction ?predicate ?object

  FILTER CONTAINS (str(?object), "http://rdf.glycoinfo.org/dbid/CHEBI/")

  BIND(REPLACE(str(?object), "http://rdf.glycoinfo.org/dbid/CHEBI/", "", "i") AS ?chebi_id)
  BIND(URI(CONCAT("http://rdf.glycoinfo.org/chebi/", ?chebi_id)) as ?chebi_uri)

  SERVICE <https://ts.glycosmos.org/sparql> {
    ?glytoucan_url glycan:has_resource_entry ?chebi_uri .
  }
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "glytoucan_url",
      "chebi_uri"
    ]
  },
  "results": {
    "bindings": []
  }
}
```
</details>




# list_propaties
### SPARQL query
```
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?predicate
WHERE {
  ?subject ?predicate ?object
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "predicate"
    ]
  },
  "results": {
    "bindings": [
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#versionIRI"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#imports"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2000/01/rdf-schema#range"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2000/01/rdf-schema#domain"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2000/01/rdf-schema#label"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/IAO_0000115"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/IAO_0006012"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#equivalentClass"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2000/01/rdf-schema#subClassOf"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#first"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#rest"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#onProperty"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#someValuesFrom"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#intersectionOf"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/IAO_0000119"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://purl.org/dc/elements/1.1/identifier"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/INO_0000154"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://semanticscience.org/resource/SIO_000253"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://purl.org/dc/elements/1.1/source"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.bioassayontology.org/bao#BAO_0002875"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.biopax.org/release/biopax-level3.owl#interactionType"
        }
      }
    ]
  }
}
```
</details>




# list_classes
### SPARQL query
```
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?class
WHERE {
  ?s a ?class.
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "class"
    ]
  },
  "results": {
    "bindings": [
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#Ontology"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#AnnotationProperty"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/NCIT_C93638"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.biopax.org/release/biopax-level3.owl#MolecularInteraction"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/ontology/interaction#InteractionId"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://biomodels.net/SBO/SBO_0000344"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#ObjectProperty"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://biomodels.net/SBO/SBO_0000241"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/EUPATH_0000591"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#Class"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#Restriction"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#InteractionId"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#NamedIndividual"
        }
      }
    ]
  }
}
```
</details>




# sample_spo
### SPARQL query
```
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT ?p ?o
WHERE {
  <http://rdf.glycoinfo.org/matrixdb.association:chebi_241349__uniprotkb_P02649> ?p ?o
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "p",
      "o"
    ]
  },
  "results": {
    "bindings": [
      {
        "p": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A"
        },
        "o": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/CHEBI/241349"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
        },
        "o": {
          "type": "uri",
          "value": "http://www.biopax.org/release/biopax-level3.owl#MolecularInteraction"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
        },
        "o": {
          "type": "uri",
          "value": "http://biomodels.net/SBO/SBO_0000344"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
        },
        "o": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#NamedIndividual"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/IAO_0000119"
        },
        "o": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/pubmed/12950167"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/IAO_0000119"
        },
        "o": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/imex/IM-27037"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.org/dc/elements/1.1/identifier"
        },
        "o": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/imex/IM-22103-3"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.org/dc/elements/1.1/identifier"
        },
        "o": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/imex/IM-27037-11"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.org/dc/elements/1.1/identifier"
        },
        "o": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/imex/IM-27037-15"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/INO_0000154"
        },
        "o": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/MI_0407"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/INO_0000154"
        },
        "o": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/MI_0914"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B"
        },
        "o": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/dbid/uniprot/P02649"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://semanticscience.org/resource/SIO_000253"
        },
        "o": {
          "type": "uri",
          "value": "http://semanticscience.org/resource/SIO_000559"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.org/dc/elements/1.1/source"
        },
        "o": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/MI_1332"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://purl.org/dc/elements/1.1/source"
        },
        "o": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/MI_0486"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://www.bioassayontology.org/bao#BAO_0002875"
        },
        "o": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/MI_0400"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://www.bioassayontology.org/bao#BAO_0002875"
        },
        "o": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/MI_0096"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://www.biopax.org/release/biopax-level3.owl#interactionType"
        },
        "o": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/MI_0407"
        }
      },
      {
        "p": {
          "type": "uri",
          "value": "http://www.biopax.org/release/biopax-level3.owl#interactionType"
        },
        "o": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/MI_0914"
        }
      }
    ]
  }
}
```
</details>




# selection_of_classes
### SPARQL query
```
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?class ?label ?description
WHERE {
  ?class a owl:Class.
  OPTIONAL { ?class rdfs:label ?label}
  OPTIONAL { ?class rdfs:comment ?description}
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "class",
      "label",
      "description"
    ]
  },
  "results": {
    "bindings": [
      {
        "class": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/NCIT_C93638"
        },
        "label": {
          "type": "literal",
          "datatype": "http://www.w3.org/2000/01/rdf-schema#Literal",
          "value": "Publication Identifier"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://biomodels.net/SBO/SBO_0000344"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://biomodels.net/SBO/SBO_0000241"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/EUPATH_0000591"
        },
        "label": {
          "type": "literal",
          "xml:lang": "en",
          "value": "host organism"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/OBI_0100026"
        },
        "label": {
          "type": "literal",
          "xml:lang": "en",
          "value": "organism"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/OBI_0000725"
        },
        "label": {
          "type": "literal",
          "value": "host role"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b0"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#InteractionId"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b1"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b2"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b3"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b4"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b5"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b6"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b7"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b8"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b9"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b10"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b11"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b12"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b13"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b14"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b15"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b16"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b17"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b18"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b19"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b20"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b21"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b22"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b23"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b24"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b25"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b26"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b27"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b28"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b29"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b30"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b31"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b32"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b33"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b34"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b35"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b36"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b37"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b38"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b39"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b40"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b41"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b42"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b43"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b44"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b45"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b46"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b47"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b48"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b49"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b50"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b51"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b52"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b53"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b54"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b55"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b56"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b57"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b58"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b59"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b60"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b61"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b62"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b63"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b64"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b65"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b66"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b67"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b68"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b69"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b70"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b71"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b72"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b73"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b74"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b75"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b76"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b77"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b78"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b79"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b80"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b81"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b82"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b83"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b84"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b85"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b86"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b87"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b88"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b89"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b90"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b91"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b92"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b93"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b94"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b95"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b96"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b97"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b98"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b99"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b100"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b101"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b102"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b103"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b104"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b105"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b106"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b107"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b108"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b109"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b110"
        }
      },
      {
        "class": {
          "type": "bnode",
          "value": "b111"
        }
      }
    ]
  }
}
```
</details>




# list_object_heads
### SPARQL query
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
SELECT ?head_o (count(?head_o) as ?count)
WHERE {
  ?s ?p ?o.
  MINUS {
      ?s a ?o .
  }
  BIND(REPLACE(str(?o), "/[^/]+$", "", "i") AS ?head_o)
}
group by ?head_o
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "head_o",
      "count"
    ]
  },
  "results": {
    "bindings": [
      {
        "head_o": {
          "type": "literal",
          "value": "Publication Identifier"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "An organism that has host role"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/rigid"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "310669"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/emdb"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "303"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/CHEBI"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "157938"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/pubmed"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "2037804"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/ntnu"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "89322"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/rnacentral"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1602"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/ensemblgenomes"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "3"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/taxonomy"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1580903"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/chembl.target"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "6"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "organism"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/uniprot"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "2369714"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/biogrid"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "775636"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://www.bioassayontosiyousuru.org"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "136"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/interpro"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "10"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/signor"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "27"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/ensembl"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "41877"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/mint"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "39224"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/doi"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "73854"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "https://bioregistry.io/reference"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "483"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/rhea"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "5"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "host organism"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "0"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/ncbigene"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "637222"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/intact"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "253255"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "host role"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/intenz"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "12"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/mpid"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "18"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "yes"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://www.w3.org/1999/02"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "112"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/refseq"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "105860"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/imex"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "945398"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/virhostnet-nrid"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "31536"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/rogid"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1776"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/complexportal"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/pmc"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1841"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/empiar"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/OMIM"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "80"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://protege.stanford.edu/plugins/owl/dc"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://www.biopax.org/release"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "3"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://www.bioassayontology.org/bao"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://biomodels.net/SBO"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "7"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/efo"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "6"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/BTO"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "3"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/dip"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "9611"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "has role"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/insdc"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "75"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/reactome"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "86"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://purl.obolibrary.org/obo"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "8482115"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/pdb"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1734"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/chembl"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "904535"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/pride"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1445"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/dbid/complex"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "356"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/ontology"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://semanticscience.org/resource"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "11166"
        }
      },
      {
        "head_o": {
          "type": "literal",
          "value": "http://rdf.glycoinfo.org/PSICQUIC"
        },
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "1"
        }
      }
    ]
  }
}
```
</details>




# count_subject
### SPARQL query
```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT (COUNT(?s) AS ?count)
WHERE {
  ?s ?p ?o
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "count"
    ]
  },
  "results": {
    "bindings": [
      {
        "count": {
          "type": "literal",
          "datatype": "http://www.w3.org/2001/XMLSchema#integer",
          "value": "29665169"
        }
      }
    ]
  }
}
```
</details>




# list_class
### SPARQL query
```
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?class
WHERE {
  ?subject a ?class
}
```
### RESULTS
<details>
<summary>Toggle</summary>

```
{
  "head": {
    "vars": [
      "class"
    ]
  },
  "results": {
    "bindings": [
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#Ontology"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#AnnotationProperty"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/NCIT_C93638"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.biopax.org/release/biopax-level3.owl#MolecularInteraction"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/ontology/interaction#InteractionId"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://biomodels.net/SBO/SBO_0000344"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#ObjectProperty"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://biomodels.net/SBO/SBO_0000241"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://purl.obolibrary.org/obo/EUPATH_0000591"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#Class"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#Restriction"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#InteractionId"
        }
      },
      {
        "class": {
          "type": "uri",
          "value": "http://www.w3.org/2002/07/owl#NamedIndividual"
        }
      }
    ]
  }
}
```
</details>
