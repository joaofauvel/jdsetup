from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

__NAMESPACE__ = "urn:schemas-johndeere-com:SpatialTypes"


@dataclass
class Mbr:
    class Meta:
        name = "MBR"
        namespace = "urn:schemas-johndeere-com:SpatialTypes"

    uom_source: Optional[str] = field(
        default=None,
        metadata={
            "name": "uomSource",
            "type": "Attribute",
        }
    )
    uom_target: Optional[str] = field(
        default=None,
        metadata={
            "name": "uomTarget",
            "type": "Attribute",
        }
    )
    north: Optional[Union[float, Decimal]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    south: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    east: Optional[Union[float, Decimal]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    west: Optional[Union[Decimal, float]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DtSignalType:
    class Meta:
        name = "dtSignalType"
        namespace = "urn:schemas-johndeere-com:SpatialTypes"

    value: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    defined_type_representation: Optional[str] = field(
        default=None,
        metadata={
            "name": "definedTypeRepresentation",
            "type": "Attribute",
        }
    )
