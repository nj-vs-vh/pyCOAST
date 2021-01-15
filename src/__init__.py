"""
Python-style classes wrapping C++ classes interfaced with SWIG.

They only incapsulate the most basic properties for now, but are easily extendable.
"""

from __future__ import annotations

from typing import Generator, List

from . import coast_wrapper


class CorsikaReader:
    def __init__(self, filename: str, verbosity: int = 0):
        self.filename = filename
        self._reader = coast_wrapper.MCorsikaReader(filename, verbosity)

    def __str__(self) -> str:
        return f"Corsika Reader for {self.filename}"

    def runs(self) -> Generator[_CorsikaRun, None, None]:
        self._current_run = coast_wrapper.MRunHeader()
        while self._reader.GetRun(self._current_run):
            # in C++ code it's OK to place new value in the same MRunHeader variable each time,
            # but in Python it seems logical to return new _CorsikaRun wrapping actual run header
            # every time
            yield _CorsikaRun(self._current_run, self)


class _CorsikaRun:
    def __init__(self, run: coast_wrapper.MRunHeader, parent_reader: CorsikaReader):
        self._parent_reader = parent_reader
        self._run = run
        self.id = self._run.GetRunID()

    def __str__(self) -> str:
        # for some reason GetRunID returns float, turn it to int for prettiness
        return f'Run {int(self.id)}'

    def showers(self) -> Generator[_CorsikaShower, None, None]:
        self._current_shower = coast_wrapper.MEventHeader()
        while self._parent_reader._reader.GetShower(self._current_shower):
            yield _CorsikaShower(self._current_shower, self._parent_reader)


class _CorsikaShower:
    def __init__(self, shower: coast_wrapper.MEventHeader, parent_reader: CorsikaReader):
        self._parent_reader = parent_reader
        self._shower = shower
        self.number = self._shower.GetEventNumber()
        n_obs_levels = self._shower.GetNObservationLevels()
        self.observation_levels = []
        for i in range(n_obs_levels):
            self.observation_levels.append(self._shower.GetObservationHeight(i))

        self.theta = self._shower.GetTheta()
        self.phi = self._shower.GetPhi()
        self.z_first = self._shower.GetZFirst()

    def __str__(self) -> str:
        return (
            f"Shower {self.number}, "
            + f"theta={self.theta}, phi={self.phi}, z first={self.z_first}, "
            + f"observed at {', '.join(str(l) for l in self.observation_levels)}"
        )

    def subblocks(self) -> Generator[_CorsikaSubBlock, None, None]:
        self._current_block = coast_wrapper.TSubBlock()
        while self._parent_reader._reader.GetData(self._current_block):
            yield _CorsikaSubBlock(self._current_block)

    def particle_coords(self) -> Generator[_CorsikaParticleCoords, None, None]:
        for block in self.subblocks():
            for particle_coords in block.particle_coords():
                yield particle_coords


class _CorsikaSubBlock:
    def __init__(self, block: coast_wrapper.TSubBlock):
        self._block = block
        self.type = block.GetBlockType()

    @property
    def is_particle_data(self):
        return self.type == coast_wrapper.TSubBlock.ePARTDATA

    def particle_coords(self) -> List[_CorsikaParticleCoords]:
        if not self.is_particle_data:
            return None
        return [_CorsikaParticleCoords(pc) for pc in coast_wrapper.getParticleCoordsList(self._block)]


class _CorsikaParticleCoords:
    def __init__(self, particle_coords: coast_wrapper.ParticleCoords):
        self.id = particle_coords.id
        self.x = particle_coords.x
        self.y = particle_coords.y

    def __str__(self) -> str:
        return f"type={self.id}, x={self.x}, y={self.y}"
