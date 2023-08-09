"""Custom client handling, including GeoIPStream base class."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk.streams import Stream


class GeoIPStream(Stream):
    """Stream class for GeoIP streams."""

    @property
    def file_url(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        license_key = self.config["license_key"]
        if license_key == 'none':
            license_key = ''

        return f"https://download.maxmind.com/app/geoip_download?edition_id={self.edition}&suffix=zip&license_key={license_key}"
