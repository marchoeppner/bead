import requests, sys
import json
 

def main():
   
  samples = rest_get("/samples")

  for sample in samples:
    sid = sample["id"]
    d = rest_get(f"/samples/delete/{sid}")
    print(d)


def rest_post(ext):
  server = "http://localhost:4567"
  r = requests.post(server+ext, headers={ "Content-Type" : "application/json"})

  if not r.ok:
    r.raise_for_status()
    sys.exit()

  return r.json()

def rest_get(ext):
  server = "http://localhost:4567"
  r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

  if not r.ok:
    r.raise_for_status()
    sys.exit()

  return r.json()


if __name__ == '__main__':
    main()