import configparser
import os

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.get_config_file_path())

        # Set configuration parameters
        self.base_url = self.get_config_value('General', 'BaseURL')
        self.browser = self.get_config_value('General', 'Browser')

    def get_config_file_path(self):
        # Assuming the config file is in the 'config' directory
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

    def get_config_value(self, section, key):
        try:
            return self.config.get(section, key)
        except configparser.NoOptionError:
            raise ValueError(f"No option '{key}' in section '{section}' found in the config file.")

# Example config.ini file:
# [General]
# BaseURL = https://example.com
# Browser = chrome
