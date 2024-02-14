# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.alerting.v3s.destinations import (
    WebhookUpdateResponse,
    WebhookDeleteResponse,
    WebhookGetResponse,
    WebhookNotificationWebhooksCreateAWebhookResponse,
    WebhookNotificationWebhooksListWebhooksResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.alerting.v3s.destinations import webhook_update_params
from cloudflare.types.alerting.v3s.destinations import webhook_notification_webhooks_create_a_webhook_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        webhook = client.alerting.v3s.destinations.webhooks.update(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.alerting.v3s.destinations.webhooks.update(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            secret="string",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.alerting.v3s.destinations.webhooks.with_raw_response.update(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.alerting.v3s.destinations.webhooks.with_streaming_response.update(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3s.destinations.webhooks.with_raw_response.update(
                "b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.alerting.v3s.destinations.webhooks.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        webhook = client.alerting.v3s.destinations.webhooks.delete(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WebhookDeleteResponse], webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.alerting.v3s.destinations.webhooks.with_raw_response.delete(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookDeleteResponse], webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.alerting.v3s.destinations.webhooks.with_streaming_response.delete(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookDeleteResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3s.destinations.webhooks.with_raw_response.delete(
                "b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.alerting.v3s.destinations.webhooks.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        webhook = client.alerting.v3s.destinations.webhooks.get(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookGetResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.alerting.v3s.destinations.webhooks.with_raw_response.get(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookGetResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.alerting.v3s.destinations.webhooks.with_streaming_response.get(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookGetResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3s.destinations.webhooks.with_raw_response.get(
                "b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.alerting.v3s.destinations.webhooks.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_notification_webhooks_create_a_webhook(self, client: Cloudflare) -> None:
        webhook = client.alerting.v3s.destinations.webhooks.notification_webhooks_create_a_webhook(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )
        assert_matches_type(WebhookNotificationWebhooksCreateAWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_notification_webhooks_create_a_webhook_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.alerting.v3s.destinations.webhooks.notification_webhooks_create_a_webhook(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            secret="string",
        )
        assert_matches_type(WebhookNotificationWebhooksCreateAWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_notification_webhooks_create_a_webhook(self, client: Cloudflare) -> None:
        response = client.alerting.v3s.destinations.webhooks.with_raw_response.notification_webhooks_create_a_webhook(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookNotificationWebhooksCreateAWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_notification_webhooks_create_a_webhook(self, client: Cloudflare) -> None:
        with client.alerting.v3s.destinations.webhooks.with_streaming_response.notification_webhooks_create_a_webhook(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookNotificationWebhooksCreateAWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_notification_webhooks_create_a_webhook(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3s.destinations.webhooks.with_raw_response.notification_webhooks_create_a_webhook(
                "",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_notification_webhooks_list_webhooks(self, client: Cloudflare) -> None:
        webhook = client.alerting.v3s.destinations.webhooks.notification_webhooks_list_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WebhookNotificationWebhooksListWebhooksResponse], webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_notification_webhooks_list_webhooks(self, client: Cloudflare) -> None:
        response = client.alerting.v3s.destinations.webhooks.with_raw_response.notification_webhooks_list_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookNotificationWebhooksListWebhooksResponse], webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_notification_webhooks_list_webhooks(self, client: Cloudflare) -> None:
        with client.alerting.v3s.destinations.webhooks.with_streaming_response.notification_webhooks_list_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookNotificationWebhooksListWebhooksResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_notification_webhooks_list_webhooks(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3s.destinations.webhooks.with_raw_response.notification_webhooks_list_webhooks(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.v3s.destinations.webhooks.update(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.v3s.destinations.webhooks.update(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            secret="string",
        )
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.v3s.destinations.webhooks.with_raw_response.update(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.v3s.destinations.webhooks.with_streaming_response.update(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookUpdateResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.update(
                "b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.v3s.destinations.webhooks.delete(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WebhookDeleteResponse], webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.v3s.destinations.webhooks.with_raw_response.delete(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookDeleteResponse], webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.v3s.destinations.webhooks.with_streaming_response.delete(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookDeleteResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.delete(
                "b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.v3s.destinations.webhooks.get(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookGetResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.v3s.destinations.webhooks.with_raw_response.get(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookGetResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.v3s.destinations.webhooks.with_streaming_response.get(
            "b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookGetResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.get(
                "b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_notification_webhooks_create_a_webhook(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.v3s.destinations.webhooks.notification_webhooks_create_a_webhook(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )
        assert_matches_type(WebhookNotificationWebhooksCreateAWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_notification_webhooks_create_a_webhook_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        webhook = await async_client.alerting.v3s.destinations.webhooks.notification_webhooks_create_a_webhook(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            secret="string",
        )
        assert_matches_type(WebhookNotificationWebhooksCreateAWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_notification_webhooks_create_a_webhook(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.v3s.destinations.webhooks.with_raw_response.notification_webhooks_create_a_webhook(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookNotificationWebhooksCreateAWebhookResponse, webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_notification_webhooks_create_a_webhook(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.alerting.v3s.destinations.webhooks.with_streaming_response.notification_webhooks_create_a_webhook(
            "023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookNotificationWebhooksCreateAWebhookResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_notification_webhooks_create_a_webhook(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.notification_webhooks_create_a_webhook(
                "",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_notification_webhooks_list_webhooks(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.v3s.destinations.webhooks.notification_webhooks_list_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[WebhookNotificationWebhooksListWebhooksResponse], webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_notification_webhooks_list_webhooks(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.notification_webhooks_list_webhooks(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookNotificationWebhooksListWebhooksResponse], webhook, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_notification_webhooks_list_webhooks(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.v3s.destinations.webhooks.with_streaming_response.notification_webhooks_list_webhooks(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookNotificationWebhooksListWebhooksResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_notification_webhooks_list_webhooks(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3s.destinations.webhooks.with_raw_response.notification_webhooks_list_webhooks(
                "",
            )
