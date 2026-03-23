# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "EmailSendingSendParams",
    "From",
    "FromEmailSendingEmailAddressObject",
    "Attachment",
    "AttachmentEmailSendingEmailInlineAttachment",
    "AttachmentEmailSendingEmailAttachment",
    "ReplyTo",
    "ReplyToEmailSendingEmailAddressObject",
]


class EmailSendingSendParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of the account."""

    from_: Required[Annotated[From, PropertyInfo(alias="from")]]
    """Sender email address. Either a plain string or an object with address and name."""

    subject: Required[str]
    """Email subject line."""

    to: Required[Union[str, SequenceNotStr[str]]]
    """Recipient(s). A single email string or an array of email strings."""

    attachments: Iterable[Attachment]
    """File attachments and inline images."""

    bcc: Union[str, SequenceNotStr[str]]
    """BCC recipient(s). A single email string or an array of email strings."""

    cc: Union[str, SequenceNotStr[str]]
    """CC recipient(s). A single email string or an array of email strings."""

    headers: Dict[str, str]
    """Custom email headers as key-value pairs."""

    html: str
    """HTML body of the email. At least one of text or html must be provided."""

    reply_to: ReplyTo
    """Reply-to address. Either a plain string or an object with address and name."""

    text: str
    """Plain text body of the email. At least one of text or html must be provided."""


class FromEmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Required[str]
    """Display name for the email address (e.g., 'John Doe')."""


From: TypeAlias = Union[str, FromEmailSendingEmailAddressObject]


class AttachmentEmailSendingEmailInlineAttachment(TypedDict, total=False):
    content: Required[str]
    """Base64-encoded content of the attachment."""

    content_id: Required[str]
    """
    Content ID used to reference this attachment in HTML via cid: URI (e.g.,
    <img src="cid:logo">).
    """

    disposition: Required[Literal["inline"]]
    """Must be 'inline'. Indicates the attachment is embedded in the email body."""

    filename: Required[str]
    """Filename for the attachment."""

    type: Required[str]
    """MIME type of the attachment (e.g., 'image/png', 'text/plain')."""


class AttachmentEmailSendingEmailAttachment(TypedDict, total=False):
    content: Required[str]
    """Base64-encoded content of the attachment."""

    disposition: Required[Literal["attachment"]]
    """Must be 'attachment'. Indicates a standard file attachment."""

    filename: Required[str]
    """Filename for the attachment."""

    type: Required[str]
    """MIME type of the attachment (e.g., 'application/pdf', 'text/plain')."""


Attachment: TypeAlias = Union[AttachmentEmailSendingEmailInlineAttachment, AttachmentEmailSendingEmailAttachment]


class ReplyToEmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Required[str]
    """Display name for the email address (e.g., 'John Doe')."""


ReplyTo: TypeAlias = Union[str, ReplyToEmailSendingEmailAddressObject]
