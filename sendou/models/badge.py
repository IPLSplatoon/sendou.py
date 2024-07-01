"""
Badge
"""


class Badge:
    """
    Represents if a Sendou.ink Badge

    Attributes:
        name (str): Badge Name
        count (int): Badge Count
        image_url (str): Badge Image URL
        gif_url (str): Badge Gif URL
    """
    name: str
    count: int
    image_url: str
    gif_url: str

    def __init__(self, data: dict):
        self.name = data.get("name", "")
        self.count = data.get("count", 0)
        self.image_url = data.get("imageUrl", "")
        self.gif_url = data.get("gifUrl", "")
