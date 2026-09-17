from dataclasses import dataclass, field

@dataclass
class OrderedPair:
    """
    Represents a point or vector in two-dimensional space.

    Attributes:
        x (float): The x-coordinate of the point or vector.
        y (float): The y-coordinate of the point or vector.
    """
    x: float = 0.0
    y: float = 0.0

@dataclass
class Body:
    name: str = ""
    mass: float = 0.0
    radius: float = 0.0
    position: OrderedPair = field(default_factory=OrderedPair)
    velocity: OrderedPair = field(default_factory=OrderedPair)
    acceleration: OrderedPair = field(default_factory=OrderedPair)
    red: int = 0
    green: int = 0
    blue: int = 0  

@dataclass
class Universe:
    bodies: list[Body] = field(default_factory=list)
    width: float = 0.0
    gravitationalConstant: float = 0.0
