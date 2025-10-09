from bs4 import BeautifulSoup

with open("viff_day.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

titles = [t.get_text(strip=True) for t in soup.select("h3.c-calendar-instance__title")]

print(titles)