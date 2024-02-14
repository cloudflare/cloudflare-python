# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.stream import (
    WebhookDeleteResponse,
    WebhookStreamWebhookCreateWebhooksResponse,
    WebhookStreamWebhookViewWebhooksResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import webhook_stream_webhook_create_webhooks_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        webhook = client.stream.webhooks.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.webhooks.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.webhooks.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_webhook_create_webhooks(self, client: Cloudflare) -> None:
        webhook = client.stream.webhooks.stream_webhook_create_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
            notification_url="https://example.com",
        )
        assert_matches_type(WebhookStreamWebhookCreateWebhooksResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_webhook_create_webhooks(self, client: Cloudflare) -> None:
        response = client.stream.webhooks.with_raw_response.stream_webhook_create_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
            notification_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookStreamWebhookCreateWebhooksResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_webhook_create_webhooks(self, client: Cloudflare) -> None:
        with client.stream.webhooks.with_streaming_response.stream_webhook_create_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
            notification_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookStreamWebhookCreateWebhooksResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_webhook_create_webhooks(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.webhooks.with_raw_response.stream_webhook_create_webhooks(
                "",
                notification_url="https://example.com",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_webhook_view_webhooks(self, client: Cloudflare) -> None:
        webhook = client.stream.webhooks.stream_webhook_view_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookStreamWebhookViewWebhooksResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_webhook_view_webhooks(self, client: Cloudflare) -> None:
        response = client.stream.webhooks.with_raw_response.stream_webhook_view_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookStreamWebhookViewWebhooksResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_webhook_view_webhooks(self, client: Cloudflare) -> None:
        with client.stream.webhooks.with_streaming_response.stream_webhook_view_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookStreamWebhookViewWebhooksResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_webhook_view_webhooks(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.webhooks.with_raw_response.stream_webhook_view_webhooks(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.stream.webhooks.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.webhooks.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.webhooks.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_webhook_create_webhooks(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.stream.webhooks.stream_webhook_create_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
            notification_url="https://example.com",
        )
        assert_matches_type(WebhookStreamWebhookCreateWebhooksResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_webhook_create_webhooks(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.webhooks.with_raw_response.stream_webhook_create_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
            notification_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookStreamWebhookCreateWebhooksResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_webhook_create_webhooks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.webhooks.with_streaming_response.stream_webhook_create_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
            notification_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookStreamWebhookCreateWebhooksResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_webhook_create_webhooks(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.webhooks.with_raw_response.stream_webhook_create_webhooks(
                "",
                notification_url="https://example.com",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_webhook_view_webhooks(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.stream.webhooks.stream_webhook_view_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookStreamWebhookViewWebhooksResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_webhook_view_webhooks(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.webhooks.with_raw_response.stream_webhook_view_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookStreamWebhookViewWebhooksResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_webhook_view_webhooks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.webhooks.with_streaming_response.stream_webhook_view_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookStreamWebhookViewWebhooksResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_webhook_view_webhooks(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.webhooks.with_raw_response.stream_webhook_view_webhooks(
                "",
            )
