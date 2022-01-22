from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_dict = tomli.loads(content)
        name = toml_dict['tool']['poetry']['name']
        description = toml_dict['tool']['poetry']['description'] 
        dependencies = toml_dict['tool']['poetry']['dependencies']
        dev = toml_dict['tool']['poetry']['dev-dependencies']
        return Project(name, description, dependencies, dev)
