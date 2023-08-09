"""GeoIP tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_geoip.city import (
    CityStream,
    LocationsStream,
    DomainStream
)

STREAM_TYPES = [
    CityStream,
    LocationsStream,
    DomainStream,
]


class TapGeoIP(Tap):
    """GeoIP tap class."""
    name = "tap-geoip"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property("license_key", th.StringType, required=True),
        th.Property("domain_edition", th.StringType, default="GeoLite2-Domain-CSV"),
        th.Property("city_edition", th.StringType, default="GeoLite2-City-CSV"),
        th.Property("languages", th.StringType, default="en"),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
