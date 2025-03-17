# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
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
    "EStartUpgrade",
    "EFinishUpgradeSuccess",
    "EFinishUpgradeFailure",
    "EReconcile",
    "EConfigureCloudflaredTunnel",
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
        EStartUpgrade,
        EFinishUpgradeSuccess,
        EFinishUpgradeFailure,
        EReconcile,
        EConfigureCloudflaredTunnel,
    ],
    PropertyInfo(discriminator="k"),
]


class EventGetResponse(BaseModel):
    e: E

    n: float
    """Sequence number, used to order events with the same timestamp"""

    t: float
    """Time the Event was recorded (seconds since the Unix epoch)"""
