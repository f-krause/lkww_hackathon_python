import os
import json
from functools import lru_cache
from typing import List
from truck_agent.api import Location


class HackathonMap:

    @property
    @lru_cache(maxsize=None)
    def locations(self) -> List[Location]:
        return self._parse_locations_from_json()

    @staticmethod
    def _parse_locations_from_json() -> List[Location]:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        resource_path = os.path.join(current_dir, "resources", "map.json")
        print(resource_path)

        if not os.path.exists(resource_path):
            raise FileNotFoundError(
                "map.json file was not found in the resources folder.")

        with open(resource_path, 'r') as f:
            json_content = f.read()
            locations = json.loads(json_content)

        location_list = [Location(**item) for item in locations]

        return location_list


if __name__ == "__main__":
    # For testing purposes, print first three locations
    print(HackathonMap().locations[:3])
