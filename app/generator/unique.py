import logging
from pathlib import Path

from app.models.items.unique import UniqueItem

from app.models.equipment.armor import Armor
from app.models.equipment.weapon import Weapon

from app.readers.text_file_reader import read_tsv_to_dict

from typing import List, Union


class UniqueGenerator:
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


    def _get_equipment_stats(
        self, item_code: str, armor_data: List[dict], weapon_data: List[dict]
    ) -> Union[Armor, Weapon, str]:
        """Return the equipment type of the item code"""
        
        for armor in armor_data:
            try:
                if armor["code"] == item_code:
                    return Armor(armor).__dict__
            except KeyError as ex:
                print(f"Armor {armor['name']} is missing a code")

        for weapon in weapon_data:
            try:
                if weapon["code"] == item_code:
                    return Weapon(weapon).__dict__
            except KeyError as ex:
                print(f"Weapon {weapon['name']} is missing a code")

        return "jewellery"


    def generate_unique_item_data(self) -> List[UniqueItem]:
        """Write all unique item data to a dictionary and return it"""
        self.logger.debug(
            f"Generating unique item data from {Path(self.text_files) / 'UniqueItems.txt'}"
        )
        unique_items = read_tsv_to_dict(Path(self.text_files) / "UniqueItems.txt")
        armor_data = read_tsv_to_dict(Path(self.text_files) / "Armor.txt")
        weapon_data = read_tsv_to_dict(Path(self.text_files) / "Weapons.txt")

        parsed_unique_items = []

        for item in unique_items:
            if not item["lvl"]:
                self.logger.info(f"Skipping {item['index']} because it has no item level")
                continue
            if not item["lvl req"]:
                self.logger.info(f"Skipping {item['index']} because it has no level requirement")
                continue

            equipment = self._get_equipment_stats(item["code"], armor_data, weapon_data)
        
            unique_item = UniqueItem(
                name=item["index"],
                item_level=item["lvl"],
                required_level=item["lvl req"],
                item_code=item["code"],
                equipment=equipment,
                properties=[]
            )

            self.logger.info(f"Generated unique item: {unique_item.name}")
            parsed_unique_items.append(vars(unique_item))

        return parsed_unique_items
