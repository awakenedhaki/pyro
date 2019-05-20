import os
import time
import random

from typing import Dict

from definitions import ROOT_DIR

def delay():
    """
    Will pause the main thread of operation.
    """
    second = random.choice(range(10))
    time.sleep(second)

def headers_rand_user_agent() -> Dict[str, str]:
    """
    Identification spoofing (cloaking), selecting random user-agents.
    """
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-CA,en;q=0.9,es-PE;q=0.8,es;q=0.7,en-GB;q=0.6,en-US;q=0.5",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "rosalind.info",
        "Referer": "http://rosalind.info/problems/locations/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": random_user_agent()
    }
    return headers

def random_user_agent() -> str:
    """
    Selects a random user-agent from user_agents.txt
    """
    path = os.path.join(ROOT_DIR, "user_agents.txt")
    with open(path, "r") as infile:
        lines = infile.readlines()
    return random.choice(lines).strip()
