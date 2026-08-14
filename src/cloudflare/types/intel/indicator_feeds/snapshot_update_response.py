# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["SnapshotUpdateResponse"]


class SnapshotUpdateResponse(BaseModel):
    file_id: Optional[int] = None
    """Feed id"""

    filename: Optional[str] = None
    """Name of the file unified in our system"""

    poll_url: Optional[str] = None
    """Account-relative polling path.

    Prepend `/accounts/{account_id}` using the same account identifier and API host
    as the upload request. The path omits the account segment because the service
    does not have your account identifier in this context.
    """

    status: Optional[str] = None
    """
    Current status of the upload at the moment the request returned. This is NOT a
    terminal state: the file is unified inline, but the durable loader has only
    accepted it, so the upload is still `Unifying`. Poll `poll_url` until the status
    reaches a terminal value (`Unified` or `Error`).
    """

    upload_id: Optional[int] = None
    """
    Identifier of the upload row, for polling this upload to a terminal state via
    `poll_url`.
    """
