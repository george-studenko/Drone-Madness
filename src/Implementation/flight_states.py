from enum import Enum, auto

class MessageID(Enum):
    STATE = auto()

class States(Enum):
    MANUAL = 0
    ARMING = 1
    TAKEOFF = 2
    IN_MISSION = 3
    WAYPOINT = 4
    LANDING = 5
    DISARMING = 6
    DEBUG_SENSORS = 7
