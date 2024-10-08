"""Coil."""

from .baseregister import BaseRegister
from ..exceptions import PysmartyException


class Coil(BaseRegister):
    """Smart Coil Register."""

    def __init__(self, **kwargs):
        super().__init__(register_type='coil', **kwargs)

    def update_state(self):
        """Read Register."""
        res = self._connection.client.read_coils(
            self.addr, slave=self._connection.slave)
        if not res.isError():
            self.state = res.bits[0]

    def set_state(self, state):
        """Write Register."""
        res = self._connection.client.write_coil(
            self.addr, state, slave=self._connection.slave)
        if not res.isError():
            self.state = state
