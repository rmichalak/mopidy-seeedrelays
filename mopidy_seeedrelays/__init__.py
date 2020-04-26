import logging
import pathlib

import pkg_resources

from mopidy import config, ext

__version__ = pkg_resources.get_distribution("Mopidy-SeeedRelays").version


class Extension(ext.Extension):

    dist_name = "Mopidy-SeeedRelays"
    ext_name = "seeedrelays"
    version = __version__

    def get_default_config(self):
        return config.read(pathlib.Path(__file__).parent / "ext.conf")

    def get_config_schema(self):
        schema = super().get_config_schema()
        schema["i2c"] = config.Integer()
        schema["address"] = config.String()
        schema["relay"] = config.Integer()
        return schema

    def setup(self, registry):
        from .frontend import SeeedRelaysFrontend
        registry.add("frontend", SeeedRelaysFrontend)

