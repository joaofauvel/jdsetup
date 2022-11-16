from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from jdsetup.gs3.models.rcd.setup import (
    FileSchemaVersion,
    Setup,
    SourceApp,
)
from jdsetup.gs3.models.spatial_types import (
    Mbr,
    DtSignalType,
)

@dataclass
class VrEastShiftComponent:
    class Meta:
        name = "vrEastShiftComponent"
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    source_uom: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: Optional[str] = field(
        default=None,
        metadata={
            "name": "variableRepresentation",
            "type": "Attribute",
        }
    )


@dataclass
class VrNorthShiftComponent:
    class Meta:
        name = "vrNorthShiftComponent"
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    source_uom: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: Optional[str] = field(
        default=None,
        metadata={
            "name": "variableRepresentation",
            "type": "Attribute",
        }
    )


@dataclass
class VrReferenceLatitude:
    class Meta:
        name = "vrReferenceLatitude"
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base"

    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    source_uom: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: Optional[str] = field(
        default=None,
        metadata={
            "name": "variableRepresentation",
            "type": "Attribute",
        }
    )


@dataclass
class VrReferenceLongitude:
    class Meta:
        name = "vrReferenceLongitude"
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base"

    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    source_uom: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: Optional[str] = field(
        default=None,
        metadata={
            "name": "variableRepresentation",
            "type": "Attribute",
        }
    )


@dataclass
class HeadlandLookup:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Field"

    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    erid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "eridRef",
            "type": "Attribute",
        }
    )


@dataclass
class NameIdpair:
    class Meta:
        name = "NameIDPair"
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Field"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    passable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class VrHeadlandOffset:
    class Meta:
        name = "vrHeadlandOffset"
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Field"

    value: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    source_uom: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: Optional[str] = field(
        default=None,
        metadata={
            "name": "variableRepresentation",
            "type": "Attribute",
        }
    )


@dataclass
class Boundary:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Field"

    last_modified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    source_node: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceNode",
            "type": "Attribute",
        }
    )
    erid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    spatial_geometry_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "spatialGeometryType",
            "type": "Attribute",
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Attribute",
        }
    )
    mbr: Optional[Mbr] = field(
        default=None,
        metadata={
            "name": "MBR",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:SpatialTypes",
        }
    )
    dt_signal_type: Optional[DtSignalType] = field(
        default=None,
        metadata={
            "name": "dtSignalType",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:SpatialTypes",
        }
    )
    name_idpair: List[NameIdpair] = field(
        default_factory=list,
        metadata={
            "name": "NameIDPair",
            "type": "Element",
        }
    )
    headland_lookup: Optional[HeadlandLookup] = field(
        default=None,
        metadata={
            "name": "HeadlandLookup",
            "type": "Element",
        }
    )


@dataclass
class CurvedTrackLine:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Field"

    last_modified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    source_node: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceNode",
            "type": "Attribute",
        }
    )
    erid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    spatial_geometry_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "spatialGeometryType",
            "type": "Attribute",
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    mbr: Optional[Mbr] = field(
        default=None,
        metadata={
            "name": "MBR",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:SpatialTypes",
        }
    )
    dt_signal_type: Optional[DtSignalType] = field(
        default=None,
        metadata={
            "name": "dtSignalType",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:SpatialTypes",
        }
    )
    vr_east_shift_component: Optional[VrEastShiftComponent] = field(
        default=None,
        metadata={
            "name": "vrEastShiftComponent",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base",
        }
    )
    vr_north_shift_component: Optional[VrNorthShiftComponent] = field(
        default=None,
        metadata={
            "name": "vrNorthShiftComponent",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base",
        }
    )
    vr_reference_latitude: Optional[VrReferenceLatitude] = field(
        default=None,
        metadata={
            "name": "vrReferenceLatitude",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base",
        }
    )
    vr_reference_longitude: Optional[VrReferenceLongitude] = field(
        default=None,
        metadata={
            "name": "vrReferenceLongitude",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base",
        }
    )


@dataclass
class HeadLand:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Field"

    last_modified: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    source_node: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceNode",
            "type": "Attribute",
        }
    )
    erid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    use_as_turn_predictor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "useAsTurnPredictor",
            "type": "Attribute",
        }
    )
    use_driven_exterior_headland: Optional[bool] = field(
        default=None,
        metadata={
            "name": "useDrivenExteriorHeadland",
            "type": "Attribute",
        }
    )
    vr_headland_offset: Optional[VrHeadlandOffset] = field(
        default=None,
        metadata={
            "name": "vrHeadlandOffset",
            "type": "Element",
        }
    )


@dataclass
class SpatialItems:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:Field"

    erid_field_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "eridFieldRef",
            "type": "Attribute",
        }
    )
    curved_track_line: List[CurvedTrackLine] = field(
        default_factory=list,
        metadata={
            "name": "CurvedTrackLine",
            "type": "Element",
        }
    )
    head_land: Optional[HeadLand] = field(
        default=None,
        metadata={
            "name": "HeadLand",
            "type": "Element",
        }
    )
    boundary: Optional[Boundary] = field(
        default=None,
        metadata={
            "name": "Boundary",
            "type": "Element",
        }
    )


@dataclass
class SpatialCatalog:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:FieldImportExport"

    file_schema_version: Optional[FileSchemaVersion] = field(
        default=None,
        metadata={
            "name": "FileSchemaVersion",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:Setup",
        }
    )
    source_app: Optional[SourceApp] = field(
        default=None,
        metadata={
            "name": "SourceApp",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:Setup",
        }
    )
    setup: Optional[Setup] = field(
        default=None,
        metadata={
            "name": "Setup",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:Setup",
        }
    )
    spatial_items: Optional[SpatialItems] = field(
        default=None,
        metadata={
            "name": "SpatialItems",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:SpatialCatalog:Field",
        }
    )
