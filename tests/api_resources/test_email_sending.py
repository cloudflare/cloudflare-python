# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.email_sending import (
    EmailSendingSendResponse,
    EmailSendingSendRawResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmailSending:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_send(self, client: Cloudflare) -> None:
        email_sending = client.email_sending.send(
            account_id="account_id",
            from_="sender@example.com",
            subject="Monthly Report",
            to=["recipient@example.com"],
        )
        assert_matches_type(EmailSendingSendResponse, email_sending, path=["response"])

    @parametrize
    def test_method_send_with_all_params(self, client: Cloudflare) -> None:
        email_sending = client.email_sending.send(
            account_id="account_id",
            from_="sender@example.com",
            subject="Monthly Report",
            to=["recipient@example.com"],
            attachments=[
                {
                    "content": "JVBERi0xLjQK...",
                    "disposition": "attachment",
                    "filename": "report.pdf",
                    "type": "application/pdf",
                }
            ],
            bcc="user@example.com",
            cc="user@example.com",
            headers={"X-Custom-Header": "value"},
            html="<h1>Hello</h1><p>Please find your report attached.</p>",
            reply_to="user@example.com",
            text="Hello\n\nPlease find your report attached.",
        )
        assert_matches_type(EmailSendingSendResponse, email_sending, path=["response"])

    @parametrize
    def test_raw_response_send(self, client: Cloudflare) -> None:
        response = client.email_sending.with_raw_response.send(
            account_id="account_id",
            from_="sender@example.com",
            subject="Monthly Report",
            to=["recipient@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_sending = response.parse()
        assert_matches_type(EmailSendingSendResponse, email_sending, path=["response"])

    @parametrize
    def test_streaming_response_send(self, client: Cloudflare) -> None:
        with client.email_sending.with_streaming_response.send(
            account_id="account_id",
            from_="sender@example.com",
            subject="Monthly Report",
            to=["recipient@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_sending = response.parse()
            assert_matches_type(EmailSendingSendResponse, email_sending, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_sending.with_raw_response.send(
                account_id="",
                from_="sender@example.com",
                subject="Monthly Report",
                to=["recipient@example.com"],
            )

    @parametrize
    def test_method_send_raw(self, client: Cloudflare) -> None:
        email_sending = client.email_sending.send_raw(
            account_id="account_id",
            from_="sender@example.com",
            mime_message="From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Hello\r\nContent-Type: text/plain\r\n\r\nHello, World!",
            recipients=["recipient@example.com"],
        )
        assert_matches_type(EmailSendingSendRawResponse, email_sending, path=["response"])

    @parametrize
    def test_raw_response_send_raw(self, client: Cloudflare) -> None:
        response = client.email_sending.with_raw_response.send_raw(
            account_id="account_id",
            from_="sender@example.com",
            mime_message="From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Hello\r\nContent-Type: text/plain\r\n\r\nHello, World!",
            recipients=["recipient@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_sending = response.parse()
        assert_matches_type(EmailSendingSendRawResponse, email_sending, path=["response"])

    @parametrize
    def test_streaming_response_send_raw(self, client: Cloudflare) -> None:
        with client.email_sending.with_streaming_response.send_raw(
            account_id="account_id",
            from_="sender@example.com",
            mime_message="From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Hello\r\nContent-Type: text/plain\r\n\r\nHello, World!",
            recipients=["recipient@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_sending = response.parse()
            assert_matches_type(EmailSendingSendRawResponse, email_sending, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send_raw(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_sending.with_raw_response.send_raw(
                account_id="",
                from_="sender@example.com",
                mime_message="From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Hello\r\nContent-Type: text/plain\r\n\r\nHello, World!",
                recipients=["recipient@example.com"],
            )


class TestAsyncEmailSending:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_send(self, async_client: AsyncCloudflare) -> None:
        email_sending = await async_client.email_sending.send(
            account_id="account_id",
            from_="sender@example.com",
            subject="Monthly Report",
            to=["recipient@example.com"],
        )
        assert_matches_type(EmailSendingSendResponse, email_sending, path=["response"])

    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncCloudflare) -> None:
        email_sending = await async_client.email_sending.send(
            account_id="account_id",
            from_="sender@example.com",
            subject="Monthly Report",
            to=["recipient@example.com"],
            attachments=[
                {
                    "content": "JVBERi0xLjQK...",
                    "disposition": "attachment",
                    "filename": "report.pdf",
                    "type": "application/pdf",
                }
            ],
            bcc="user@example.com",
            cc="user@example.com",
            headers={"X-Custom-Header": "value"},
            html="<h1>Hello</h1><p>Please find your report attached.</p>",
            reply_to="user@example.com",
            text="Hello\n\nPlease find your report attached.",
        )
        assert_matches_type(EmailSendingSendResponse, email_sending, path=["response"])

    @parametrize
    async def test_raw_response_send(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.with_raw_response.send(
            account_id="account_id",
            from_="sender@example.com",
            subject="Monthly Report",
            to=["recipient@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_sending = await response.parse()
        assert_matches_type(EmailSendingSendResponse, email_sending, path=["response"])

    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.with_streaming_response.send(
            account_id="account_id",
            from_="sender@example.com",
            subject="Monthly Report",
            to=["recipient@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_sending = await response.parse()
            assert_matches_type(EmailSendingSendResponse, email_sending, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_sending.with_raw_response.send(
                account_id="",
                from_="sender@example.com",
                subject="Monthly Report",
                to=["recipient@example.com"],
            )

    @parametrize
    async def test_method_send_raw(self, async_client: AsyncCloudflare) -> None:
        email_sending = await async_client.email_sending.send_raw(
            account_id="account_id",
            from_="sender@example.com",
            mime_message="From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Hello\r\nContent-Type: text/plain\r\n\r\nHello, World!",
            recipients=["recipient@example.com"],
        )
        assert_matches_type(EmailSendingSendRawResponse, email_sending, path=["response"])

    @parametrize
    async def test_raw_response_send_raw(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_sending.with_raw_response.send_raw(
            account_id="account_id",
            from_="sender@example.com",
            mime_message="From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Hello\r\nContent-Type: text/plain\r\n\r\nHello, World!",
            recipients=["recipient@example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        email_sending = await response.parse()
        assert_matches_type(EmailSendingSendRawResponse, email_sending, path=["response"])

    @parametrize
    async def test_streaming_response_send_raw(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_sending.with_streaming_response.send_raw(
            account_id="account_id",
            from_="sender@example.com",
            mime_message="From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Hello\r\nContent-Type: text/plain\r\n\r\nHello, World!",
            recipients=["recipient@example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            email_sending = await response.parse()
            assert_matches_type(EmailSendingSendRawResponse, email_sending, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send_raw(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_sending.with_raw_response.send_raw(
                account_id="",
                from_="sender@example.com",
                mime_message="From: sender@example.com\r\nTo: recipient@example.com\r\nSubject: Hello\r\nContent-Type: text/plain\r\n\r\nHello, World!",
                recipients=["recipient@example.com"],
            )
