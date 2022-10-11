import logging

from .const import LOCATION_CONNECTION, APP_URI
from .generic import RingGeneric

_LOGGER = logging.getLogger(__name__)


class OtherDevice(RingGeneric):
    """Implementation for Basic other devices"""

    @property
    def family(self):
        """Return Ring device family type."""
        return "other"

    def update_health_data(self):
        """Update health attrs."""
        ret = self._ring.query(LOCATION_CONNECTION.format(self._attrs.get("location_id")), api=APP_URI).json()
        for asset in ret["assets"]:
            if asset["doorbotId"] == self.id:
                self._health_attrs = dict(status=asset["status"])

    def status(self):
        """Return status of the asset - online or offline."""
        return self._health_attrs["status"]

    def __repr__(self):
        """Return __repr__."""
        return "<{0}: {1} {2}>".format(self.__class__.__name__, self.name, self._attrs.get("third_party_dsn"))
