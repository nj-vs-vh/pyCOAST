"""
Python-style classes wrapping C++ classes interfaced with SWIG.

They only incapsulate the most basic properties for now, but are easily extendable.
"""

from __future__ import annotations

from typing import Generator

from . import coast_wrapper


class CorsikaReader:
    """Wrapper around MCorsikaReader (C++ class) interfaced by SWIG"""

    def __init__(self, filename: str, verbosity: int=0):
        self._reader = coast_wrapper.MCorsikaReader(filename, verbosity)
        self._current_run = coast_wrapper.MRunHeader()

    def runs(self) -> Generator[_CorsikaRun, None, None]:
        while self._reader.GetRun(self._current_run):
            yield _CorsikaRun(self._current_run)


class _CorsikaRun:
    def __init__(self, run: coast_wrapper.MRunHeader):
        self._run = run
        self.id = self._run.GetRunID()

    def __str__(self) -> str:
        # for some reason GetRunID returns float, turn it to int for prettiness
        return f'Run {int(self.id)}'
