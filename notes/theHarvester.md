# theHarvester

## K čemu slouží?
Slouži k tomu aby byl použit během reconnaissance stage (fáze sběru informací [viz. kyp]) při red team assessment nebi při penetestu.
Provádí OSINT (open source intelligence)
Sbírá z veřejných zdrojů (legální) jména, emaily, IPs, subdomains, URLs
## Dependencies
Python 3.12 or higher
https://github.com/laramies/theHarvester/wiki/Installation
a nějaký UV
## Co mě překvapilo v kódu?
- skoro ke každé akci tu je napsané co má program vypsat pokud ta dana funkce nefunguje
- main.py pracuje s moduly dané služby př.
```
elif engineitem == 'gitlab':
                    try:
                        gitlab_search = gitlabsearch.SearchGitlab(word)
                        stor_lst.append(
                            store(
                                gitlab_search,
                                engineitem,
                                store_host=True,
                                store_emails=True,
```


