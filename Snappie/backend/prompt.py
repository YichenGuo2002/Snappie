import requests
from bs4 import BeautifulSoup
import re
import json

def translateToArray(digits):
    result = []
    for digit in digits:
        if(digit in "."):
            result.append(0)
        elif(digit in '0123456789'):
            result.append(int(digit))
    return result

def scrapeNYTimes(difficulty):
    URL = "https://www.nytimes.com/puzzles/sudoku/hard"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    scripts = soup.find('script', string=re.compile('window.gameData')).text
    data = scripts.split("=", 1)[1]
    ld = json.loads(data)
    return ld[difficulty]['puzzle_data']['puzzle']