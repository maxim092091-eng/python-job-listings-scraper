from python_job_listings_scraper import scraper


example = """
<div class="card-content">
    <h2 class="title is-5">Senior Python Developer</h2>
    <h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
    <p class="location">Stewartbury, AA</p>
    <a class="card-footer-item" href="https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html">Apply</a>
</div>
"""

result = [
    {
        "title": "Senior Python Developer",
        "company": "Payne, Roberts and Davis",
        "location": "Stewartbury, AA",
        "job_detail_url": "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html",
    }
]

example_1 = """
<div class="card-content">
    <h3 class="subtitle is-6 company">Payne, Roberts and Davis</h3>
    <p class="location">Stewartbury, AA</p>
</div>
"""

result_1 = [
    {
        "title": None,
        "company": "Payne, Roberts and Davis",
        "location": "Stewartbury, AA",
        "job_detail_url": None,
    }
]


def test_page_parse():
    assert scraper.scrape_jobs(example) == result


def test_page_parse_when_title_and_link_missing():
    assert scraper.scrape_jobs(example_1) == result_1
