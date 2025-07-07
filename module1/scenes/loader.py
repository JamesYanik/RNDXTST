class SceneLoader:
    def __init__(self, scene):
        self.scene = scene

    def load(self):
        return self.scene


class Scene:
    id: str
    name: str
    levels: int
