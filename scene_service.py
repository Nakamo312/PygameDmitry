
import logging
from scene import Scene


class SceneService():
    def __init__(self):
        self.scenes: dict[str, Scene] = dict()
        self.curent_scene: Scene = Scene("deafault")
    
    def create_scene(self, id: str):
        counter = 0
        tmp_id = id
        while id in self.scenes:
            id = f"{tmp_id}{counter}"
        self.scenes[id] = Scene(id)
        logging.info(f"[SceneService]: scene with id {id} is created")
    
    def set_active_scene(self, id: str):
        if id in self.scenes:
            self.curent_scene = self.scenes[id]
        else:
            logging.error(f"[SceneService]: scene with id {id} does not exists")
        logging.info(f"[SceneService]: scene with id {id} is active")
    
    def clear_scene(self, id: str):
        if id in self.scenes:
            self.scenes[id].clear()
        else:
            logging.error(f"[SceneService]: scene with id {id} does not exists")
        logging.info(f"[SceneService]: scene with id {id} is cleared")
    
    