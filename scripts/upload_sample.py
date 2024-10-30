#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests, sys
import json
import argparse

parser = argparse.ArgumentParser(description="Script options")
parser.add_argument("--input", help="An input option")
parser.add_argument("--output")
args = parser.parse_args()


def main(input):

  with open(input) as f:
    lines = f.read().splitlines()

  allele_data = "\n".join(lines)

  sample = { 'sample_id': "Sample2", "taxon": "Ecoli"}

  d = rest_post("/samples",sample)
  sid = d["id"]

  alleles = { "cgmlst_scheme": "chewbbaca_9", "cgmlst_scheme_version": "v9", "profile": allele_data }

  a = rest_post(f"/samples/{sid}/alleles",alleles)
  print(a)

def rest_post(ext,data):
  server = "http://localhost:4567"
  r = requests.post(server+ext, data=json.dumps(data), headers={ "Content-Type" : "application/json"})

  if not r.ok:
    print(r)
    #r.raise_for_status()
    #sys.exit()

  return r.json()


if __name__ == '__main__':
    main(args.input)
