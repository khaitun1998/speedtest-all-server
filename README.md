# Speedtest.net on all server

An python script to run Speedtest.net on all available servers, AUTOMATICALLY!!!

## Requirements

- Python 3.6 or higher
- [speedtest-cli](https://github.com/sivel/speedtest-cli)
- csv

## Run
```sh
cd speedtest-all-server/
python3 speedtest_all_server.py
```

By default, this script will run speedtest with <b>Multi mode</b>. If you want to test with <b>Single mode</b>, please change:

```sh
down ,up ,ping = speed_test_multi(server_to_test)
```

into

```sh
down ,up ,ping = speed_test_single(server_to_test)
```

The result will be recorded in <b>result.csv</b> file. 

If you want to update list of available servers, please go to [http://c.speedtest.net/speedtest-servers-static.php](http://c.speedtest.net/speedtest-servers-static.php). After that, you must parse XML into JSON Format, using this free tool: [Link](https://codebeautify.org/xmltojson). After parsing XML into JSON, rename it as <b>server.json</b>.

Enjoy!!