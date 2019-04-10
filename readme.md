# Application programming interfaces(APIs)
## Prepared for DAT-129 at the CCAC

Codd samples for studnets to reference in creating simple python programs which scrape data from websites and display results in user friendly ways. You may explore [student work samples on our website][idx] on our class work upload index

## coding resources
[python requests module  offical documentation](http://docs.python-requests.org/en/master/)

[idx]: https://github.com/edarsow/python2

![picture](0c31094c2b9165ca76c725a9f9e876b4.jpg)

# uses for web scraping
1. Learning the ins and outs pf html
2. Extracting data from web which don't run a formal data extraction api
3. Exploring tree-based data structures
        this is coputer<code>that is automatically
        import requests
        from bs4 import BeautifulSoup
        url='https://www.archdaily.com/articles?ad_name=main-menu'
        response=requests.get(url)

        soup = BeautifulSoup(response.text,'html.parser')
        l=soup.findAll(class_='date-publication afd-mobile-margin')

        name=BeautifulSoup(response.text,'html.parser')
        s=name.findall(class_='afd-title-big afd-title-big--bmargin-small afd-mobile-margi')

        for item in l:
            if item=='08:00 - 30 March, 2019':
                for i in s:
                    print(i.text)


            #print(item.text)

