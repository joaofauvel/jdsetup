import dataclasses
from pathlib import Path
from jdsetup.gs3.models.rcd.setup import (
    Participant,
    Client,
    Farm,
    Field,
    SetupFile,
    SourceApp,
    Setup,
    FileSchemaVersion,
    Synchronization,
)

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser

@dataclasses.dataclass
class ParticipantDefinition:
    client: Client
    farm: Farm
    fields: list[Field] = dataclasses.field(default_factory=list)

    @classmethod
    def from_string(cls, client: str, farm: str, fields: list[str]) -> 'ParticipantDefinition':
        cl = Client(name=client)
        fm = Farm(cl, name=farm)
        fds = [Field(fm, name=f) for f in fields]
        return cls(cl, fm, fds)

    @classmethod
    def from_config(cls) -> 'ParticipantDefinition':
        pass

class GS3:
    def __init__(self, participant: ParticipantDefinition, profile: str = 'JDSETUP') -> None:
        self.profile = profile
        self.participant = participant

    def _create_card_scaffold_structure(self, root: str = '.') -> None:
        p = Path(f'{root}/GS3_2630/{self.profile}/RCD/EIC/Fields/')
        for field in self.participant.fields:
            (p / field.erid[6:8].upper() / field.erid.strip('}{')).mkdir(parents=True)




config_default_paths = {
    'source_app': './jdsetup/gs3/config/source_app.json',
    'setup': './jdsetup/gs3/config/setup.json',
    'file_schema_version': './jdsetup/gs3/config/file_schema_version.json',
    'synchronization': './jdsetup/gs3/config/synchronization.json',
}


def scaffold_setup(parser: JsonParser, 
                setup: str, 
                file_schema_version: str, 
                synchronization: str) -> Setup:
    setup_ = parser.parse(setup, Setup)
    setup_.file_schema_version = parser.parse(file_schema_version, FileSchemaVersion)
    setup_.synchronization = parser.parse(synchronization, Synchronization)
    return setup_


def scaffold_setupfile(parser: JsonParser, 
                    source_app: str, 
                    setup: str, 
                    file_schema_version: str, 
                    synchronization: str) -> SetupFile:
    setup_ = scaffold_setup(parser, setup, file_schema_version, synchronization)
    source_app_ = parser.parse(source_app, SourceApp)
    return SetupFile(source_app=source_app_, setup=setup_)
