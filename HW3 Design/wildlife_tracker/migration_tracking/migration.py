from typing import Any
from wildlife_tracker.habitat_management.habitat import Habitat

class Migration:
    def __init__(self, 
                 migration_id: int, 
                 start_location: Habitat, 
                 destination: Habitat, 
                 start_date: str, 
                 status: str = "Scheduled"):
        self.migration_id = migration_id
        self.start_location = start_location
        self.destination = destination
        self.start_date = start_date
        self.status = status