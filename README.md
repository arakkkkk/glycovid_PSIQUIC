# glycovid_PSIQUIC

## Content

```
# query psicquic data by rest api
python query_all.py
# exppantion tsv by "|"
python mylib/expansion_tsv.py
# create ttl file from tsv
python create_ttl.py
# create owl file from ttl
python create_owl.py
# run test query by /sparql/sparqlist/*.txt in /turtle/**/*.ttl
python sparql/query.py
# check /sparql/out/out.md
```

[rdf contain](https://github.com/arakkkkk/glycovid_PSIQUIC/blob/main/sparql/out/out.md)<br>

### Description

- mylib/general_method.py
  - service list of psicquic
- data/
  - query results
- expdata/
  - results of expantion tsvdata
- sparql/
  - run sparql query in python

# glycovid_PSICQUIC 仕様

- スキーマ

[Flowchart Maker & Online Diagram Software](https://app.diagrams.net/#G1l1cZKZryTm6ed0e-L-dOC0RhhKUMjtAt)

- db 一覧
  - BioGrid
  - bhf-ucl
  - ChEMBL
  - HPIDb
  - IntAct
  - IMEx
  - mentha
  - MPIDB
  - iRefIndex
  - MatrixDB
  - MINT
  - Reactome
  - Reactome-FIs
  - EBI-GOA-miRNA
  - UniProt
  - MBInfo
  - BindingDB
  - VirHostNet
  - #BAR
  - EBI-GOA-nonIntAct
  - tfact2gene
- クエリ内容

```jsx
queryes = [
  "species:human" + " OR species:9606" + " OR taxidA:human" + " OR taxidA:9606" + " OR taxidB:human" + " OR taxidA:9606"
];
interactiontype_except_list = [
  'psi-mi:"MI:0217"(phosphorylation reaction)',
  'psi-mi:"MI:0203"(dephosphorylation reaction)',
  'psi-mi:"MI:1110"(predicted interaction)'
];
```

- MatrixDB とデータがつながる形でマッピング

[Flowchart Maker & Online Diagram Software](https://app.diagrams.net/#G1Vdkum5NCG3MsLvJ7HJ6PDXt6iG7PCHaw)

```jsx
@prefix ns1: <http://www.biopax.org/release/biopax-level3.owl#> .
@prefix ns2: <http://www.linkedmodel.org/schema/vaem#> .
@prefix ns3: <http://purl.obolibrary.org/obo/> .
@prefix ns4: <http://rdf.glycoinfo.org/ontology/interaction#> .
@prefix ns5: <http://www.bioassayontology.org/bao#> .
@prefix ns6: <http://purl.org/dc/elements/1.1/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://identifiers.org/matrixdb.association:intact_EBI-7460430__uniprotkb_P53667> ns3:IAO_0000119 <https://identifiers.org/pubmed/15660133> ;
    ns3:INO_0000154 ns3:MI_0915 ;
    ns3:id <https://identifiers.org/minT/MINT-8220587> ;
    ns6:source ns3:MI_0471 ;
    ns4:has_interactor_A <https://identifiers.org/intact/EBI-7460430> ;
    ns4:has_interactor_B <https://identifiers.org/uniprot/P53667> ;
    ns5:BAO_0000383 <https://identifiers.org/minT/MINT-8220587> ;
    ns1:author "Soosairajahetal.(2005)"^^xsd:string ;
    ns1:interactionType ns3:MI_0915 ;
    ns1:organism <https://identifiers.org/taxonomy/9606> ;
    ns2:hasIdentifier <https://identifiers.org/minT/MINT-8220587> .
```

- subject: interactor_ab
  - [https://identifiers.org/matrixdb.association:{database*a}*{id*a}\_\_{database_b}*](https://identifiers.org/matrixdb.association:intact_EBI-7460430__uniprotkb_P53667){id_b}
  - 大文字は小文字に
  - 記号は-に変換(\_)
- object
  - [https://identifiers.org](https://identifiers.org/): 　 → 　　[http://rdf.glycoinfo.org/dbid/](http://glycoinfo.org/dbid/)
  - P39060-PRO_000005794 → P39060#PRO_000005794
  - chebi のデータは[https://github.com/dbcls/togoid-config/blob/main/config/dataset.yaml](https://github.com/dbcls/togoid-config/blob/main/config/dataset.yaml)に合わせる
- interaction_ab から interactorA/B へのプロパティ
  - [~~http://rdf.glycoinfo.org/ontology/interaction#has_interactor_A](http://rdf.glycoinfo.org/ontology/interaction#has_interactor_A)~~
  - [http://rdf.glycoinfo.org/PSICQUIC/Ontology#has_interactor_A](http://rdf.glycoinfo.org/psiquic/Ontology#has_interactor_A)
- interaction id の class
  - [~~http://rdf.glycoinfo.org/ontology/interaction](http://rdf.glycoinfo.org/ontology/interaction#has_interactor_A)#InteractionId~~
  - [http://rdf.glycoinfo.org/PSICQUIC/Ontology#InteractionId](http://rdf.glycoinfo.org/psiquic/Ontology#InteractionId)
- 基本的に URI は<[http://rdf.glycoinfo.org/dbid/](http://glycoinfo.org/dbid/){db}/{id}>を使用する
  - [https://identifiers.org](https://identifiers.org/)/{db}/:　 → 　[http://rdf.glycoinfo.org/dbid/](http://glycoinfo.org/dbid/){db}/
  - purl.obolibrary.org, bioregistry.org は例外的に使用する
- Host organism の URI について
  - taxonid: -1(in vitro)は<[http://www.bioassayontosiyousuru.org/bao#BAO_0020008](http://www.bioassayontology.org/bao#BAO_0020008)>を使用する
  - axohaid: -2(chemical synthesis)は<[http://semanticscience.org/resource/SIO_000559](http://semanticscience.org/resource/SIO_000559)>を使用する
  ```
  <...> <http://semanticscience.org/resource/SIO_000253> [ rdf:type <http://semanticscience.org/resource/SIO_000559> ] .
  ```
  ```
  <...> <http://semanticscience.org/resource/SIO_000253> [ rdf:type <http://www.bioassayontology.org/bao#BAO_0020008> ] .
  ```
- 除いたデータ
  - [http://rdf\\.glycoinfo\\.org/dbid/pubmed/unassigned\\d+](http://rdf%5C%5C.glycoinfo%5C%5C.org/dbid/pubmed/unassigned%5C%5Cd+)
    - intact, imex, mentha
  - [http://rdf\\.glycoinfo\\.org/dbid/reactome/REACT\_\\d{4}\\.\\d](http://rdf%5C%5C.glycoinfo%5C%5C.org/dbid/reactome/REACT_%5C%5Cd%7B4%7D%5C%5C.%5C%5Cd)
    - mint
  - [http://rdf\\.glycoinfo\\.org/dbid/uniprot/Missing-Uniprot-ID-for-[A-Z0-9]+](http://rdf%5C%5C.glycoinfo%5C%5C.org/dbid/uniprot/Missing-Uniprot-ID-for-%5BA-Z0-9%5D+)
    - tfact2gene
  - [http://rdf\\.glycoinfo\\.org/dbid/ensembl/Missing-Ensembl-Gene-ID-for-[-@A-Z0-9]+](http://rdf%5C%5C.glycoinfo%5C%5C.org/dbid/ensembl/Missing-Ensembl-Gene-ID-for-%5B-@A-Z0-9%5D+)
    - tfact2gene

### object list
