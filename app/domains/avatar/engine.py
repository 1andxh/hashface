import hashlib
from enum import Enum
from dataclasses import dataclass


GRID_SIZE = 5
HALF_COLS = 3
BODY_CELL_COUNT = 12
DEFAULT_SIZE, MIN_SIZE, MAX_SIZE = 250, 16, 1024
ENGINE_VERSION = 1
EYE_POSITIONS = ((1,1), (1,3))
MOUTH_ROW = 3
RESERVED_HALF_CELLS = frozenset({(1,1), (1,3), (2,3)})

class EyeExpression(Enum):
    NEUTRAL = 0
    SQUINT = 1
    HAPPY = 2
    WIDE = 3

class MouthExpression(Enum):
    NEUTRAL = 0
    SMILE = 1
    FROWN = 2
    OPEN = 3


@dataclass(frozen=True)
class HashDNA:
    digest: bytes

    # def hash_seed(seed: str):
    #     digest = hashlib.sha256(seed.encode("utf-8")).digest()
  
    @classmethod
    def from_seed(cls, seed: str):
        return cls(hashlib.sha256(seed.encode("utf-8")).digest())

    @property
    def base_color(self) -> tuple[int, int, int, int]:
        return tuple(self.digest[0:3])

    @property
    def accent_color(self) -> tuple[int, int, int, int]:
        return tuple(self.digest[3:6])
        

    @property
    def eye_expression(self) -> EyeExpression:
        return EyeExpression(self.digest[6] % 4)
        

    @property
    def mouth_expression(self) -> MouthExpression:
        return MouthExpression(self.digest[7] % 4)
        

