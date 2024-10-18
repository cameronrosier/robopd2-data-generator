import logging
from pathlib import Path

from app.models.equipment.armor import Armor
from app.models.equipment.weapon import Weapon
from app.models.items.runeword import RunewordItem

from app.readers.text_file_reader import read_tsv_to_dict

from typing import List, Union


class RunewordGenerator:
    def __init__(
        self,
        output_dir: str,
        text_files: str,
        table_files: str,
    ) -> None:
        self.output_dir = output_dir
        self.text_files = text_files
        self.table_files = table_files
        self.logger = logging.getLogger(__name__)


    def get_item_type_from_base(self, item_base, item_types):
        for item_type in item_types[1:]:
            if item_type['Code'] == item_base:
                return item_type['ItemType']


    def get_item_bases(self, runeword_line: dict, armor_data: List[dict], weapon_data: List[dict]) -> List[Union[Armor, Weapon]]:
        """Return a list of item bases that can be used to make a runeword"""
        item_types = read_tsv_to_dict(Path(self.text_files) / "ItemTypes.txt")
        # Get number of sockets required
        num_sockets = 0
        for i in range(1, 7):
            if runeword_line[f"Rune{i}"]:
                num_sockets += 1

        # Get allowed item types and excluded types
        allowed_types = []
        for i in range(1, 7):
            if runeword_line[f"itype{i}"]:
                allowed_types.append(runeword_line[f"itype{i}"])

        all_bases = {
            "weapons": [],
            "armor": []
        }


        for allowed_type in allowed_types:
            # Search weapon_data
            try:
                for weapon in weapon_data:
                    if weapon['type'] == allowed_type:
                        if int(weapon['gemsockets']) >= num_sockets:
                            all_bases['weapons'].append(self.get_item_type_from_base(weapon['type'], item_types))
                for armor in armor_data:
                    if armor['type'] == allowed_type:
                        if int(armor['gemsockets']) >= num_sockets:
                            all_bases['armor'].append(self.get_item_type_from_base(armor['type'], item_types))
            except KeyError:
                self.logger.debug(f"KeyError: {allowed_type}")
        
        all_bases['weapons'] = list(set(all_bases['weapons']))
        all_bases['armor'] = list(set(all_bases['armor']))
        return all_bases


    def get_rune_names(self, rune_nums: List[str], misc_data: List[dict]) -> List[str]:
        """Return a list of rune names from a list of rune numbers"""
        rune_names = []
        for rune_num in rune_nums:
            for item in misc_data:
                if rune_num == item['code']:
                    rune_names.append(item['*name'])
        return rune_names


    def generate_runeword_item_data(self) -> List[RunewordItem]:
        """Write all unique item data to a dictionary and return it"""
        self.logger.debug(
            f"Generating runeword item data from {Path(self.text_files) / 'Runes.txt'}"
        )
        runewords = read_tsv_to_dict(Path(self.text_files) / "Runes.txt")
        misc_data = read_tsv_to_dict(Path(self.text_files) / "Misc.txt")
        armor_data = read_tsv_to_dict(Path(self.text_files) / "Armor.txt")
        weapon_data = read_tsv_to_dict(Path(self.text_files) / "Weapons.txt")

        runeword_items = []

        for runeword in runewords[1:]:
            rw_num = runeword['Name']
            name = runeword['Rune Name']
            bases = self.get_item_bases(runeword, armor_data, weapon_data)
            rune_nums = [runeword[f"Rune{i}"] for i in range(1, 7) if runeword[f"Rune{i}"]]
            rune_names = self.get_rune_names(rune_nums, misc_data)
            properties = []

            runeword_items.append(
                {
                    "rw_num": rw_num,
                    "name": name,
                    "bases": bases,
                    "rune_nums": rune_nums,
                    "rune_names": rune_names,
                    "properties": properties
                }
            )

        print(runeword_items)
        return runeword_items
