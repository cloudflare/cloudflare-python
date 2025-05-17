# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ....._utils import PropertyInfo
from ....._models import BaseModel

__all__ = [
    "LatestListResponse",
    "Item",
    "ItemE",
    "ItemEInit",
    "ItemELeave",
    "ItemEStartAttestation",
    "ItemEFinishAttestationSuccess",
    "ItemEFinishAttestationFailure",
    "ItemEStartRotateCryptKey",
    "ItemEFinishRotateCryptKeySuccess",
    "ItemEFinishRotateCryptKeyFailure",
    "ItemEStartRotatePki",
    "ItemEFinishRotatePkiSuccess",
    "ItemEFinishRotatePkiFailure",
    "ItemEStartUpgrade",
    "ItemEFinishUpgradeSuccess",
    "ItemEFinishUpgradeFailure",
    "ItemEReconcile",
    "ItemEConfigureCloudflaredTunnel",
]


class ItemEInit(BaseModel):
    k: Literal["Init"]
    """Initialized process"""


class ItemELeave(BaseModel):
    k: Literal["Leave"]
    """Stopped process"""


class ItemEStartAttestation(BaseModel):
    k: Literal["StartAttestation"]
    """Started attestation"""


class ItemEFinishAttestationSuccess(BaseModel):
    k: Literal["FinishAttestationSuccess"]
    """Finished attestation"""


class ItemEFinishAttestationFailure(BaseModel):
    k: Literal["FinishAttestationFailure"]
    """Failed attestation"""


class ItemEStartRotateCryptKey(BaseModel):
    k: Literal["StartRotateCryptKey"]
    """Started crypt key rotation"""


class ItemEFinishRotateCryptKeySuccess(BaseModel):
    k: Literal["FinishRotateCryptKeySuccess"]
    """Finished crypt key rotation"""


class ItemEFinishRotateCryptKeyFailure(BaseModel):
    k: Literal["FinishRotateCryptKeyFailure"]
    """Failed crypt key rotation"""


class ItemEStartRotatePki(BaseModel):
    k: Literal["StartRotatePki"]
    """Started PKI rotation"""


class ItemEFinishRotatePkiSuccess(BaseModel):
    k: Literal["FinishRotatePkiSuccess"]
    """Finished PKI rotation"""


class ItemEFinishRotatePkiFailure(BaseModel):
    k: Literal["FinishRotatePkiFailure"]
    """Failed PKI rotation"""


class ItemEStartUpgrade(BaseModel):
    k: Literal["StartUpgrade"]
    """Started upgrade"""

    url: str
    """Location of upgrade bundle"""


class ItemEFinishUpgradeSuccess(BaseModel):
    k: Literal["FinishUpgradeSuccess"]
    """Finished upgrade"""


class ItemEFinishUpgradeFailure(BaseModel):
    k: Literal["FinishUpgradeFailure"]
    """Failed upgrade"""


class ItemEReconcile(BaseModel):
    k: Literal["Reconcile"]
    """Reconciled"""


class ItemEConfigureCloudflaredTunnel(BaseModel):
    k: Literal["ConfigureCloudflaredTunnel"]
    """Configured Cloudflared tunnel"""


ItemE: TypeAlias = Annotated[
    Union[
        ItemEInit,
        ItemELeave,
        ItemEStartAttestation,
        ItemEFinishAttestationSuccess,
        ItemEFinishAttestationFailure,
        ItemEStartRotateCryptKey,
        ItemEFinishRotateCryptKeySuccess,
        ItemEFinishRotateCryptKeyFailure,
        ItemEStartRotatePki,
        ItemEFinishRotatePkiSuccess,
        ItemEFinishRotatePkiFailure,
        ItemEStartUpgrade,
        ItemEFinishUpgradeSuccess,
        ItemEFinishUpgradeFailure,
        ItemEReconcile,
        ItemEConfigureCloudflaredTunnel,
    ],
    PropertyInfo(discriminator="k"),
]


class Item(BaseModel):
    e: ItemE

    n: float
    """Sequence number, used to order events with the same timestamp"""

    t: float
    """Time the Event was recorded (seconds since the Unix epoch)"""


class LatestListResponse(BaseModel):
    count: float

    items: List[Item]
