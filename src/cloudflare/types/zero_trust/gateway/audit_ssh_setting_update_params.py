# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuditSSHSettingUpdateParams"]


class AuditSSHSettingUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    public_key: Required[str]
    """Base64 encoded HPKE public key used to encrypt all your ssh session logs.

    https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/use-cases/ssh/ssh-infrastructure-access/#enable-ssh-command-logging
    """
