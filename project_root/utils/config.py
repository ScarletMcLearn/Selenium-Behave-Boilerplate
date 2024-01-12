# config.py
import configparser
import os

class Config:
    def __init__(self):
        """
        Configuration class for reading values from the config file.

        Reads values from the 'config.ini' file, sets configuration parameters, and provides methods
        for accessing configuration values.
        """
        self.config = configparser.ConfigParser()
        self.config.read(self.get_config_file_path())

        # Print the sections for debugging
        print(f"Sections in the config file: {self.config.sections()}")

        # Set configuration parameters
        self.base_url = self.get_config_value('General', 'BaseURL')
        self.browser = self.get_config_value('General', 'Browser')

        # Set valid user credentials
        self.valid_username = self.get_config_value('ValidUserCredentials', 'Username')
        self.valid_password = self.get_config_value('ValidUserCredentials', 'Password')

    def get_config_file_path(self):
        """
        Get the path to the configuration file.

        :return: Full path to the configuration file.
        """
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.ini')

    def get_config_value(self, section, key):
        """
        Get the value for a given key in a specific section of the configuration file.

        :param section: The section in the configuration file.
        :param key: The key for which the value is to be retrieved.
        :return: The value associated with the specified key in the given section.
        :raises ValueError: If the section or key is not found in the configuration file.
        """
        try:
            return self.config.get(section, key)
        except configparser.NoOptionError:
            raise ValueError(f"No option '{key}' in section '{section}' found in the config file.")
        except configparser.NoSectionError:
            raise ValueError(f"No section '{section}' found in the config file.")

# Testing
# # Instantiate the Config class
# config = Config()

# # # Use the configuration values
# print(f"BaseURL: {config.base_url}")
# print(f"Browser: {config.browser}")
# print(f"Valid Username: {config.valid_username}")
# print(f"Valid Password: {config.valid_password}")
