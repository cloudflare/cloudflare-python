# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["EmailSendingSendRawParams"]


class EmailSendingSendRawParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of the account."""

    from_: Required[Annotated[str, PropertyInfo(alias="from")]]
    """Sender email address."""

    mime_message: Required[str]
    """The full MIME-encoded email message.

    Should include standard RFC 5322 headers such as From, To, Subject, and
    Content-Type. The from and recipients fields in the request body control SMTP
    envelope routing; the From and To headers in the MIME message control what the
    recipient's email client displays.
    """

    recipients: Required[SequenceNotStr[str]]
    """List of recipient email addresses."""
