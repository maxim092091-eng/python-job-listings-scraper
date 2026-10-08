import csv

from bs4 import BeautifulSoup


def scrape_jobs(html: str) -> list[dict[str, str | None]]:
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select("div.card-content")

    jobs = []
    for card in cards:
        title = get_text(card.find("h2", class_="title is-5"))
        company = get_text(card.find("h3", class_="subtitle is-6 company"))
        location = get_text(card.find("p", class_="location"))

        job_detail_link = card.find("a", class_="card-footer-item", string="Apply")
        job_detail_url = job_detail_link.get("href") if job_detail_link else None

        jobs.append(
            {
                "title": title,
                "company": company,
                "location": location,
                "job_detail_url": job_detail_url,
            }
        )

    return jobs


def get_text(element: str) -> str | None:
    if element is not None:
        return element.get_text(strip=True)

    return None


def export_csv(data: list[dict[str, str]]) -> None:
    with open("job_listings.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file, fieldnames=["title", "company", "location", "job_detail_url"]
        )

        writer.writeheader()

        for item in data:
            writer.writerow(item)
