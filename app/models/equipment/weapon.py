from app.util.util import empty_str_to_zero

class Weapon:

    def __init__(self, weapon_data):
        self.weapon_data = weapon_data
        self.name = weapon_data["name"]
        self.one_or_two_handed = weapon_data["1or2handed"] == "1"
        self.two_handed = weapon_data["2handed"] == "1"
        self.thrown = self.is_thrown()
        self.damage_values = self.get_damage_values()
        self.level = int(weapon_data["level"])
        self.required_strength = empty_str_to_zero(weapon_data["reqstr"])
        self.required_dexterity = empty_str_to_zero(weapon_data["reqdex"])
        self.durability = int(weapon_data["durability"])
        self.type = weapon_data["type"]
        self.sockets = empty_str_to_zero(weapon_data["gemsockets"])
        self.code = weapon_data["code"]


    def is_thrown(self) -> bool:
        if self.weapon_data['minmisdam'] != "":
            return True
        return False

    def get_damage_values(self) -> dict:
        print(self.weapon_data['name'])
        damage_values = {}
        if not self.two_handed:
            damage_values['one_handed'] = {'min': int(self.weapon_data['mindam']), 'max': int(self.weapon_data['maxdam'])}
        elif self.one_or_two_handed:
            damage_values['one_handed'] = {'min': int(self.weapon_data['mindam']), 'max': int(self.weapon_data['maxdam'])}
        
        if self.two_handed:
            damage_values['two_handed'] = {'min': int(self.weapon_data['2handmindam']), 'max': int(self.weapon_data['2handmaxdam'])}
        
        if self.thrown:
            damage_values['thrown'] = {'min': int(self.weapon_data['minmisdam']), 'max': int(self.weapon_data['maxmisdam'])}

        return damage_values
    
    def __dict__(self):
        return {
            'name': self.name,
            'one_or_two_handed': self.one_or_two_handed,
            'two_handed': self.two_handed,
            'thrown': self.thrown,
            'damage_values': self.damage_values,
            'level': self.level,
            'required_strength': self.required_strength,
            'required_dexterity': self.required_dexterity,
            'durability': self.durability,
            'type': self.type,
            'sockets': self.sockets,
            'code': self.code
        }