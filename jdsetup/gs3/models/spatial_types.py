from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

__NAMESPACE__ = "urn:schemas-johndeere-com:SpatialTypes"


@dataclass
class Mbr:
    class Meta:
        name = "MBR"
        namespace = "urn:schemas-johndeere-com:SpatialTypes"

    uom_source: str = field(
        default='arcdeg',
        metadata={
            "name": "uomSource",
            "type": "Attribute",
        }
    )
    uom_target: str = field(
        default='arcdeg',
        metadata={
            "name": "uomTarget",
            "type": "Attribute",
        }
    )
    north: Optional[float] = field(
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
    east: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    west: Optional[float] = field(
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

    value: str = field(
        default='dtiSignalTypeUnknown',
        metadata={
            "type": "Attribute",
        }
    )
    defined_type_representation: str = field(
        default='dtSignalType',
        metadata={
            "name": "definedTypeRepresentation",
            "type": "Attribute",
        }
    )
