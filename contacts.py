import json

class Contact():
    def read(path) -> list:
        """
        This function will return a list of contacts
        """
        with open(path, 'r', encoding='utf8') as f:
            return json.load(f)

    def write(path, dados):
        with open(path, 'w', encoding='utf8') as f:
            json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))