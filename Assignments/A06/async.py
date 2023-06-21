import asyncio,os
from pyppeteer import launch
from bs4 import BeautifulSoup
currentlocation=os.path.dirname(os.path.abspath(__file__))
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.wunderground.com/history/daily/KLAW/date/2023-6-13')
    content = await page.content()
    await page.screenshot({'path': currentlocation+'//image.png'})
    await browser.close()
    return content

content=asyncio.get_event_loop().run_until_complete(main())
formatted_html = BeautifulSoup(content, 'html.parser').prettify()
with open(currentlocation+"//data.html",'w',encoding='utf-8') as f:
        f.writelines(formatted_html)
    