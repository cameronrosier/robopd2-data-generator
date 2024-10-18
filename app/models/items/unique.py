from dataclasses import dataclass
from typing import List


@dataclass
class UniqueItem(dict):
    name: str
    item_level: int
    required_level: int
    item_code: str
    equipment: List[dict]
    properties: List[dict]

    damage_armor_enhanced: bool = False
