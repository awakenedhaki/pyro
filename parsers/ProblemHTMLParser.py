from model.Problem import Problem

class ProblemHTMLParser():

    problem = None

    def parseHTML(self, soup, problem: Problem) -> None:
        """
        Parses HTML of a rosalind problem into Problem fields.
        :param problem:
        :param soup: BeautifulSoup object
        :return: None
        """
        # Set problem as class variable
        ProblemHTMLParser.problem = problem
        # Remove all blockquote tags from HTML
        soup.find("blockquote").extract()
        ProblemHTMLParser.problem.title = \
            soup.h1.get_text().split("solved")[0].strip()
        paragraphs = soup \
            .find("div", class_="problem-statement") \
            .find_all("p")
        ProblemHTMLParser.problem.body = "".join([paragraph.get_text().replace("\n", " ") + "\n"
                             for paragraph in paragraphs]).replace("$", "")
        self.parseHTMLSample(soup)
        # Not all problems have a Topic
        self.parseHTMLTopics(soup)
        return problem

    def parseHTMLTopics(self, soup):
        """
        Parse topics of a given problem HTML.
        If AttributeError exception, set topics to None.
        :param soup: BeautifulSoup
        :return: None
        """
        try:
            tempTopics = soup.find("p", class_="topics") \
                .get_text() \
                .split(":")[1] \
                .split(",")
            ProblemHTMLParser.problem.topics = ", ".join([tempTopic.strip() for tempTopic in tempTopics])
        except AttributeError as e:
            ProblemHTMLParser.problem.topics = None

    def parseHTMLSample(self, soup):
        """
        Parse sample dataset and output from problem HTML.
        If ValueError exception is thrown, then set self.data and self.output
        to None
        :param soup: BeautifulSoup
        :return: None
        """
        try:
            sample = []
            # Only want the last two codehilite tags in any problem.
            for codehilite in soup.find_all("div", class_="codehilite")[-2:]:
                codehilite_text = codehilite.get_text().strip()
                if not codehilite_text.startswith("http"):
                    sample.append(codehilite_text)
            ProblemHTMLParser.problem.data, ProblemHTMLParser.problem.output = sample
        except ValueError:
            ProblemHTMLParser.problem.data = None
            ProblemHTMLParser.problem.output = None
