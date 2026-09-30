# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "VersionListResponse",
    "Configuration",
    "ConfigurationAuthorizedKey",
    "ConfigurationEnvironmentVariable",
    "ConfigurationObservability",
    "ConfigurationObservabilityLogs",
]


class ConfigurationAuthorizedKey(BaseModel):
    """User-provided SSH public key."""

    public_key: str
    """An SSH public key."""

    name: Optional[str] = None
    """Optional human readable name for this key."""


class ConfigurationEnvironmentVariable(BaseModel):
    """An environment variable with a value set."""

    name: str
    """An environment variable name."""

    value: str
    """An environment variable value."""


class ConfigurationObservabilityLogs(BaseModel):
    """Observability logging settings."""

    enabled: Optional[bool] = None


class ConfigurationObservability(BaseModel):
    """Settings for deployment observability such as logging."""

    logs: Optional[ConfigurationObservabilityLogs] = None
    """Observability logging settings."""


class Configuration(BaseModel):
    """User-specified container configuration changes."""

    authorized_keys: Optional[List[ConfigurationAuthorizedKey]] = None

    command: Optional[List[str]] = None
    """
    The command that runs when the container starts, passed to the entrypoint. You
    can override this at run-time. If you override only the command, it gets passed
    to the default entrypoint specified in the image.
    """

    entrypoint: Optional[List[str]] = None
    """
    The entry point for the container, specifying the executable to run when the
    container starts. You can override this at run-time. If you do, the default
    command from the image is ignored. Specify both entrypoint and command at
    run-time to completely replace the image defaults.
    """

    environment_variables: Optional[List[ConfigurationEnvironmentVariable]] = None
    """Container environment variables."""

    image: Optional[str] = None
    """Image url."""

    instance_type: Optional[Literal["lite", "basic", "standard-1", "standard-2", "standard-3", "standard-4"]] = None
    """The instance type configures vCPU, memory, and disk.

    - "lite": 1/16 vCPU, 256 MiB memory, 2 GB disk
    - "basic": 1/4 vCPU, 1 GiB memory, 4 GB disk
    - "standard-1": 1/2 vCPU, 4 GiB memory, 8 GB disk
    - "standard-2": 1 vCPU, 6 GiB memory, 12 GB disk
    - "standard-3": 2 vCPU, 8 GiB memory, 16 GB disk
    - "standard-4": 4 vCPU, 12 GiB memory, 20 GB disk
    """

    observability: Optional[ConfigurationObservability] = None
    """Settings for deployment observability such as logging."""


class VersionListResponse(BaseModel):
    """An application with the configuration of its version."""

    configuration: Configuration
    """User-specified container configuration changes."""

    percentage: int

    version: int
