import requests, sys
import json
 
def main():
   
  samples = rest_get("/samples")

  for sample in samples:
    this_sample = rest_get(f"/samples/{sample['id']}")
    print(f"{this_sample['sample']}")

def rest_get(ext):
  server = "http://localhost:4567"
  r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

  if not r.ok:
    r.raise_for_status()
    sys.exit()

  return r.json()


if __name__ == '__main__':
    main()
