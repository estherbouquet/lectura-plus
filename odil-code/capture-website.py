#!/usr/bin/python3
import asyncio, os, time, uuid
from pyppeteer import launch
from flask import Flask, send_file, request, after_this_request
app = Flask(__name__)
loop = asyncio.get_event_loop()

async def screenshotasync(url, path, css):
    print("Capturing "+url+" in "+path+" with CSS "+css)
    browser = await launch({'headless': True, 'args': ['--no-sandbox']},
            handleSIGINT=False,
            handleSIGTERM=False,
            handleSIGHUP=False)
    page = await browser.newPage()
    await page.setViewport({'width': 384, 'height': 150})
    await page.goto(url, options={'waitUntil': ['load', 'domcontentloaded', 'networkidle0']})

    # Remove website stylesheets and style
    await page.evaluate("() => [...document.querySelectorAll('link'), ...document.querySelectorAll('style')].filter(e => e.parentNode).forEach(e => e.parentNode.removeChild(e))") 

    # Remove website javascript
    await page.evaluate("() => [...document.querySelectorAll('script')].filter(e => e.parentNode).forEach(e => e.parentNode.removeChild(e))") 

    # Inject my CSS stylesheet
    await page.evaluate("() => { const l = document.querySelector('head').appendChild(document.createElement('link')); l.rel='stylesheet'; l.type='text/css'; l.href='"+css+"'; l.onload = () => l.classList.add('css-loaded'); }")
    #à remplacer par une url de mon site estherbouquet.com/rss-essor.css par ex -> injecte le fichier css à la fin du head de la page vers laquelle on pointe

    # *To debug, copy/paste the javascript in your browser console prefixed with `let code = ` and run it with `code()`*

    # First, we wait for our CSS then we check that it has been applied
    await page.waitFor('.css-loaded');
    await page.waitForSelector('.footer', options ={'hidden': True});

    # Take a screenshot
    time.sleep(2)
    await page.screenshot({'path': path, 'fullPage': True})
    await browser.close()

def screenshot(url, path, css):
    asyncio.get_event_loop().run_until_complete(screenshotasync(url, path, css))


@app.route('/capture/<path:url>')
def capture(url):
    css = "https://estherbouquet.com/ODIL/main-odil.css"
    filename = os.path.join(os.getcwd(),str(uuid.uuid4())+'.png')
    loop.run_until_complete(screenshotasync(url, filename, css))

    @after_this_request
    def remove_file(response):
        try:
            os.remove(filename)
        except Exception as error:
            app.logger.error("Error removing or closing downloaded file handle", error)
        return response
    return send_file(filename)

app.run(host='0.0.0.0')
#screenshot("https://www.lessor42.fr/quand-la-lumiere-jaillit-sur-l-abbaye-de-charlieu-22583.html", "33f0dfeb-a31b-4382-bf78-3832b4d08938.png", "https://estherbouquet.com/ODIL/main-odil.css")
