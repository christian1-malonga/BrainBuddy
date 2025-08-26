import requests
from bs4 import BeautifulSoup

# URLs to scrape
BASE_URL = "https://www.aionlinecourse.com/"
AI_BASICS_URL = BASE_URL + "ai-basics"
PROJECTS_URL = BASE_URL + "ai-projects"


def get_ai_basics():
    resp = requests.get(AI_BASICS_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    basics = []
    for link in soup.select('a[href^="/ai-basics/"]'):
        title = link.text.strip()
        url = BASE_URL.rstrip('/') + link['href']
        basics.append({"title": title, "url": url})
    return basics


def get_all_courses():
    resp = requests.get(PROJECTS_URL)
    soup = BeautifulSoup(resp.text, "html.parser")
    courses = []
    for link in soup.select('a[href^="/ai-projects/playground/"]'):
        title = link.text.strip()
        url = BASE_URL.rstrip('/') + link['href']
        courses.append({"title": title, "url": url})
    return courses


def main():
    ai_basics = get_ai_basics()
    print("AI Basics:")
    for item in ai_basics:
        print(item)

    courses = get_all_courses()
    print("\nAll Courses:")
    for item in courses:
        print(item)

    # Here you can add code to insert into Django models or save as JSON

if __name__ == "__main__":
    main()
