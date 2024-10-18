class Armor:

    def __init__(self, armor_data):
        self.armor_data = armor_data
        self.name = armor_data["name"]
        self.item_type = armor_data["type"]
        self.min_ac = int(armor_data["minac"])
        self.max_ac = int(armor_data["maxac"])
        self.req_str = int(armor_data["reqstr"])
        self.req_dex = int(armor_data["reqdex"])
        self.durability = int(armor_data["durability"])
        self.block = int(armor_data["block"])
        self.sockets = int(armor_data["gemsockets"])
        self.level = int(armor_data["level"])
        self.code = armor_data["code"]

    def __dict__(self):
        return {
            "name": self.name,
            "item_type": self.item_type,
            "min_ac": self.min_ac,
            "max_ac": self.max_ac,
            "req_str": self.req_str,
            "req_dex": self.req_dex,
            "durability": self.durability,
            "block": self.block,
            "sockets": self.sockets,
            "level": self.level,
            "code": self.code,
        }