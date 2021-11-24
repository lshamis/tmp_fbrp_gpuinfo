import a0
import json
import subprocess
import time
import xmltodict

p = a0.Publisher("gpuinfo")
while True:
    nv_smi = subprocess.check_output(["nvidia-smi", "-x", "-q"])
    p.pub(json.dumps(xmltodict.parse(nv_smi.decode())))
    time.sleep(1)
