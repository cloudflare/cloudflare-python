# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["InstanceListV1Response", "Status", "Configuration", "Location"]


class Status(BaseModel):
    """The latest known status of a container instance."""

    state: Literal["provisioning", "running", "failed", "stopping", "stopped", "unhealthy", "inactive", "unknown"]
    """The current lifecycle state of a container instance."""

    updated_at: str
    """UTC timestamp string in ISO 8601 format."""

    exit_code: Optional[int] = None
    """The process exit code, when the runtime reports one."""


class Configuration(BaseModel):
    """The resources allocated to the container instance."""

    disk: int
    """Disk allocated to the container instance, in decimal MB."""

    memory: int
    """Memory allocated to the container instance, in MiB."""

    vcpu: float
    """Number of virtual CPUs allocated to the container instance."""


class Location(BaseModel):
    """The location of the instance's current container placement."""

    name: str
    """Unique location code used to identify locations on a logical level."""

    region: str
    """Represents a group of datacenters.

    Choose one of "AFR", "APAC", "EEUR", "ENAM", "WNAM", "ME", "OC", "SAM", or
    "WEUR".
    """


class InstanceListV1Response(BaseModel):
    """The last-reported state of a logical container instance."""

    id: str
    """A container instance ID (64-character hex Durable Object actor ID)."""

    application_id: str
    """An Application ID represents an identifier of an application."""

    image: str
    """The image for the current container placement, when one is available."""

    status: Status
    """The latest known status of a container instance."""

    configuration: Optional[Configuration] = None
    """The resources allocated to the container instance."""

    location: Optional[Location] = None
    """The location of the instance's current container placement."""

    name: Optional[str] = None
    """The customer-provided instance name, when available.

    Its UTF-8 encoding uses at most 1,024 bytes.
    """

    started_at: Optional[str] = None
    """The time at which the current container placement started, when one exists."""
