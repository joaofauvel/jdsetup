from dataclasses import InitVar, dataclass, field
from functools import partial
from typing import Callable, List, Optional
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

    value: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    source_uom: str = field(
        default='m',
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: str = field(
        default='vrEastShiftComponent',
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

    value: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    source_uom: str = field(
        default='m',
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: str = field(
        default='vrNorthShiftComponent',
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
    source_uom: str = field(
        default='arcdeg',
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: str = field(
        default='vrLatitude',
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
    source_uom: str = field(
        default='arcdeg',
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: str = field(
        default='vrLongitude',
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

    value: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        }
    )
    source_uom: str = field(
        default='ft',
        metadata={
            "name": "sourceUOM",
            "type": "Attribute",
        }
    )
    variable_representation: str = field(
        default='vrHeadlandOffset',
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

    last_modified: XmlDateTime = field(
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
    erid: str = field(
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
    use_as_turn_predictor: bool = field(
        default=False,
        metadata={
            "name": "useAsTurnPredictor",
            "type": "Attribute",
        }
    )
    use_driven_exterior_headland: bool = field(
        default=True,
        metadata={
            "name": "useDrivenExteriorHeadland",
            "type": "Attribute",
        }
    )
    vr_headland_offset: VrHeadlandOffset = field(
        default_factory=VrHeadlandOffset,
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
    dt_signal_type_factory: InitVar[Callable[[], DtSignalType]] = partial(DtSignalType, value='dtiSignalTypeRTK')

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
    erid: str = field(
        default_factory=fmt_uuid4,
        metadata={
            "type": "Attribute",
        }
    )
    spatial_geometry_type: str = field(
        default='polygon',
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
    mbr: Mbr = field(
        default_factory=Mbr,
        metadata={
            "name": "MBR",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:SpatialTypes",
        }
    )
    dt_signal_type: DtSignalType = field(
        default_factory=dt_signal_type_factory,
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
        if not self.file_name and self.erid:
            self.file_name = f'Boundary{self.erid.strip("}{")}'


@dataclass
class CurvedTrackLine:
    class Meta:
        namespace = ""

    field_: InitVar[Field | None] = None
    reference_longitude: InitVar[float | None] = None
    reference_latitude: InitVar[float | None] = None

    last_modified: XmlDateTime = field(
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
    erid: str = field(
        default_factory=fmt_uuid4,
        metadata={
            "type": "Attribute",
        }
    )
    spatial_geometry_type: str = field(
        default='line',
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
    mbr: Mbr = field(
        default_factory=Mbr,
        metadata={
            "name": "MBR",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:SpatialTypes",
        }
    )
    dt_signal_type: DtSignalType = field(
        default_factory=DtSignalType,
        metadata={
            "name": "dtSignalType",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:SpatialTypes",
        }
    )
    vr_east_shift_component: VrEastShiftComponent = field(
        default_factory=VrEastShiftComponent,
        metadata={
            "name": "vrEastShiftComponent",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:RCD:SpatialCatalog:Base",
        }
    )
    vr_north_shift_component: VrNorthShiftComponent = field(
        default_factory=VrNorthShiftComponent,
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

    def __post_init__(self, field_, reference_longitude, reference_latitude) -> None:
        if field_:
            self.source_node = field_.source_node
        if reference_longitude:
            self.vr_reference_longitude = VrReferenceLongitude(value=reference_longitude) 
        if reference_latitude:
            self.vr_reference_latitude = VrReferenceLatitude(value=reference_latitude)
        if not self.file_name and self.erid:
            self.file_name = f'CurveTrack{self.erid.strip("}{")}'


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

    non_production_code: int = field(
        metadata={
            "name": "nonProductionCode",
            "type": "Attribute",
        }
    )
    file_schema_content_version: FileSchemaContentVersion = field(
        metadata={
            "name": "FileSchemaContentVersion",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:BasicTypes",
        }
    )
    unit_of_measure_version: UnitOfMeasureVersion = field(
        metadata={
            "name": "UnitOfMeasureVersion",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:BasicTypes",
        }
    )
    representation_system_version: RepresentationSystemVersion = field(
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
    build: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    revision: int = field(
        metadata={
            "type": "Attribute",
        }
    )
    name_source_app: str = field(
        metadata={
            "name": "nameSourceApp",
            "type": "Attribute",
        }
    )
    uuid_source_app: str = field(
        metadata={
            "name": "uuidSourceApp",
            "type": "Attribute",
        }
    )
    uuid_source_app_node: str = field(
        metadata={
            "name": "uuidSourceAppNode",
            "type": "Attribute",
        }
    )
    uuid_session: str = field(
        metadata={
            "name": "uuidSession",
            "type": "Attribute",
        }
    )


@dataclass
class SCSetup:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    file_schema_version: FileSchemaVersion = field(
        metadata={
            "name": "FileSchemaVersion",
            "type": "Element",
        }
    )
    synchronization: Synchronization = field(
        metadata={
            "name": "Synchronization",
            "type": "Element",
            "namespace": "urn:schemas-johndeere-com:BasicTypes",
        }
    )
    participant: Participant = field(
        metadata={
            "name": "Participant",
            "type": "Element",
        }
    )
    farm: Farm = field(
        metadata={
            "name": "Farm",
            "type": "Element",
        }
    )
    field_: Field = field(
        metadata={
            "name": "Field",
            "type": "Element",
        }
    )
    products: Products = field(
        default_factory=Products,
        metadata={
            "name": "Products",
            "type": "Element",
        }
    )


@dataclass
class SpatialCatalog:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:SpatialCatalog:FieldImportExport"

    file_schema_version: SCFileSchemaVersion = field(
        metadata={
            "name": "FileSchemaVersion",
            "type": "Element",
            "namespace": "",
        }
    )
    source_app: SCSourceApp = field(
        metadata={
            "name": "SourceApp",
            "type": "Element",
            "namespace": "",
        }
    )
    setup: SCSetup = field(
        metadata={
            "name": "Setup",
            "type": "Element",
            "namespace": "",
        }
    )
    spatial_items: SpatialItems = field(
        metadata={
            "name": "SpatialItems",
            "type": "Element",
            "namespace": "",
        }
    )
