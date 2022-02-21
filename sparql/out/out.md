
--- 
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
```
{"head": {"vars": ["predicate"]}, "results": {"bindings": [{"predicate": {"type": "uri", "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"}}, {"predicate": {"type": "uri", "value": "http://purl.obolibrary.org/obo/IAO_0000119"}}, {"predicate": {"type": "uri", "value": "http://purl.obolibrary.org/obo/INO_0000154"}}, {"predicate": {"type": "uri", "value": "http://purl.org/dc/elements/1.1/identifier"}}, {"predicate": {"type": "uri", "value": "http://purl.org/dc/elements/1.1/source"}}, {"predicate": {"type": "uri", "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A"}}, {"predicate": {"type": "uri", "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B"}}, {"predicate": {"type": "uri", "value": "http://semanticscience.org/resource/SIO_000253"}}, {"predicate": {"type": "uri", "value": "http://www.bioassayontology.org/bao#BAO_0002875"}}, {"predicate": {"type": "uri", "value": "http://www.biopax.org/release/biopax-level3.owl#interactionType"}}]}}
```

--- 
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
```
{"head": {"vars": ["p", "o"]}, "results": {"bindings": [{"p": {"type": "uri", "value": "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"}, "o": {"type": "uri", "value": "http://biomodels.net/SBO/SBO_0000344"}}, {"p": {"type": "uri", "value": "http://purl.obolibrary.org/obo/IAO_0000119"}, "o": {"type": "uri", "value": "http://rdf.glycoinfo.org/dbid/pubmed/12950167"}}, {"p": {"type": "uri", "value": "http://purl.obolibrary.org/obo/IAO_0000119"}, "o": {"type": "uri", "value": "http://rdf.glycoinfo.org/dbid/imex/IM-27037"}}, {"p": {"type": "uri", "value": "http://purl.obolibrary.org/obo/INO_0000154"}, "o": {"type": "uri", "value": "http://purl.obolibrary.org/obo/MI_0407"}}, {"p": {"type": "uri", "value": "http://purl.obolibrary.org/obo/INO_0000154"}, "o": {"type": "uri", "value": "http://purl.obolibrary.org/obo/MI_0914"}}, {"p": {"type": "uri", "value": "http://purl.org/dc/elements/1.1/identifier"}, "o": {"type": "uri", "value": "http://rdf.glycoinfo.org/dbid/imex/IM-22103-3"}}, {"p": {"type": "uri", "value": "http://purl.org/dc/elements/1.1/identifier"}, "o": {"type": "uri", "value": "http://rdf.glycoinfo.org/dbid/imex/IM-27037-11"}}, {"p": {"type": "uri", "value": "http://purl.org/dc/elements/1.1/identifier"}, "o": {"type": "uri", "value": "http://rdf.glycoinfo.org/dbid/imex/IM-27037-15"}}, {"p": {"type": "uri", "value": "http://purl.org/dc/elements/1.1/source"}, "o": {"type": "uri", "value": "http://purl.obolibrary.org/obo/MI_1332"}}, {"p": {"type": "uri", "value": "http://purl.org/dc/elements/1.1/source"}, "o": {"type": "uri", "value": "http://purl.obolibrary.org/obo/MI_0486"}}, {"p": {"type": "uri", "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A"}, "o": {"type": "uri", "value": "http://rdf.glycoinfo.org/dbid/CHEBI/241349"}}, {"p": {"type": "uri", "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_B"}, "o": {"type": "uri", "value": "http://rdf.glycoinfo.org/dbid/uniprot/P02649"}}, {"p": {"type": "uri", "value": "http://semanticscience.org/resource/SIO_000253"}, "o": {"type": "uri", "value": "http://semanticscience.org/resource/SIO_000559"}}, {"p": {"type": "uri", "value": "http://www.bioassayontology.org/bao#BAO_0002875"}, "o": {"type": "uri", "value": "http://purl.obolibrary.org/obo/MI_0400"}}, {"p": {"type": "uri", "value": "http://www.bioassayontology.org/bao#BAO_0002875"}, "o": {"type": "uri", "value": "http://purl.obolibrary.org/obo/MI_0096"}}, {"p": {"type": "uri", "value": "http://www.biopax.org/release/biopax-level3.owl#interactionType"}, "o": {"type": "uri", "value": "http://purl.obolibrary.org/obo/MI_0407"}}, {"p": {"type": "uri", "value": "http://www.biopax.org/release/biopax-level3.owl#interactionType"}, "o": {"type": "uri", "value": "http://purl.obolibrary.org/obo/MI_0914"}}]}}
```

--- 
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
```
{"head": {"vars": ["count"]}, "results": {"bindings": [{"count": {"type": "literal", "datatype": "http://www.w3.org/2001/XMLSchema#integer", "value": "23071846"}}]}}
```

--- 
## SPARQL query
```
prefix owl: <http://www.w3.org/2002/07/owl#>

SELECT DISTINCT ?class
WHERE {
  ?subject a ?class
}
```
## RESULTS
```
{"head": {"vars": ["class"]}, "results": {"bindings": [{"class": {"type": "uri", "value": "http://purl.obolibrary.org/obo/EUPATH_0000591"}}, {"class": {"type": "uri", "value": "http://biomodels.net/SBO/SBO_0000344"}}, {"class": {"type": "uri", "value": "http://biomodels.net/SBO/SBO_0000241"}}, {"class": {"type": "uri", "value": "http://purl.obolibrary.org/obo/NCIT_C93638"}}, {"class": {"type": "uri", "value": "http://rdf.glycoinfo.org/PSICQUIC/Ontology#InteractionId"}}]}}
```
