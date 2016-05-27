#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'essepuntato'

import json
from crossref_processor import CrossrefProcessor
from conf import *
from resource_finder import ResourceFinder
from orcid_finder import ORCIDFinder
from graphlib import ProvSet
from storer import Storer

cur_file_path = "../test/ref-list-ex.json"
with open(cur_file_path) as fp:
    json_object = json.load(fp)
    crp = CrossrefProcessor(base_iri, context_path, info_dir, json_object,
                            ResourceFinder(ts_url=triplestore_url), ORCIDFinder(orcid_conf_path))
    print "Start processing"
    result = crp.process()
    if result is not None:
        print "Handle provenance"
        prov = ProvSet(result, base_iri, context_path, info_dir)
        print "Create provenance"
        prov.generate_provenance()

        print "Store and push results"
        res_storer = Storer(result)
        res_storer.upload_and_store(base_dir, triplestore_url, base_iri, context_path)

        print "Store and push provenance"
        prov_storer = Storer(prov)
        prov_storer.upload_and_store(base_dir, triplestore_url, base_iri, context_path)

        # TODO: data for datasets (and distributions?)
        # TODO: handle issues in pushing and storing appropriately (no store, no triplestore, for instance)
    else:
        print "issues!"