import json

class PluginManager:
    def __init__(self):
        self._plugins = []

    def activate(self, plugin):
        plugin.activate()
        self._plugins.append(plugin)

    def deactivate(self, plugin):
        plugin.deactivate()
        self._plugins.remove(plugin)

    
    def install(self, path="."):
        from plugin1.plugin import Plugin as P1
        from plugin2.plugin import Plugin as P2
        with open("plugin1/spec.json") as fp:
            spec1 = json.load(fp)
        
        with open("plugin2/spec.json") as fp:
            spec2 = json.load(fp)
        p1 = P1(spec1)
        p2 = P2(spec2)
        self.activate(p1)
        self.activate(p2)
        
        # omoguciti ucitavanje i plugin.py
        # aktivirati plugin
        # dopuni specifikacija instaliranih i aktiviranih pluginova

    def uninstall(self, plugin):
        # deaktivirati plugin
        # izmenimo specifikaciju konfiguracione datoteke da je plugin obrisan
        self.deactivate(plugin)
    

        
