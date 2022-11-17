from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:schemas-johndeere-com:BasicTypes"


@dataclass
class FileSchemaContentVersion:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    major: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    minor: int = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Node:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    uuid: str = field(
        metadata={
            "type": "Attribute",
        }
    )
    last_seen: XmlDateTime = field(
        metadata={
            "name": "lastSeen",
            "type": "Attribute",
        }
    )


@dataclass
class RepresentationSystemVersion:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    major: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    minor: int = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UnitOfMeasureVersion:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    major: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    minor: int = field(
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NodeVersions:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    node: Node = field(
        metadata={
            "name": "Node",
            "type": "Element",
        }
    )


@dataclass
class Synchronization:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    node_versions: NodeVersions = field(
        metadata={
            "name": "NodeVersions",
            "type": "Element",
        }
    )
    entity_deletions: Optional[object] = field(
        default=None,
        metadata={
            "name": "EntityDeletions",
            "type": "Element",
        }
    )
