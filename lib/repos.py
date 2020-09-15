''' Defining the Repository class '''
class Repos():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._forks = data['forks']
        self._language = data['language']
        self._save()

    def __str__(self):
        return f'Behold, {self._name}'

    def _save(self):
        self.all.append(self._name)

    def get_name(self):
        return self._name
