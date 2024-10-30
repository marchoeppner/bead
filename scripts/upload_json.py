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
    sample = json.load(f)

  d = rest_post("/samples",sample)
  print(d)

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
