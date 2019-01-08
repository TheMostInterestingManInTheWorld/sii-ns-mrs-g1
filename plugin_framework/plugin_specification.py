class PluginSpecification:
    def __init__(self, spec):
        self._spec = spec
        # FIXME: fali symbolic_name

    @property
    def author(self):
        return self._spec.get("author", "")

    @property
    def description(self):
        return self._spec.get("description", "")
    
    @property
    def version(self):
        return self._spec.get("version", "1.0.0")
        
    @property
    def app_version(self):
        return self._spec.get("app_version", "1.0.0")
    
    @property
    def release_notes(self):
        return self._spec.get("release_notes", "")

    @property
    def size(self):
        return self._spec.get("size", 0.0)

