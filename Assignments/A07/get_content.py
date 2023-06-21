import asyncio,os
from pyppeteer import launch
from bs4 import BeautifulSoup
currentlocation=os.path.dirname(os.path.abspath(__file__))
async def main(url=None):
    browser = await launch()
    page = await browser.newPage()
    if not url:url='https://www.wunderground.com/history/daily/KLAW/date/2023-6-13'
    await page.goto(url)
    await asyncio.sleep(5)
    await page.waitForSelector('lib-city-history-observation')
    
    content = await page.content()
    # await page.screenshot({'path': currentlocation+'//image.png'})
    await browser.close()
    return content

def get_dynamic_content(url):
    content=asyncio.get_event_loop().run_until_complete(main(url))
    # formatted_html = BeautifulSoup(content, 'html.parser').prettify()
    formatted_html = BeautifulSoup(content)
    table = formatted_html.find('lib-city-history-observation')
    data = []    
    headings = []
    print(table)
    if table:
        rows = table.find_all("tr")
        for row in rows:
            heading_cells = row.find_all("th")
            headings.append([cell.get_text(strip=True) for cell in heading_cells])
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            data.append([cell.get_text(strip=True) for cell in cells])
    print(data,headings)
    return (data,headings)
    # return formatted_html
# get_dynamic_content(None)