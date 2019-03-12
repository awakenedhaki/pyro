from typing import List

from model.Problem import Problem

class ProblemHTMLParser():

    problem = None

    def parseHTML(self, soup, problem: Problem) -> None:
        """
        Parses HTML of a rosalind problem into Problem fields.
        :param problem: Problem
        :param soup: BeautifulSoup object
        :return: None
        """
        # Set problem as class variable
        ProblemHTMLParser.problem = problem
        # Remove all blockquote tags from HTML
        soup.find("blockquote").extract()
        # Gets header of HTML, and sets problem.title
        ProblemHTMLParser.problem.title = \
            soup.h1.get_text().split("solved")[0].strip()
        # Gets paragraphs of HTML
        paragraphs = soup \
            .find("div", class_="problem-statement") \
            .find_all("p")
        # Re-structures HTML paragraphs, and sets problem.body
        ProblemHTMLParser.problem.body = "".join([paragraph.get_text().replace("\n", " ") + "\n"
                             for paragraph in paragraphs]).replace("$", "")
        self.parseHTMLSample(soup)
        self.parseHTMLTopics(soup) # Not all problems have topics
        return problem

    def parseHTMLTopics(self, soup):
        """
        Parse topics of a given problem HTML, and sets problem.topics
            If AttributeError exception, set topics to None.
        :param soup: BeautifulSoup
        :return: None
        """
        try:
            tempTopics = soup.find("p", class_="topics") \
                .get_text() \
                .split(":")[1] \
                .split(",")
            ProblemHTMLParser.problem.topics = \
                ", ".join([tempTopic.strip() for tempTopic in tempTopics])
        except AttributeError as e:
            # If there are no tags
            ProblemHTMLParser.problem.topics = None

    def parseHTMLSample(self, soup):
        """
        Parse sample dataset and output from problem HTML and
        sets it to problem.data and problem.output
            If ValueError exception is thrown, then set self.data and self.output
            to None
        :param soup: BeautifulSoup
        :return: None
        """
        try:
            sample: List[str] = []
            # Only want the last two codehilite tags in any problem.
            #   codehilite is the HTML tag for sample data and sample output
            for codehilite in soup.find_all("div", class_="codehilite")[-2:]:
                sample.append(codehilite.get_text().strip())
            ProblemHTMLParser.problem.data, ProblemHTMLParser.problem.output = sample
        except ValueError:
            # if there is no sample data or sample output
            ProblemHTMLParser.problem.data = None
            ProblemHTMLParser.problem.output = None
