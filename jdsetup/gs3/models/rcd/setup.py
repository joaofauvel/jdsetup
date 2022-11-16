from dataclasses import InitVar, dataclass, field
from decimal import Decimal
from typing import List, Optional, Union
from uuid import uuid4, UUID
from xsdata.models.datatype import XmlDateTime
from jdsetup.gs3.models.basic_types import (
    FileSchemaContentVersion,
    RepresentationSystemVersion,
    Synchronization,
    UnitOfMeasureVersion,
)

__NAMESPACE__ = "urn:schemas-johndeere-com:RCD:Setup"

def fmt_uuid4() -> str:
    return f'{{{str(uuid4())}}}'

@dataclass
class Area:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class Chemical:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    material_classification: Optional[str] = field(
        default=None,
        metadata={
            "name": "materialClassification",
            "type": "Attribute",
        }
    )
    restricted_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "restrictedUse",
            "type": "Attribute",
        }
    )
    chemical_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "chemicalTypeRef",
            "type": "Attribute",
        }
    )


@dataclass
class ChemicalType:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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


@dataclass
class Client:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    last_modified: XmlDateTime = field(
        default=XmlDateTime.now(),
        metadata={
            "name": "lastModified",
            "type": "Attribute",
        }
    )
    source_node: str = field(
        default=fmt_uuid4(),
        metadata={
            "name": "sourceNode",
            "type": "Attribute",
        }
    )
    erid: str = field(
        default=fmt_uuid4(),
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


@dataclass
class ConnectionType:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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


@dataclass
class CropWeight:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class Farm:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    client: InitVar[Client | None] = None

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
        default=fmt_uuid4(),
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
    client_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "clientRef",
            "type": "Attribute",
        }
    )

    def __post_init__(self, client) -> None:
        self.client_ref = client.erid if client else None
        self.source_node = client.source_node if client else None


@dataclass
class FertilizerType:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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


@dataclass
class ImplementModel:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    name: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    implement_model_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "implementModelId",
            "type": "Attribute",
        }
    )
    implement_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "implementTypeRef",
            "type": "Attribute",
        }
    )
    implement_definition: Optional[object] = field(
        default=None,
        metadata={
            "name": "ImplementDefinition",
            "type": "Element",
        }
    )


@dataclass
class ImplementType:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "refID",
            "type": "Attribute",
        }
    )


@dataclass
class ImplementTypeRef:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    erid_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "eridRef",
            "type": "Attribute",
        }
    )


@dataclass
class MachineModel:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    machine_model_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "machineModelId",
            "type": "Attribute",
        }
    )
    machine_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "machineTypeRef",
            "type": "Attribute",
        }
    )
    machine_definition: Optional[object] = field(
        default=None,
        metadata={
            "name": "MachineDefinition",
            "type": "Element",
        }
    )


@dataclass
class NamedFlagType:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class SourceApp:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
class StandardPayableMoisture:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class Task:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class UserDefinedTypeInstance:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class DtHeadlandCoverageSetting:
    class Meta:
        name = "dtHeadlandCoverageSetting"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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


@dataclass
class DtHitchType:
    class Meta:
        name = "dtHitchType"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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


@dataclass
class DtNonSteeringAxleLocation:
    class Meta:
        name = "dtNonSteeringAxleLocation"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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


@dataclass
class DtPassableCoverageSetting:
    class Meta:
        name = "dtPassableCoverageSetting"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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


@dataclass
class VrDistance:
    class Meta:
        name = "vrDistance"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrGpstoNonSteeringAxleOffset:
    class Meta:
        name = "vrGPSToNonSteeringAxleOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrImplementFrontOffset:
    class Meta:
        name = "vrImplementFrontOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrImplementLength:
    class Meta:
        name = "vrImplementLength"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrImplementVerticalCuttingEdgeToGroundOffset:
    class Meta:
        name = "vrImplementVerticalCuttingEdgeToGroundOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrImplementVerticalReceiverToCuttingEdgeOffset:
    class Meta:
        name = "vrImplementVerticalReceiverToCuttingEdgeOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrInlineOffset:
    class Meta:
        name = "vrInlineOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrLateralOffset:
    class Meta:
        name = "vrLateralOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrMachineReceiverVerticalOffset:
    class Meta:
        name = "vrMachineReceiverVerticalOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrNonSteeringAxleToConnectionOffset:
    class Meta:
        name = "vrNonSteeringAxleToConnectionOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrNumberOfRows:
    class Meta:
        name = "vrNumberOfRows"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrPhysicalImplementWidth:
    class Meta:
        name = "vrPhysicalImplementWidth"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrReceiverOffset:
    class Meta:
        name = "vrReceiverOffset"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class VrRowWidth:
    class Meta:
        name = "vrRowWidth"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Union[float, Decimal]] = field(
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
class VrTurnRadius:
    class Meta:
        name = "vrTurnRadius"
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    value: Optional[Decimal] = field(
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
class ConnectionDistance:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    vr_non_steering_axle_to_connection_offset: Optional[VrNonSteeringAxleToConnectionOffset] = field(
        default=None,
        metadata={
            "name": "vrNonSteeringAxleToConnectionOffset",
            "type": "Element",
        }
    )
    connection_type: Optional[ConnectionType] = field(
        default=None,
        metadata={
            "name": "ConnectionType",
            "type": "Element",
        }
    )


@dataclass
class ControlPoint:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    vr_lateral_offset: Optional[VrLateralOffset] = field(
        default=None,
        metadata={
            "name": "vrLateralOffset",
            "type": "Element",
        }
    )
    vr_inline_offset: Optional[VrInlineOffset] = field(
        default=None,
        metadata={
            "name": "vrInlineOffset",
            "type": "Element",
        }
    )


@dataclass
class Crop:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    id: Optional[int] = field(
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
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    legacy_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "legacyId",
            "type": "Attribute",
        }
    )
    crop_weight: Optional[CropWeight] = field(
        default=None,
        metadata={
            "name": "CropWeight",
            "type": "Element",
        }
    )
    standard_payable_moisture: Optional[StandardPayableMoisture] = field(
        default=None,
        metadata={
            "name": "StandardPayableMoisture",
            "type": "Element",
        }
    )


@dataclass
class Field:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    farm: InitVar[Farm | None] = None

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
        default=fmt_uuid4(),
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
    farm_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "farmRef",
            "type": "Attribute",
        }
    )
    area: Area = field(
        default=None,
        metadata={
            "name": "Area",
            "type": "Element",
        }
    )

    def __post_init__(self, farm) -> None:
        self.farm_ref = farm.erid if farm else None
        self.source_node = farm.source_node if farm else None


@dataclass
class FileSchemaVersion:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
class FlagTypes:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    named_flag_type: List[NamedFlagType] = field(
        default_factory=list,
        metadata={
            "name": "NamedFlagType",
            "type": "Element",
        }
    )


@dataclass
class ImplementAutomationSettings:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    number_of_skipped_tracks: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfSkippedTracks",
            "type": "Attribute",
        }
    )
    vr_turn_radius: Optional[VrTurnRadius] = field(
        default=None,
        metadata={
            "name": "vrTurnRadius",
            "type": "Element",
        }
    )
    dt_headland_coverage_setting: Optional[DtHeadlandCoverageSetting] = field(
        default=None,
        metadata={
            "name": "dtHeadlandCoverageSetting",
            "type": "Element",
        }
    )
    dt_passable_coverage_setting: Optional[DtPassableCoverageSetting] = field(
        default=None,
        metadata={
            "name": "dtPassableCoverageSetting",
            "type": "Element",
        }
    )
    boundary_sequences: Optional[object] = field(
        default=None,
        metadata={
            "name": "BoundarySequences",
            "type": "Element",
        }
    )


@dataclass
class MachineAutomationSettings:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    turn_sensitivity: Optional[int] = field(
        default=None,
        metadata={
            "name": "turnSensitivity",
            "type": "Attribute",
        }
    )
    vr_turn_radius: Optional[VrTurnRadius] = field(
        default=None,
        metadata={
            "name": "vrTurnRadius",
            "type": "Element",
        }
    )


@dataclass
class MachineType:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    ref_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "refID",
            "type": "Attribute",
        }
    )
    implement_type_ref: List[ImplementTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "ImplementTypeRef",
            "type": "Element",
        }
    )


@dataclass
class Participant:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    client: Optional[Client] = field(
        default=None,
        metadata={
            "name": "Client",
            "type": "Element",
        }
    )


@dataclass
class RearConnectionPointOffset:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    vr_lateral_offset: Optional[VrLateralOffset] = field(
        default=None,
        metadata={
            "name": "vrLateralOffset",
            "type": "Element",
        }
    )
    vr_inline_offset: Optional[VrInlineOffset] = field(
        default=None,
        metadata={
            "name": "vrInlineOffset",
            "type": "Element",
        }
    )


@dataclass
class ReceiverPoint:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    vr_lateral_offset: Optional[VrLateralOffset] = field(
        default=None,
        metadata={
            "name": "vrLateralOffset",
            "type": "Element",
        }
    )
    vr_inline_offset: Optional[VrInlineOffset] = field(
        default=None,
        metadata={
            "name": "vrInlineOffset",
            "type": "Element",
        }
    )
    vr_implement_vertical_receiver_to_cutting_edge_offset: Optional[VrImplementVerticalReceiverToCuttingEdgeOffset] = field(
        default=None,
        metadata={
            "name": "vrImplementVerticalReceiverToCuttingEdgeOffset",
            "type": "Element",
        }
    )


@dataclass
class RowDistance:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    vr_number_of_rows: Optional[VrNumberOfRows] = field(
        default=None,
        metadata={
            "name": "vrNumberOfRows",
            "type": "Element",
        }
    )
    vr_row_width: Optional[VrRowWidth] = field(
        default=None,
        metadata={
            "name": "vrRowWidth",
            "type": "Element",
        }
    )


@dataclass
class UserDefinedType:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    user_defined_type_instance: List[UserDefinedTypeInstance] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedTypeInstance",
            "type": "Element",
        }
    )
    parent: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class ImplementWidth:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    use_rows: Optional[bool] = field(
        default=None,
        metadata={
            "name": "useRows",
            "type": "Attribute",
        }
    )
    vr_distance: Optional[VrDistance] = field(
        default=None,
        metadata={
            "name": "vrDistance",
            "type": "Element",
        }
    )
    row_distance: Optional[RowDistance] = field(
        default=None,
        metadata={
            "name": "RowDistance",
            "type": "Element",
        }
    )


@dataclass
class Offsets:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    vr_implement_length: Optional[VrImplementLength] = field(
        default=None,
        metadata={
            "name": "vrImplementLength",
            "type": "Element",
        }
    )
    control_point: Optional[ControlPoint] = field(
        default=None,
        metadata={
            "name": "ControlPoint",
            "type": "Element",
        }
    )
    vr_implement_front_offset: Optional[VrImplementFrontOffset] = field(
        default=None,
        metadata={
            "name": "vrImplementFrontOffset",
            "type": "Element",
        }
    )
    receiver_point: Optional[ReceiverPoint] = field(
        default=None,
        metadata={
            "name": "ReceiverPoint",
            "type": "Element",
        }
    )
    rear_connection_point_offset: Optional[RearConnectionPointOffset] = field(
        default=None,
        metadata={
            "name": "RearConnectionPointOffset",
            "type": "Element",
        }
    )
    vr_implement_vertical_cutting_edge_to_ground_offset: Optional[VrImplementVerticalCuttingEdgeToGroundOffset] = field(
        default=None,
        metadata={
            "name": "vrImplementVerticalCuttingEdgeToGroundOffset",
            "type": "Element",
        }
    )
    vr_receiver_offset: Optional[VrReceiverOffset] = field(
        default=None,
        metadata={
            "name": "vrReceiverOffset",
            "type": "Element",
        }
    )
    vr_gpsto_non_steering_axle_offset: Optional[VrGpstoNonSteeringAxleOffset] = field(
        default=None,
        metadata={
            "name": "vrGPSToNonSteeringAxleOffset",
            "type": "Element",
        }
    )
    connection_distance: List[ConnectionDistance] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionDistance",
            "type": "Element",
        }
    )
    dt_non_steering_axle_location: Optional[DtNonSteeringAxleLocation] = field(
        default=None,
        metadata={
            "name": "dtNonSteeringAxleLocation",
            "type": "Element",
        }
    )
    vr_machine_receiver_vertical_offset: Optional[VrMachineReceiverVerticalOffset] = field(
        default=None,
        metadata={
            "name": "vrMachineReceiverVerticalOffset",
            "type": "Element",
        }
    )


@dataclass
class Products:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    chemical: List[Chemical] = field(
        default_factory=list,
        metadata={
            "name": "Chemical",
            "type": "Element",
        }
    )
    crop: List[Crop] = field(
        default_factory=list,
        metadata={
            "name": "Crop",
            "type": "Element",
        }
    )


@dataclass
class TrackSpacing:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    use_rows: Optional[bool] = field(
        default=None,
        metadata={
            "name": "useRows",
            "type": "Attribute",
        }
    )
    vr_distance: Optional[VrDistance] = field(
        default=None,
        metadata={
            "name": "vrDistance",
            "type": "Element",
        }
    )
    row_distance: Optional[RowDistance] = field(
        default=None,
        metadata={
            "name": "RowDistance",
            "type": "Element",
        }
    )


@dataclass
class ImplementSettings:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    implement_width: Optional[ImplementWidth] = field(
        default=None,
        metadata={
            "name": "ImplementWidth",
            "type": "Element",
        }
    )
    track_spacing: Optional[TrackSpacing] = field(
        default=None,
        metadata={
            "name": "TrackSpacing",
            "type": "Element",
        }
    )
    offsets: Optional[Offsets] = field(
        default=None,
        metadata={
            "name": "Offsets",
            "type": "Element",
        }
    )
    vr_physical_implement_width: Optional[VrPhysicalImplementWidth] = field(
        default=None,
        metadata={
            "name": "vrPhysicalImplementWidth",
            "type": "Element",
        }
    )


@dataclass
class MachineSettings:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    dt_hitch_type: Optional[DtHitchType] = field(
        default=None,
        metadata={
            "name": "dtHitchType",
            "type": "Element",
        }
    )
    offsets: Optional[Offsets] = field(
        default=None,
        metadata={
            "name": "Offsets",
            "type": "Element",
        }
    )


@dataclass
class ImplementDefinition:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    implement_settings: Optional[ImplementSettings] = field(
        default=None,
        metadata={
            "name": "ImplementSettings",
            "type": "Element",
        }
    )
    implement_automation_settings: Optional[ImplementAutomationSettings] = field(
        default=None,
        metadata={
            "name": "ImplementAutomationSettings",
            "type": "Element",
        }
    )


@dataclass
class MachineDefinition:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    machine_settings: Optional[MachineSettings] = field(
        default=None,
        metadata={
            "name": "MachineSettings",
            "type": "Element",
        }
    )
    machine_automation_settings: Optional[MachineAutomationSettings] = field(
        default=None,
        metadata={
            "name": "MachineAutomationSettings",
            "type": "Element",
        }
    )


@dataclass
class Implement:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    name: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "serialNumber",
            "type": "Attribute",
        }
    )
    isoname: Optional[object] = field(
        default=None,
        metadata={
            "name": "ISONAME",
            "type": "Attribute",
        }
    )
    implement_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "implementTypeRef",
            "type": "Attribute",
        }
    )
    structure_label: Optional[object] = field(
        default=None,
        metadata={
            "name": "structureLabel",
            "type": "Attribute",
        }
    )
    implement_model_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "implementModelRef",
            "type": "Attribute",
        }
    )
    implement_definition: Optional[ImplementDefinition] = field(
        default=None,
        metadata={
            "name": "ImplementDefinition",
            "type": "Element",
        }
    )


@dataclass
class Machine:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

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
    name: Optional[Union[str, int]] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    active: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "serialNumber",
            "type": "Attribute",
        }
    )
    isoname: Optional[object] = field(
        default=None,
        metadata={
            "name": "ISONAME",
            "type": "Attribute",
        }
    )
    machine_type_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "machineTypeRef",
            "type": "Attribute",
        }
    )
    machine_model_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "machineModelRef",
            "type": "Attribute",
        }
    )
    machine_definition: Optional[MachineDefinition] = field(
        default=None,
        metadata={
            "name": "MachineDefinition",
            "type": "Element",
        }
    )


@dataclass
class Equipment:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    machine: List[Machine] = field(
        default_factory=list,
        metadata={
            "name": "Machine",
            "type": "Element",
        }
    )
    implement: List[Implement] = field(
        default_factory=list,
        metadata={
            "name": "Implement",
            "type": "Element",
        }
    )


@dataclass
class Setup:
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
    field_value: List[Field] = field(
        default_factory=list,
        metadata={
            "name": "Field",
            "type": "Element",
        }
    )
    fertilizer_type: List[FertilizerType] = field(
        default_factory=list,
        metadata={
            "name": "FertilizerType",
            "type": "Element",
        }
    )
    chemical_type: List[ChemicalType] = field(
        default_factory=list,
        metadata={
            "name": "ChemicalType",
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
    machine_type: List[MachineType] = field(
        default_factory=list,
        metadata={
            "name": "MachineType",
            "type": "Element",
        }
    )
    implement_type: List[ImplementType] = field(
        default_factory=list,
        metadata={
            "name": "ImplementType",
            "type": "Element",
        }
    )
    equipment: Optional[Equipment] = field(
        default=None,
        metadata={
            "name": "Equipment",
            "type": "Element",
        }
    )
    task: List[Task] = field(
        default_factory=list,
        metadata={
            "name": "Task",
            "type": "Element",
        }
    )
    flag_types: Optional[FlagTypes] = field(
        default=None,
        metadata={
            "name": "FlagTypes",
            "type": "Element",
        }
    )
    user_defined_type: List[UserDefinedType] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedType",
            "type": "Element",
        }
    )
    machine_model: List[MachineModel] = field(
        default_factory=list,
        metadata={
            "name": "MachineModel",
            "type": "Element",
        }
    )
    implement_model: List[ImplementModel] = field(
        default_factory=list,
        metadata={
            "name": "ImplementModel",
            "type": "Element",
        }
    )


@dataclass
class SetupFile:
    class Meta:
        namespace = "urn:schemas-johndeere-com:RCD:Setup"

    language: str = field(
        default='en-US',
        metadata={
            "type": "Attribute",
        }
    )
    source_app: Optional[SourceApp] = field(
        default=None,
        metadata={
            "name": "SourceApp",
            "type": "Element",
        }
    )
    setup: Optional[Setup] = field(
        default=None,
        metadata={
            "name": "Setup",
            "type": "Element",
        }
    )
