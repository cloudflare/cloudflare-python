# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Type, Union, Iterable, cast

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.email_sending import email_sending_send_params, email_sending_send_raw_params
from .subdomains.subdomains import (
    SubdomainsResource,
    AsyncSubdomainsResource,
    SubdomainsResourceWithRawResponse,
    AsyncSubdomainsResourceWithRawResponse,
    SubdomainsResourceWithStreamingResponse,
    AsyncSubdomainsResourceWithStreamingResponse,
)
from ...types.email_sending.email_sending_send_response import EmailSendingSendResponse
from ...types.email_sending.email_sending_send_raw_response import EmailSendingSendRawResponse

__all__ = ["EmailSendingResource", "AsyncEmailSendingResource"]


class EmailSendingResource(SyncAPIResource):
    @cached_property
    def subdomains(self) -> SubdomainsResource:
        return SubdomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailSendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return EmailSendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailSendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return EmailSendingResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        account_id: str | None = None,
        from_: email_sending_send_params.From,
        subject: str,
        to: Union[str, SequenceNotStr[str]],
        attachments: Iterable[email_sending_send_params.Attachment] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str]] | Omit = omit,
        cc: Union[str, SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        reply_to: email_sending_send_params.ReplyTo | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendingSendResponse:
        """
        Send an email

        Args:
          account_id: Identifier of the account.

          from_: Sender email address. Either a plain string or an object with address and name.

          subject: Email subject line.

          to: Recipient(s). A single email string or an array of email strings.

          attachments: File attachments and inline images.

          bcc: BCC recipient(s). A single email string or an array of email strings.

          cc: CC recipient(s). A single email string or an array of email strings.

          headers: Custom email headers as key-value pairs.

          html: HTML body of the email. At least one of text or html must be provided.

          reply_to: Reply-to address. Either a plain string or an object with address and name.

          text: Plain text body of the email. At least one of text or html must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email/sending/send", account_id=account_id),
            body=maybe_transform(
                {
                    "from_": from_,
                    "subject": subject,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "headers": headers,
                    "html": html,
                    "reply_to": reply_to,
                    "text": text,
                },
                email_sending_send_params.EmailSendingSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EmailSendingSendResponse]._unwrapper,
            ),
            cast_to=cast(Type[EmailSendingSendResponse], ResultWrapper[EmailSendingSendResponse]),
        )

    def send_raw(
        self,
        *,
        account_id: str | None = None,
        from_: str,
        mime_message: str,
        recipients: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendingSendRawResponse:
        """
        Send a raw MIME email

        Args:
          account_id: Identifier of the account.

          from_: Sender email address.

          mime_message: The full MIME-encoded email message. Should include standard RFC 5322 headers
              such as From, To, Subject, and Content-Type. The from and recipients fields in
              the request body control SMTP envelope routing; the From and To headers in the
              MIME message control what the recipient's email client displays.

          recipients: List of recipient email addresses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/email/sending/send_raw", account_id=account_id),
            body=maybe_transform(
                {
                    "from_": from_,
                    "mime_message": mime_message,
                    "recipients": recipients,
                },
                email_sending_send_raw_params.EmailSendingSendRawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EmailSendingSendRawResponse]._unwrapper,
            ),
            cast_to=cast(Type[EmailSendingSendRawResponse], ResultWrapper[EmailSendingSendRawResponse]),
        )


class AsyncEmailSendingResource(AsyncAPIResource):
    @cached_property
    def subdomains(self) -> AsyncSubdomainsResource:
        return AsyncSubdomainsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailSendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEmailSendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailSendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncEmailSendingResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        account_id: str | None = None,
        from_: email_sending_send_params.From,
        subject: str,
        to: Union[str, SequenceNotStr[str]],
        attachments: Iterable[email_sending_send_params.Attachment] | Omit = omit,
        bcc: Union[str, SequenceNotStr[str]] | Omit = omit,
        cc: Union[str, SequenceNotStr[str]] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        html: str | Omit = omit,
        reply_to: email_sending_send_params.ReplyTo | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendingSendResponse:
        """
        Send an email

        Args:
          account_id: Identifier of the account.

          from_: Sender email address. Either a plain string or an object with address and name.

          subject: Email subject line.

          to: Recipient(s). A single email string or an array of email strings.

          attachments: File attachments and inline images.

          bcc: BCC recipient(s). A single email string or an array of email strings.

          cc: CC recipient(s). A single email string or an array of email strings.

          headers: Custom email headers as key-value pairs.

          html: HTML body of the email. At least one of text or html must be provided.

          reply_to: Reply-to address. Either a plain string or an object with address and name.

          text: Plain text body of the email. At least one of text or html must be provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email/sending/send", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "subject": subject,
                    "to": to,
                    "attachments": attachments,
                    "bcc": bcc,
                    "cc": cc,
                    "headers": headers,
                    "html": html,
                    "reply_to": reply_to,
                    "text": text,
                },
                email_sending_send_params.EmailSendingSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EmailSendingSendResponse]._unwrapper,
            ),
            cast_to=cast(Type[EmailSendingSendResponse], ResultWrapper[EmailSendingSendResponse]),
        )

    async def send_raw(
        self,
        *,
        account_id: str | None = None,
        from_: str,
        mime_message: str,
        recipients: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EmailSendingSendRawResponse:
        """
        Send a raw MIME email

        Args:
          account_id: Identifier of the account.

          from_: Sender email address.

          mime_message: The full MIME-encoded email message. Should include standard RFC 5322 headers
              such as From, To, Subject, and Content-Type. The from and recipients fields in
              the request body control SMTP envelope routing; the From and To headers in the
              MIME message control what the recipient's email client displays.

          recipients: List of recipient email addresses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/email/sending/send_raw", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "from_": from_,
                    "mime_message": mime_message,
                    "recipients": recipients,
                },
                email_sending_send_raw_params.EmailSendingSendRawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[EmailSendingSendRawResponse]._unwrapper,
            ),
            cast_to=cast(Type[EmailSendingSendRawResponse], ResultWrapper[EmailSendingSendRawResponse]),
        )


class EmailSendingResourceWithRawResponse:
    def __init__(self, email_sending: EmailSendingResource) -> None:
        self._email_sending = email_sending

        self.send = to_raw_response_wrapper(
            email_sending.send,
        )
        self.send_raw = to_raw_response_wrapper(
            email_sending.send_raw,
        )

    @cached_property
    def subdomains(self) -> SubdomainsResourceWithRawResponse:
        return SubdomainsResourceWithRawResponse(self._email_sending.subdomains)


class AsyncEmailSendingResourceWithRawResponse:
    def __init__(self, email_sending: AsyncEmailSendingResource) -> None:
        self._email_sending = email_sending

        self.send = async_to_raw_response_wrapper(
            email_sending.send,
        )
        self.send_raw = async_to_raw_response_wrapper(
            email_sending.send_raw,
        )

    @cached_property
    def subdomains(self) -> AsyncSubdomainsResourceWithRawResponse:
        return AsyncSubdomainsResourceWithRawResponse(self._email_sending.subdomains)


class EmailSendingResourceWithStreamingResponse:
    def __init__(self, email_sending: EmailSendingResource) -> None:
        self._email_sending = email_sending

        self.send = to_streamed_response_wrapper(
            email_sending.send,
        )
        self.send_raw = to_streamed_response_wrapper(
            email_sending.send_raw,
        )

    @cached_property
    def subdomains(self) -> SubdomainsResourceWithStreamingResponse:
        return SubdomainsResourceWithStreamingResponse(self._email_sending.subdomains)


class AsyncEmailSendingResourceWithStreamingResponse:
    def __init__(self, email_sending: AsyncEmailSendingResource) -> None:
        self._email_sending = email_sending

        self.send = async_to_streamed_response_wrapper(
            email_sending.send,
        )
        self.send_raw = async_to_streamed_response_wrapper(
            email_sending.send_raw,
        )

    @cached_property
    def subdomains(self) -> AsyncSubdomainsResourceWithStreamingResponse:
        return AsyncSubdomainsResourceWithStreamingResponse(self._email_sending.subdomains)
