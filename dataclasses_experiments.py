from typing import List, Dict
from dataclasses import dataclass
from json import loads


@dataclass()
class BattlePveAttributes:
    user_id:        str
    battle_id:      str

    def __post_init__(self):
        ...


def main() -> bool:
    input_json = """{\"user_id\": \"246\", \"battle_id\": \"battle\"}"""
    battle_pve_dict = loads(input_json)
    a = BattlePveAttributes(**battle_pve_dict)
    return True


if __name__ == '__main__':
    main()