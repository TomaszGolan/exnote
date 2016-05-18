from __future__ import print_function

from ConfigParser import SafeConfigParser
import os

_config = os.path.expanduser("~/.exnote.ini")
_bashrc = os.path.expanduser("~/.bashrc")
_autocomplete = 'eval "$(_EXNOTE_COMPLETE=source exnote)"'

cfg = {
    "path":   os.path.expanduser("~/.exnote"),
    "editor": "vi"
}


def _enable_ac():
    with open(_bashrc, 'a') as f:
        f.write('\n' + _autocomplete)


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

        print("\nAuto-complete can be enabled by adding: \
              \n\n    %s\n\nto ~/.bashrc"
              % _autocomplete)

        if raw_input("\nDo you want to enable it now? [Y/N]: ").lower() == 'y':
            _enable_ac()

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
