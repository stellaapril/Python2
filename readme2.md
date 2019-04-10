## Archdaily Scraping
![](250px-ArchDaily.svg.png)
# architecture
# python
# daily news

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
          

            print(item.text)
