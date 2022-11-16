import dataclasses
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, TypeVar

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import JsonParser

from jdsetup.gs3.models.rcd.setup import (Client, Farm, Field,
                                          FileSchemaVersion, Participant,
                                          Setup, SetupFile, SourceApp,
                                          Synchronization)
from jdsetup.gs3.models.rcd.spatial_catalog import (Boundary, CurvedTrackLine,
                                                    SpatialCatalog)

config_default_paths = {
    'source_app': './jdsetup/gs3/config/source_app.json',
    'setup': './jdsetup/gs3/config/setup.json',
    'file_schema_version': './jdsetup/gs3/config/file_schema_version.json',
    'synchronization': './jdsetup/gs3/config/synchronization.json',
}

@dataclasses.dataclass
class GS3Paths:
    setup: Path
    fields: list[Path] = dataclasses.field(default_factory=list)

    def create_structure(self) -> None:
        for f in self.fields:
            f.mkdir(parents=True)

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
    
T = TypeVar('T')
class Parser(ABC):
    @abstractmethod
    def parse(path: str, target_obj: T) -> T:
        pass

class GS3:
    def __init__(self, 
            parser: Parser, 
            participant: ParticipantDefinition, 
            profile: str = 'JDSETUP', 
            root: str = '.') -> None:
        self.profile = profile
        self.participant = participant
        self.parser = parser
        self.gs3paths = self._resolve_gs3paths(root)

    def _resolve_gs3paths(self, root: str = '.') -> GS3Paths:
        p = Path(f'{root}/GS3_2630/{self.profile}/RCD/EIC/')
        paths = GS3Paths(setup=p)
        for field in self.participant.fields:
            f = (p / 'Fields' / field.erid[7:9].upper() / field.erid.strip('}{'))
            paths.fields.append(f)
        return paths

    def _create_folder_scaffold(self, root: str = '.') -> None:
        self.gs3paths.create_structure()

    def _scaffold_setup(self, 
                    setup: str, 
                    file_schema_version: str, 
                    synchronization: str) -> Setup:
        setup_: Setup = self.parser.parse(setup, Setup)
        setup_.file_schema_version = self.parser.parse(file_schema_version, FileSchemaVersion)
        setup_.synchronization = self.parser.parse(synchronization, Synchronization)
        return setup_

    def _scaffold_setupfile(self, 
                        source_app: str, 
                        setup: str, 
                        file_schema_version: str, 
                        synchronization: str) -> SetupFile:
        setup_ = self._scaffold_setup(setup, file_schema_version, synchronization)
        source_app_ = self.parser.parse(source_app, SourceApp)
        return SetupFile(source_app=source_app_, setup=setup_)

    def setupfile(self, config_paths: dict[str, str] = config_default_paths) -> SetupFile:
        sf = self._scaffold_setupfile(**config_paths)
        sf.setup.participant = Participant(client=self.participant.client)
        sf.setup.farm = self.participant.farm
        sf.setup.fields = self.participant.fields
        return sf

    def spatialcatalog(self, config_paths: dict[str, str] = config_default_paths) -> SpatialCatalog:
        pass



