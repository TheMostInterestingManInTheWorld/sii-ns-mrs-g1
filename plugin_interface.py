class PluginInterface:
    def __init__(self):
        super().__init__()
    
    def activate(self):
        raise NotImplementedError()

    def deactivate(self):
        raise NotImplementedError()
