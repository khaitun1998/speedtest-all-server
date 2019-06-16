import json
import speedtest as st
import csv
import os, sys

id_server = []

header = 'id country name sponsor download(mbps) upload(mbps) ping(ms)'
header = header.split()

file = open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'result.csv')), 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)

def speed_test_multi(server):
    s = st.Speedtest()
    s.get_servers(server)
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def speed_test_single(server):
    s = st.Speedtest()
    s.get_servers(server)
    s.download(threads=1)
    s.upload(threads=1)
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

with open('server.json', encoding="utf8", newline='') as json_f:
    data = json.load(json_f)
    for d in data['server']:
        print(f'Testing server: {d["_name"]} in country: {d["_country"]}')
        server_to_test = [int(d['_id'])]
        try:
            down ,up ,ping = speed_test_multi(server_to_test)
        except:
           print("error") 

        result_str = f'{d["_id"]}_{d["_country"]}_{d["_name"]}_{d["_sponsor"]}_{round(down/1000000, 2)} Mbps_{round(up/1000000,2)} Mbps_{round(ping,2)} ms'

        file = open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'result.csv')), 'a', newline='')
        with file:
            writer = csv.writer(file)
            writer.writerow(result_str.split("_"))