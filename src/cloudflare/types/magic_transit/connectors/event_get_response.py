# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["EventGetResponse", "E"]


class E(BaseModel):
    """Event kind plus event-specific payload fields.

    Event kinds:
    - `Init`: Initialized process
    - `Leave`: Stopped process
    - `StartAttestation`: Started attestation
    - `FinishAttestationSuccess`: Finished attestation
    - `FinishAttestationFailure`: Failed attestation
    - `StartRotateCryptKey`: Started crypt key rotation
    - `FinishRotateCryptKeySuccess`: Finished crypt key rotation
    - `FinishRotateCryptKeyFailure`: Failed crypt key rotation
    - `StartRotatePki`: Started PKI rotation
    - `FinishRotatePkiSuccess`: Finished PKI rotation
    - `FinishRotatePkiFailure`: Failed PKI rotation
    - `StartUpgrade`: Started upgrade
    - `FinishUpgradeSuccess`: Finished upgrade
    - `FinishUpgradeFailure`: Failed upgrade
    - `Reconcile`: Reconciled
    - `ConfigureCloudflaredTunnel`: Configured Cloudflared tunnel
    - `RekeyInstallBoth`: Installed initial inbound and outbound keys
    - `RekeyStart`: Installed new inbound key, kept old outbound
    - `RekeyRestart`: Restarted in-progress rekey with newer key material
    - `RekeyAdvance`: Confirmed traffic on new inbound key, swapped outbound to new
    - `RekeyComplete`: Deleted old keys
    - `RekeyReset`: Deleted all keys after receiving an unexpected key
    """

    k: Literal[
        "Init",
        "Leave",
        "StartAttestation",
        "FinishAttestationSuccess",
        "FinishAttestationFailure",
        "StartRotateCryptKey",
        "FinishRotateCryptKeySuccess",
        "FinishRotateCryptKeyFailure",
        "StartRotatePki",
        "FinishRotatePkiSuccess",
        "FinishRotatePkiFailure",
        "StartUpgrade",
        "FinishUpgradeSuccess",
        "FinishUpgradeFailure",
        "Reconcile",
        "ConfigureCloudflaredTunnel",
        "RekeyInstallBoth",
        "RekeyStart",
        "RekeyRestart",
        "RekeyAdvance",
        "RekeyComplete",
        "RekeyReset",
    ]
    """Event kind"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class EventGetResponse(BaseModel):
    """Recorded Event"""

    e: E
    """Event kind plus event-specific payload fields.

    Event kinds:

    - `Init`: Initialized process
    - `Leave`: Stopped process
    - `StartAttestation`: Started attestation
    - `FinishAttestationSuccess`: Finished attestation
    - `FinishAttestationFailure`: Failed attestation
    - `StartRotateCryptKey`: Started crypt key rotation
    - `FinishRotateCryptKeySuccess`: Finished crypt key rotation
    - `FinishRotateCryptKeyFailure`: Failed crypt key rotation
    - `StartRotatePki`: Started PKI rotation
    - `FinishRotatePkiSuccess`: Finished PKI rotation
    - `FinishRotatePkiFailure`: Failed PKI rotation
    - `StartUpgrade`: Started upgrade
    - `FinishUpgradeSuccess`: Finished upgrade
    - `FinishUpgradeFailure`: Failed upgrade
    - `Reconcile`: Reconciled
    - `ConfigureCloudflaredTunnel`: Configured Cloudflared tunnel
    - `RekeyInstallBoth`: Installed initial inbound and outbound keys
    - `RekeyStart`: Installed new inbound key, kept old outbound
    - `RekeyRestart`: Restarted in-progress rekey with newer key material
    - `RekeyAdvance`: Confirmed traffic on new inbound key, swapped outbound to new
    - `RekeyComplete`: Deleted old keys
    - `RekeyReset`: Deleted all keys after receiving an unexpected key
    """

    n: float
    """Sequence number, used to order events with the same timestamp"""

    t: float
    """Time the Event was recorded (seconds since the Unix epoch)"""

    v: Optional[str] = None
    """Version"""
