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
