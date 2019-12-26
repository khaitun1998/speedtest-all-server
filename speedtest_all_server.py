import json
import csv
import os, sys
import time
import traceback

from optparse import OptionParser

start_time = time.time()

filename = "server_minimize.json"
# test_type = ""
id_server = []

header = 'id time location serverName download(mbps) upload(mbps) ping(ms) jitter(ms) result_url time_execute(s)'
header = header.split()

parser = OptionParser()

# parser.add_option("-t", "--type", dest="test_type", default="multi")
parser.add_option("-l", "--list", dest="test_list", default="minimize")

(options, args) = parser.parse_args()

# print(options.test_type)

if options.test_list == 'minimize':
    filename = 'server_minimize.json'
elif options.test_list == 'full':
    filename = 'server.json'
else:
    print("Invalid Argument")
    sys.exit(0)

file = open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'result.csv')), 'w', newline='')
with file:
    writer = csv.writer(file)
    writer.writerow(header)

count = 0

with open(filename, encoding="utf8", newline='') as json_f:
    data = json.load(json_f)
    for d in data['server']:
        print(f'Testing server: {d["_name"]} in country: {d["_country"]}')
        s_time = time.time()
        server_to_test = int(d['_id'])
            
        result_str = ""
        
        try:
            # if options.test_type == 'multi':
            #     down ,up ,ping = speed_test_multi(server_to_test)
            # elif options.test_type == 'single':
            #     down ,up ,ping = speed_test_single(server_to_test)
            
            stream = os.popen(f'speedtest -f json -s {server_to_test}')
            
            tmp_result = json.loads(stream.read())
            
            download = tmp_result["download"]["bandwidth"]
            upload = tmp_result["upload"]["bandwidth"]
            ping = tmp_result["ping"]["latency"]
            jitter = tmp_result["ping"]["jitter"]
            timestamp = tmp_result["timestamp"]
            result_url = tmp_result["result"]["url"]
            location = f'{tmp_result["server"]["location"]} - {tmp_result["server"]["country"]}'
            server_name = f'{tmp_result["server"]["name"]}'
            
            result_str = f'{d["_id"]}_{timestamp}_{location}_{server_name}_{round((download*8)/(1024*1024), 2)}_{round((upload*8)/(1024*1024),2)}_{round(ping,2)}_{round(jitter,2)}_{result_url}_{round(time.time() - s_time, 2)} s'
            
        except Exception:
           traceback.print_exc() 
           result_str = f'error'
        
        file = open(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'result.csv')), 'a', newline='')
        count+=1
        print(f'Number of tested server: {count}')
        
        with file:
            writer = csv.writer(file)
            writer.writerow(result_str.split("_"))

print(f'Total execution time: {time.time() - start_time} s')
