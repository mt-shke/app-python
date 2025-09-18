import json

class JsonManager:
    path : str


    def __init__(self, path : str):
        self.path = path

    def load(self) -> dict:
        with open(self.path, "r") as file:
            return json.load(file)
    
    def write(self, content) -> None:
        hold_content = self.load()
        hold_content.update(content)
        with open(self.path, "w") as file:
            json.dump(hold_content, file, indent=4)