"""
Badge
"""


class Badge:
    name: str
    count: int
    image_url: str
    gif_url: str

    def __init__(self, data: dict):
        self.name = data.get("name")
        self.count = data.get("count")
        self.image_url = data.get("imageUrl")
        self.gif_url = data.get("gifUrl")
