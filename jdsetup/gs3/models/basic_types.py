from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:schemas-johndeere-com:BasicTypes"


@dataclass
class FileSchemaContentVersion:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    major: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    minor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Node:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    last_seen: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastSeen",
            "type": "Attribute",
        }
    )


@dataclass
class RepresentationSystemVersion:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    major: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    minor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UnitOfMeasureVersion:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    major: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    minor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class NodeVersions:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    node: Optional[Node] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
        }
    )


@dataclass
class Synchronization:
    class Meta:
        namespace = "urn:schemas-johndeere-com:BasicTypes"

    node_versions: Optional[NodeVersions] = field(
        default=None,
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
