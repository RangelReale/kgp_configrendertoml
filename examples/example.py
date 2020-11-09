from kubragen.configfile import ConfigFileOutput_Dict

from kgp_configrendertoml import ConfigFileRender_TOML

renderer = ConfigFileRender_TOML()
print(renderer.render(ConfigFileOutput_Dict({
    'x': 1,
    'y': {
        'y1': 2,
        'y2': [3, 4, 5],
        'z': {
            'z1': 10,
            'z2': '11',
        },
    },
})))
