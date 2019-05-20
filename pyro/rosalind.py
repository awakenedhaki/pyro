import os
import re
import json

from shutil import copyfile
try:
    from definitions import ROS_DIR, ROOT_DIR
except ImportError:
    from definitions import ROOT_DIR
from model.problems import Problems
from exceptions.ros_exists import RosalindAlreadyExists

class Rosalind(object):

    def __init__(self):
        with open("problems.json", "r") as infile:
            self.problems = Problems(json.load(infile))
        self.lang = None

    def setup(self, path=None):
        try:
            if os.path.exists(ROS_DIR):
                raise RosalindAlreadyExists("Rosalind directory has already been created.")
        except NameError:
            pass
        home = os.getenv("HOME")
        if not path:
            path = os.path.join(home, "rosalind")
            os.mkdir(path)
        elif path:
            path = os.path.join(home, path)
            if os.path.exists(path):
                path = os.path.join(path, "rosalind")
                os.mkdir(path)
        Rosalind.add_path(path)

    def make_problem_dir(self, key):
        os.chdir(ROS_DIR)
        keys = self.problems.find_key(key)
        os.mkdir(keys)
        self.make_problem_files(keys)

    def next_problem(self, lang="py"):
        self.lang = lang
        if len(os.listdir(ROS_DIR)) == 0:
            self.make_problem_dir("0")
        else:
            pattern = re.compile("(\d{,})-.*")
            ros_dir_items = (item for item in os.listdir(ROS_DIR) if not item.startswith("."))
            last_problem = max((int(re.search(pattern, dir).group(1)) 
                                for dir in ros_dir_items))
            next_ = str(last_problem + 1)
            self.make_problem_dir(next_)

    def make_problem_files(self, keys):
        os.chdir(os.path.join(ROS_DIR, keys))
        problem = self.problems[keys]
        with open("README.md", "w") as readme_file:
            readme_file.write(f"# {problem['title']}\n\n")
            readme_file.write(f"{problem['statement']}\n\n")
            readme_file.write(f"{problem['given']}\n\n")
            readme_file.write(f"{problem['return_']}")
        with open("ouput.txt", "w") as output_file:
            output_file.write(f"{problem['output']}")
        with open("input.txt", "w") as input_file:
            input_file.write(f"{problem['input_']}")
        template_path = os.path.join(ROOT_DIR, f"templates/template.{self.lang}")
        dst_path = os.path.join(ROS_DIR, keys, f"{problem['id']}.{self.lang}")
        copyfile(template_path, dst_path)
        
    @staticmethod
    def add_path(path):
        definitions_path = os.path.join(ROOT_DIR, "definitions.py")
        home = os.getenv("HOME")
        path = path.replace(home, "")[1:]
        with open(definitions_path, "a") as outfile:
            outfile.write(f"ROS_DIR = os.path.join(HOME, \"{path}\")")
