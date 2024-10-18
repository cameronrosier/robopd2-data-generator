from dataclasses import dataclass
from typing import List


@dataclass
class RunewordItem(dict):
    rw_num: str
    name: int
    bases: List[str]
    rune_nums: List[str]
    rune_names: List[str]
    properties: List[dict]

    def __dict__(self):
        return {
            "rw_num": self.rw_num,
            "name": self.name,
            "bases": self.bases,
            "rune_nums": self.rune_nums,
            "rune_names": self.rune_names,
            "properties": self.properties,
        }