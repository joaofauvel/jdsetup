from dataclasses import InitVar, dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from jdsetup.gs3.models.basic_types import FileSchemaContentVersion, RepresentationSystemVersion, Synchronization, UnitOfMeasureVersion
from jdsetup.gs3.models.rcd.setup import (
    Farm,
    Field,
    FileSchemaVersion,
    Participant,
    Products,
)
from jdsetup.gs3.models.spatial_types import (
    Mbr,
    DtSignalType,
)
from jdsetup.gs3.common import fmt_uuid4

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
        default='None',
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
class VrHeadlandOffset:
    class Meta:
        name = "vrHeadlandOffset"
        namespace = ""

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
class HeadLand:
    class Meta:
        namespace = ""

    field_: InitVar[Field | None] = None

    last_modified: Optional[XmlDateTime] = field(
        default=XmlDateTime.now(),
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
        default_factory=fmt_uuid4,
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

    def __post_init__(self, field_) -> None:
        if field_:
            self.source_node = field_.source_node

@dataclass
class HeadlandLookup:
    class Meta:
        namespace = ""

    headland: InitVar[HeadLand | None] = None

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

    def __post_init__(self, headland):
        if headland:
            self.erid_ref = headland.erid


@dataclass
class NameIdpair:
    class Meta:
        name = "NameIDPair"
        namespace = ""

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
class Boundary:
    class Meta:
        namespace = ""

    field_: InitVar[Field | None] = None

    last_modified: Optional[XmlDateTime] = field(
        default=XmlDateTime.now(),
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
        default_factory=fmt_uuid4,
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

    def __post_init__(self, field_) -> None:
        if field_:
            self.source_node = field_.source_node


@dataclass
class CurvedTrackLine:
    class Meta:
        namespace = ""

    field_: InitVar[Field | None] = None

    last_modified: Optional[XmlDateTime] = field(
        default=XmlDateTime.now(),
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
        default_factory=fmt_uuid4,
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

    def __post_init__(self, field_) -> None:
        if field_:
            self.source_node = field_.source_node


@dataclass
class SpatialItems:
    class Meta:
        namespace = ""

    field_: InitVar[Field | None] = None

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

    def __post_init__(self, field_) -> None:
        if field_:
            self.erid_field_ref = field_.erid


@dataclass
class SCFileSchemaVersion:
    class Meta:
        namespace = ""

    non_production_code: Optional[int] = field(
        default=None,
        metadata={
            "name": "nonProductionCode",
            "type": "Attribute",
        }
    )
    file_schema_content_version: Optional[FileSchemaContentVersion] = field(
        default=None,
        metadata={
            "name": "FileSchemaContentVersion",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:BasicTypes",
        }
    )
    unit_of_measure_version: Optional[UnitOfMeasureVersion] = field(
        default=None,
        metadata={
            "name": "UnitOfMeasureVersion",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:BasicTypes",
        }
    )
    representation_system_version: Optional[RepresentationSystemVersion] = field(
        default=None,
        metadata={
            "name": "RepresentationSystemVersion",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:BasicTypes",
        }
    )


@dataclass
class SCSourceApp:
    class Meta:
        namespace = ""

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
    build: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    revision: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    name_source_app: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameSourceApp",
            "type": "Attribute",
        }
    )
    uuid_source_app: Optional[str] = field(
        default=None,
        metadata={
            "name": "uuidSourceApp",
            "type": "Attribute",
        }
    )
    uuid_source_app_node: Optional[str] = field(
        default=None,
        metadata={
            "name": "uuidSourceAppNode",
            "type": "Attribute",
        }
    )
    uuid_session: Optional[str] = field(
        default=None,
        metadata={
            "name": "uuidSession",
            "type": "Attribute",
        }
    )


@dataclass
class SCSetup:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    file_schema_version: Optional[FileSchemaVersion] = field(
        default=None,
        metadata={
            "name": "FileSchemaVersion",
            "type": "Element",
        }
    )
    synchronization: Optional[Synchronization] = field(
        default=None,
        metadata={
            "name": "Synchronization",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:BasicTypes",
        }
    )
    participant: Optional[Participant] = field(
        default=None,
        metadata={
            "name": "Participant",
            "type": "Element",
        }
    )
    farm: Optional[Farm] = field(
        default=None,
        metadata={
            "name": "Farm",
            "type": "Element",
        }
    )
    fields: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
        }
    )
    products: Optional[Products] = field(
        default=None,
        metadata={
            "name": "Products",
            "type": "Element",
        }
    )


@dataclass
class SpatialCatalog:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:FieldImportExport"

    file_schema_version: Optional[SCFileSchemaVersion] = field(
        default=None,
        metadata={
            "name": "FileSchemaVersion",
            "type": "Element",
            "namespace": "",
        }
    )
    source_app: Optional[SCSourceApp] = field(
        default=None,
        metadata={
            "name": "SourceApp",
            "type": "Element",
            "namespace": "",
        }
    )
    setup: Optional[SCSetup] = field(
        default=None,
        metadata={
            "name": "Setup",
            "type": "Element",
            "namespace": "",
        }
    )
    spatial_items: Optional[SpatialItems] = field(
        default=None,
        metadata={
            "name": "SpatialItems",
            "type": "Element",
            "namespace": "",
        }
    )
