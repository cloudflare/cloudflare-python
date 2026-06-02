# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "EventGetResponse",
    "E",
    "EInit",
    "ELeave",
    "EStartAttestation",
    "EFinishAttestationSuccess",
    "EFinishAttestationFailure",
    "EStartRotateCryptKey",
    "EFinishRotateCryptKeySuccess",
    "EFinishRotateCryptKeyFailure",
    "EStartRotatePki",
    "EFinishRotatePkiSuccess",
    "EFinishRotatePkiFailure",
    "EStartUpgrade",
    "EFinishUpgradeSuccess",
    "EFinishUpgradeFailure",
    "EReconcile",
    "EConfigureCloudflaredTunnel",
    "ERekeyInstallBoth",
    "ERekeyStart",
    "ERekeyAdvance",
    "ERekeyComplete",
    "ERekeyReset",
]


class EInit(BaseModel):
    k: Literal["Init"]
    """Initialized process"""


class ELeave(BaseModel):
    k: Literal["Leave"]
    """Stopped process"""


class EStartAttestation(BaseModel):
    k: Literal["StartAttestation"]
    """Started attestation"""


class EFinishAttestationSuccess(BaseModel):
    k: Literal["FinishAttestationSuccess"]
    """Finished attestation"""


class EFinishAttestationFailure(BaseModel):
    k: Literal["FinishAttestationFailure"]
    """Failed attestation"""


class EStartRotateCryptKey(BaseModel):
    k: Literal["StartRotateCryptKey"]
    """Started crypt key rotation"""


class EFinishRotateCryptKeySuccess(BaseModel):
    k: Literal["FinishRotateCryptKeySuccess"]
    """Finished crypt key rotation"""


class EFinishRotateCryptKeyFailure(BaseModel):
    k: Literal["FinishRotateCryptKeyFailure"]
    """Failed crypt key rotation"""


class EStartRotatePki(BaseModel):
    k: Literal["StartRotatePki"]
    """Started PKI rotation"""


class EFinishRotatePkiSuccess(BaseModel):
    k: Literal["FinishRotatePkiSuccess"]
    """Finished PKI rotation"""


class EFinishRotatePkiFailure(BaseModel):
    k: Literal["FinishRotatePkiFailure"]
    """Failed PKI rotation"""


class EStartUpgrade(BaseModel):
    k: Literal["StartUpgrade"]
    """Started upgrade"""

    url: str
    """Location of upgrade bundle"""


class EFinishUpgradeSuccess(BaseModel):
    k: Literal["FinishUpgradeSuccess"]
    """Finished upgrade"""


class EFinishUpgradeFailure(BaseModel):
    k: Literal["FinishUpgradeFailure"]
    """Failed upgrade"""


class EReconcile(BaseModel):
    k: Literal["Reconcile"]
    """Reconciled"""


class EConfigureCloudflaredTunnel(BaseModel):
    k: Literal["ConfigureCloudflaredTunnel"]
    """Configured Cloudflared tunnel"""


class ERekeyInstallBoth(BaseModel):
    k: Literal["RekeyInstallBoth"]
    """Installed initial inbound and outbound keys"""

    tunnel_id: str
    """Tunnel identifier"""


class ERekeyStart(BaseModel):
    k: Literal["RekeyStart"]
    """Installed new inbound key, kept old outbound"""

    tunnel_id: str
    """Tunnel identifier"""


class ERekeyAdvance(BaseModel):
    k: Literal["RekeyAdvance"]
    """Confirmed traffic on new inbound key, swapped outbound to new"""

    tunnel_id: str
    """Tunnel identifier"""


class ERekeyComplete(BaseModel):
    k: Literal["RekeyComplete"]
    """Deleted old keys"""

    tunnel_id: str
    """Tunnel identifier"""


class ERekeyReset(BaseModel):
    k: Literal["RekeyReset"]
    """Deleted all keys after receiving an unexpected key"""

    tunnel_id: str
    """Tunnel identifier"""


E: TypeAlias = Annotated[
    Union[
        EInit,
        ELeave,
        EStartAttestation,
        EFinishAttestationSuccess,
        EFinishAttestationFailure,
        EStartRotateCryptKey,
        EFinishRotateCryptKeySuccess,
        EFinishRotateCryptKeyFailure,
        EStartRotatePki,
        EFinishRotatePkiSuccess,
        EFinishRotatePkiFailure,
        EStartUpgrade,
        EFinishUpgradeSuccess,
        EFinishUpgradeFailure,
        EReconcile,
        EConfigureCloudflaredTunnel,
        ERekeyInstallBoth,
        ERekeyStart,
        ERekeyAdvance,
        ERekeyComplete,
        ERekeyReset,
    ],
    PropertyInfo(discriminator="k"),
]


class EventGetResponse(BaseModel):
    """Recorded Event"""

    e: E

    n: float
    """Sequence number, used to order events with the same timestamp"""

    t: float
    """Time the Event was recorded (seconds since the Unix epoch)"""

    v: Optional[str] = None
    """Version"""
