# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
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
    "Bcc",
    "BccEmailSendingEmailAddressObject",
    "BccUnionMember2",
    "BccUnionMember2EmailSendingEmailAddressObject",
    "Cc",
    "CcEmailSendingEmailAddressObject",
    "CcUnionMember2",
    "CcUnionMember2EmailSendingEmailAddressObject",
    "ReplyTo",
    "ReplyToEmailSendingEmailAddressObject",
    "To",
    "ToEmailSendingEmailAddressObject",
    "ToUnionMember2",
    "ToUnionMember2EmailSendingEmailAddressObject",
]


class EmailSendingSendParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier of the account."""

    from_: Required[Annotated[From, PropertyInfo(alias="from")]]
    """Sender email address. Either a plain string or an object with address and name."""

    subject: Required[str]
    """Email subject line."""

    attachments: Iterable[Attachment]
    """File attachments and inline images."""

    bcc: Bcc
    """BCC recipient(s).

    A single email string, a named address object, or an array of either.
    """

    cc: Cc
    """CC recipient(s).

    A single email string, a named address object, or an array of either.
    """

    headers: Dict[str, str]
    """Custom email headers as key-value pairs."""

    html: str
    """HTML body of the email. Provide at least one of text or html (non-empty)."""

    reply_to: ReplyTo
    """Reply-to address. Either a plain string or an object with address and name."""

    text: str
    """Plain text body of the email. Provide at least one of text or html (non-empty)."""

    to: To
    """Recipient(s).

    Optional if cc or bcc is provided. A single email string, a named address
    object, or an array of either.
    """


class FromEmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Optional[str]
    """Display name for the email address (e.g., 'John Doe').

    Optional; set to null or leave it unset to send the address on its own.
    """


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
    """Must be 'inline'. Embeds the attachment in the email body."""

    filename: Required[str]
    """Filename for the attachment."""

    type: Required[str]
    """MIME type of the attachment (e.g., 'image/png', 'text/plain')."""


class AttachmentEmailSendingEmailAttachment(TypedDict, total=False):
    content: Required[str]
    """Base64-encoded content of the attachment."""

    disposition: Required[Literal["attachment"]]
    """Must be 'attachment'. Adds a standard file attachment."""

    filename: Required[str]
    """Filename for the attachment."""

    type: Required[str]
    """MIME type of the attachment (e.g., 'application/pdf', 'text/plain')."""


Attachment: TypeAlias = Union[AttachmentEmailSendingEmailInlineAttachment, AttachmentEmailSendingEmailAttachment]


class BccEmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Optional[str]
    """Display name for the email address (e.g., 'John Doe').

    Optional; set to null or leave it unset to send the address on its own.
    """


class BccUnionMember2EmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Optional[str]
    """Display name for the email address (e.g., 'John Doe').

    Optional; set to null or leave it unset to send the address on its own.
    """


BccUnionMember2: TypeAlias = Union[str, BccUnionMember2EmailSendingEmailAddressObject]

Bcc: TypeAlias = Union[str, BccEmailSendingEmailAddressObject, SequenceNotStr[BccUnionMember2]]


class CcEmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Optional[str]
    """Display name for the email address (e.g., 'John Doe').

    Optional; set to null or leave it unset to send the address on its own.
    """


class CcUnionMember2EmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Optional[str]
    """Display name for the email address (e.g., 'John Doe').

    Optional; set to null or leave it unset to send the address on its own.
    """


CcUnionMember2: TypeAlias = Union[str, CcUnionMember2EmailSendingEmailAddressObject]

Cc: TypeAlias = Union[str, CcEmailSendingEmailAddressObject, SequenceNotStr[CcUnionMember2]]


class ReplyToEmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Optional[str]
    """Display name for the email address (e.g., 'John Doe').

    Optional; set to null or leave it unset to send the address on its own.
    """


ReplyTo: TypeAlias = Union[str, ReplyToEmailSendingEmailAddressObject]


class ToEmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Optional[str]
    """Display name for the email address (e.g., 'John Doe').

    Optional; set to null or leave it unset to send the address on its own.
    """


class ToUnionMember2EmailSendingEmailAddressObject(TypedDict, total=False):
    address: Required[str]
    """Email address (e.g., 'user@example.com')."""

    name: Optional[str]
    """Display name for the email address (e.g., 'John Doe').

    Optional; set to null or leave it unset to send the address on its own.
    """


ToUnionMember2: TypeAlias = Union[str, ToUnionMember2EmailSendingEmailAddressObject]

To: TypeAlias = Union[str, ToEmailSendingEmailAddressObject, SequenceNotStr[ToUnionMember2]]
