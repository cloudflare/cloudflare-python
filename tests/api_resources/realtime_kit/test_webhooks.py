# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.realtime_kit import (
    WebhookEditWebhookResponse,
    WebhookGetWebhooksResponse,
    WebhookCreateWebhookResponse,
    WebhookDeleteWebhookResponse,
    WebhookGetWebhookByIDResponse,
    WebhookReplaceWebhookResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_webhook(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.create_webhook(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )
        assert_matches_type(WebhookCreateWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_method_create_webhook_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.create_webhook(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            enabled=True,
        )
        assert_matches_type(WebhookCreateWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_create_webhook(self, client: Cloudflare) -> None:
        response = client.realtime_kit.webhooks.with_raw_response.create_webhook(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookCreateWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_create_webhook(self, client: Cloudflare) -> None:
        with client.realtime_kit.webhooks.with_streaming_response.create_webhook(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookCreateWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create_webhook(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.create_webhook(
                app_id="app_id",
                account_id="",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.create_webhook(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )

    @parametrize
    def test_method_delete_webhook(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.delete_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(WebhookDeleteWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_delete_webhook(self, client: Cloudflare) -> None:
        response = client.realtime_kit.webhooks.with_raw_response.delete_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_delete_webhook(self, client: Cloudflare) -> None:
        with client.realtime_kit.webhooks.with_streaming_response.delete_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_webhook(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.delete_webhook(
                webhook_id="webhook_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.delete_webhook(
                webhook_id="webhook_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.delete_webhook(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @parametrize
    def test_method_edit_webhook(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.edit_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(WebhookEditWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_method_edit_webhook_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.edit_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            enabled=True,
            events=["meeting.started"],
            name="name",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )
        assert_matches_type(WebhookEditWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_edit_webhook(self, client: Cloudflare) -> None:
        response = client.realtime_kit.webhooks.with_raw_response.edit_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookEditWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_edit_webhook(self, client: Cloudflare) -> None:
        with client.realtime_kit.webhooks.with_streaming_response.edit_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookEditWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit_webhook(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.edit_webhook(
                webhook_id="webhook_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.edit_webhook(
                webhook_id="webhook_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.edit_webhook(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @parametrize
    def test_method_get_webhook_by_id(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.get_webhook_by_id(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(WebhookGetWebhookByIDResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_get_webhook_by_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.webhooks.with_raw_response.get_webhook_by_id(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookGetWebhookByIDResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_get_webhook_by_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.webhooks.with_streaming_response.get_webhook_by_id(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookGetWebhookByIDResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_webhook_by_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.get_webhook_by_id(
                webhook_id="webhook_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.get_webhook_by_id(
                webhook_id="webhook_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.get_webhook_by_id(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @parametrize
    def test_method_get_webhooks(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.get_webhooks(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookGetWebhooksResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_get_webhooks(self, client: Cloudflare) -> None:
        response = client.realtime_kit.webhooks.with_raw_response.get_webhooks(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookGetWebhooksResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_get_webhooks(self, client: Cloudflare) -> None:
        with client.realtime_kit.webhooks.with_streaming_response.get_webhooks(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookGetWebhooksResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_webhooks(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.get_webhooks(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.get_webhooks(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_replace_webhook(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.replace_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )
        assert_matches_type(WebhookReplaceWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_method_replace_webhook_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.realtime_kit.webhooks.replace_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            enabled=True,
        )
        assert_matches_type(WebhookReplaceWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_replace_webhook(self, client: Cloudflare) -> None:
        response = client.realtime_kit.webhooks.with_raw_response.replace_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookReplaceWebhookResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_replace_webhook(self, client: Cloudflare) -> None:
        with client.realtime_kit.webhooks.with_streaming_response.replace_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookReplaceWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_replace_webhook(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.replace_webhook(
                webhook_id="webhook_id",
                account_id="",
                app_id="app_id",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.replace_webhook(
                webhook_id="webhook_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.realtime_kit.webhooks.with_raw_response.replace_webhook(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_webhook(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.create_webhook(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )
        assert_matches_type(WebhookCreateWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_method_create_webhook_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.create_webhook(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            enabled=True,
        )
        assert_matches_type(WebhookCreateWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_create_webhook(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.webhooks.with_raw_response.create_webhook(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookCreateWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_create_webhook(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.webhooks.with_streaming_response.create_webhook(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookCreateWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create_webhook(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.create_webhook(
                app_id="app_id",
                account_id="",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.create_webhook(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )

    @parametrize
    async def test_method_delete_webhook(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.delete_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(WebhookDeleteWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_delete_webhook(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.webhooks.with_raw_response.delete_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_delete_webhook(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.webhooks.with_streaming_response.delete_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_webhook(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.delete_webhook(
                webhook_id="webhook_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.delete_webhook(
                webhook_id="webhook_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.delete_webhook(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @parametrize
    async def test_method_edit_webhook(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.edit_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(WebhookEditWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_method_edit_webhook_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.edit_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            enabled=True,
            events=["meeting.started"],
            name="name",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )
        assert_matches_type(WebhookEditWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_edit_webhook(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.webhooks.with_raw_response.edit_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookEditWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_edit_webhook(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.webhooks.with_streaming_response.edit_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookEditWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit_webhook(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.edit_webhook(
                webhook_id="webhook_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.edit_webhook(
                webhook_id="webhook_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.edit_webhook(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @parametrize
    async def test_method_get_webhook_by_id(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.get_webhook_by_id(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(WebhookGetWebhookByIDResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_get_webhook_by_id(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.webhooks.with_raw_response.get_webhook_by_id(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookGetWebhookByIDResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_get_webhook_by_id(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.webhooks.with_streaming_response.get_webhook_by_id(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookGetWebhookByIDResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_webhook_by_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.get_webhook_by_id(
                webhook_id="webhook_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.get_webhook_by_id(
                webhook_id="webhook_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.get_webhook_by_id(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @parametrize
    async def test_method_get_webhooks(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.get_webhooks(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookGetWebhooksResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_get_webhooks(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.webhooks.with_raw_response.get_webhooks(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookGetWebhooksResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_get_webhooks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.webhooks.with_streaming_response.get_webhooks(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookGetWebhooksResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_webhooks(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.get_webhooks(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.get_webhooks(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_replace_webhook(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.replace_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )
        assert_matches_type(WebhookReplaceWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_method_replace_webhook_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.realtime_kit.webhooks.replace_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            enabled=True,
        )
        assert_matches_type(WebhookReplaceWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_replace_webhook(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.webhooks.with_raw_response.replace_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookReplaceWebhookResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_replace_webhook(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.webhooks.with_streaming_response.replace_webhook(
            webhook_id="webhook_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            events=[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ],
            name="All events webhook",
            url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookReplaceWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_replace_webhook(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.replace_webhook(
                webhook_id="webhook_id",
                account_id="",
                app_id="app_id",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.replace_webhook(
                webhook_id="webhook_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.realtime_kit.webhooks.with_raw_response.replace_webhook(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                events=[
                    "meeting.started",
                    "meeting.ended",
                    "meeting.participantJoined",
                    "meeting.participantLeft",
                    "meeting.chatSynced",
                    "recording.statusUpdate",
                    "livestreaming.statusUpdate",
                    "meeting.transcript",
                    "meeting.summary",
                ],
                name="All events webhook",
                url="https://webhook.site/b23a5bbd-c7b0-4ced-a9e2-78ae7889897e",
            )
