# Speedtest on all server

An python script to run speedtest on all available servers, AUTOMATICALLY!!!

## Requirements

- Python 3.6 or higher
- [speedtest-cli](https://github.com/sivel/speedtest-cli)
- csv

Link to get list of server from Ookla: [Server List](http://c.speedtest.net/speedtest-servers-static.php).

Parse into JSON Format: [Link](https://codebeautify.org/xmltojson). After parse XML to JSON, rename it as <b>server.json</b>.

## Run
```sh
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

The result will be recorded in <b>result.csv</b> file. Enjoy!!