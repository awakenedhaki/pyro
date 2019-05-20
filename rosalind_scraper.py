import json

from scraper.problem_scraper import ProblemScraper
from persistence.encoder import EnhancedJSONEncoder

def main():
    scraper = ProblemScraper()
    problems = {
        f"{i}-{problem.id}": problem for i, problem in enumerate(scraper.run())
    }
    with open("problems.json", "w") as outfile:
        json.dump(problems, outfile, cls=EnhancedJSONEncoder)


if __name__ == "__main__":
    main()
