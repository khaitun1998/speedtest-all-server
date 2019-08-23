# Speedtest.net on all server

An python script to run speedtest on all available servers, AUTOMATICALLY!!!

## Requirements

- Python 3.6 or higher
- [speedtest-cli](https://github.com/sivel/speedtest-cli)
- csv

## Run
```sh
cd speedtest-all-server/
python3 speedtest_all_server.py
```

By default, this script will run speedtest with <b>Multi mode</b> with minimal server list. If you want to test with <b>Single mode</b> or with full server list:

```sh
python3 speedtest_all_server.py -t [test_type] -l [test_list]
```

Option:
- test_type:
    - multi
    - single
- test_list:
    - full: Testing with a full list from Ookla, over 8000 servers :)
    - minimize: Testing with a minimize list, about 300 servers from each country



The result will be recorded in <b>result.csv</b> file. 

If you want to update list of available servers, please go to [http://c.speedtest.net/speedtest-servers-static.php](http://c.speedtest.net/speedtest-servers-static.php). After that, you must parse XML into JSON Format, using this free tool: [Link](https://codebeautify.org/xmltojson). After parsing XML into JSON, rename it as <b>server.json</b>.

Enjoy!!