import json

class Config():
    def __init__(self, file=None):
        if file is not None:
            self.set_config(file)
        else:
            default_config = 'config.json'
            local_config = 'local_config.json'
            try:
                self.set_config(local_config)
            except IOError:
                self.set_config(default_config)

    def set_config(self, filename):
        with open(filename, 'r') as f:
            self.config = json.loads(f.read())

    @property
    def dict(self):
        return self.config

    @property
    def net(self):
        return self.config['siec']


class ConfigPL(Config):
    @property
    def siec(self):
        return self.net



if __name__ == '__main__':
    cfg_pl = ConfigPL()
    print(cfg_pl.siec)