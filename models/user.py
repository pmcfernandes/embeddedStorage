from models.base_model import BaseModel


class User(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = ""
        self.password = ""
        self.name = ""
        self.email = ""

