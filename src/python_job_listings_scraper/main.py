from .api import fetch_page
from .scraper import scrape_jobs, export_csv


def main() -> None:
    url = "https://realpython.github.io/fake-jobs/"

    try:
        html = fetch_page(url)

        job_list = scrape_jobs(html)

        export_csv(job_list)

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
