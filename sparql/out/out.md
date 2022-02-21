# list_propaties

## SPARQL query

```
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?predicate
WHERE {
  ?subject ?predicate ?object
}
```

## RESULTS

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
          "value": "http://www.w3.org/2000/01/rdf-schema#label"
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
          "value": "http://purl.obolibrary.org/obo/IAO_0000119"
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
          "value": "http://purl.org/dc/elements/1.1/identifier"
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
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A"
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
          "value": "http://www.bioassayontology.org/bao#BAO_0002875"
        }
      },
      {
        "predicate": {
          "type": "uri",
          "value": "http://www.biopax.org/release/biopax-level3.owl#interactionType"
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
      }
    ]
  }
}
```

</details>

# list_classes

## SPARQL query

```
prefix owl: <http://www.w3.org/2002/07/owl#>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?class
WHERE {
  ?s a ?class.
}
```

## RESULTS

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
          "value": "http://purl.obolibrary.org/obo/EUPATH_0000591"
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
          "value": "http://purl.obolibrary.org/obo/NCIT_C93638"
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
          "value": "http://www.w3.org/2002/07/owl#ObjectProperty"
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
          "value": "http://www.w3.org/2002/07/owl#NamedIndividual"
        }
      }
    ]
  }
}
```

</details>

# sample_spo

## SPARQL query

```
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT ?p ?o
WHERE {
  <http://rdf.glycoinfo.org/matrixdb.association:chebi_241349__uniprotkb_P02649> ?p ?o
}
```

## RESULTS

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

## SPARQL query

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

## RESULTS

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
          "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#InteractionId"
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
      }
    ]
  }
}
```

</details>

# count_subject

## SPARQL query

```
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT (COUNT(?s) AS ?count)
WHERE {
  ?s ?p ?o
}
```

## RESULTS

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
          "value": "30143644"
        }
      }
    ]
  }
}
```

</details>

# list_class

## SPARQL query

```
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?class
WHERE {
  ?subject a ?class
}
```

## RESULTS

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
          "value": "http://purl.obolibrary.org/obo/EUPATH_0000591"
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
          "value": "http://purl.obolibrary.org/obo/NCIT_C93638"
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
          "value": "http://www.w3.org/2002/07/owl#ObjectProperty"
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
          "value": "http://www.w3.org/2002/07/owl#NamedIndividual"
        }
      }
    ]
  }
}
```

</details>
