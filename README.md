# cgxSubOptimal
Enable or disable per prefix ARP

Instructions:

* Install python3
* Install cloudgenix python sdk : pip3 install cloudgenix
* Setup authentication as listed below
* Create a csv file with the example at devicelist.csv
* run the script using: python3 cgxPerPrefixARP.py --all --enable
* You can also specify a text file with a list to site names, each site in its own line, that will be affected by the script: python3 [cgxPerPrefixARPSubOptimal py](cgxPerPrefixARPSubOptimal.py) --site_file sites.txt --enable

cgxSubOptimal.py looks for the following for AUTH, in this order of precedence:

* --email or --password options on the command line.
* CLOUDGENIX_USER and CLOUDGENIX_PASSWORD values imported from cloudgenix_settings.py
* CLOUDGENIX_AUTH_TOKEN value imported from cloudgenix_settings.py
* X_AUTH_TOKEN environment variable
* AUTH_TOKEN environment variable
* Interactive prompt for user/pass (if one is set, or all other methods fail.)

Exmpale:
```
~/proj/cgxPerPrefixARP$ ./cgxPerPrefixARP.py --all --enable
INFO:PerPrefixARP:Death Valley at Death Valley is being configured
INFO:PerPrefixARP:-- already have fcconfig
INFO:PerPrefixARP:-- updating fcconfig entry
INFO:PerPrefixARP:Raphael's Test at Raphael's Test Branch is being configured
INFO:PerPrefixARP:-- creating fcconfig namespace
INFO:PerPrefixARP:Dan 2k at Dan Home is being configured
INFO:PerPrefixARP:-- already have fcconfig
INFO:PerPrefixARP:-- updating fcconfig entry
INFO:PerPrefixARP:Rich-ION2K-1 at Rich-Home is being configured
INFO:PerPrefixARP:-- creating fcconfig namespace
INFO:PerPrefixARP:Dmitry-Home at Dmitry-Site is being configured
INFO:PerPrefixARP:-- creating fcconfig namespace
INFO:PerPrefixARP:Alireza Test at Alireza Test Branch is being configured
INFO:PerPrefixARP:-- creating fcconfig namespace
INFO:PerPrefixARP:Leo Home ION7k at Leo-Home is being configured
INFO:PerPrefixARP:-- creating fcconfig namespace
INFO:PerPrefixARP:Kamal's ION2K at Kamal's home is being configured
INFO:PerPrefixARP:-- creating fcconfig namespace
INFO:PerPrefixARP:Rich-ION2K-2 at Rich-Home is being configured
INFO:PerPrefixARP:-- creating fcconfig namespace
INFO:PerPrefixARP:ID-300-SD1A at ID-300-FAIRVIEW is being configured
INFO:PerPrefixARP:-- creating fcconfig namespace
```
