from __future__ import print_function

from ConfigParser import SafeConfigParser
import os

_config = os.path.expanduser("~/.exnote.ini")

cfg = {
    "path":   os.path.expanduser("~/.exnote"),
    "editor": "vi"
}


def cfg_init():
    _cfg = SafeConfigParser()

    if not os.path.isfile(_config):
        print("\nFirst run configuration (ENTER to default):\n")

        _cfg.add_section("SETTINGS")

        for o, v in cfg.items():
            v = raw_input("Set %s (default: %s): " % (o, v)) or v
            _cfg.set("SETTINGS", o, v)

        with open(_config, 'w') as f:
            _cfg.write(f)

        print("\nDone. You can change your settings in %s\n" % _config)

    _cfg.read(_config)

    for o in cfg:
        try:
            cfg[o] = _cfg.get("SETTINGS", o)
        except:
            pass

    if not os.path.exists(cfg['path']):
        os.makedirs(cfg['path'])

    if not os.path.exists(os.path.join(cfg['path'], ".meta")):
        os.makedirs(os.path.join(cfg['path'], ".meta"))
