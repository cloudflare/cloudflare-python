# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.alerting.destinations import (
    Webhooks,
    WebhookCreateResponse,
    WebhookDeleteResponse,
    WebhookUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        webhook = client.alerting.destinations.webhooks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.alerting.destinations.webhooks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            secret="secret",
        )
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.webhooks.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.alerting.destinations.webhooks.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.webhooks.with_raw_response.create(
                account_id="",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        webhook = client.alerting.destinations.webhooks.update(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.alerting.destinations.webhooks.update(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            secret="secret",
        )
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.webhooks.with_raw_response.update(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.alerting.destinations.webhooks.with_streaming_response.update(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.webhooks.with_raw_response.update(
                webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.alerting.destinations.webhooks.with_raw_response.update(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        webhook = client.alerting.destinations.webhooks.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Webhooks], webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.webhooks.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncSinglePage[Webhooks], webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.alerting.destinations.webhooks.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncSinglePage[Webhooks], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.webhooks.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        webhook = client.alerting.destinations.webhooks.delete(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.webhooks.with_raw_response.delete(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.alerting.destinations.webhooks.with_streaming_response.delete(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.webhooks.with_raw_response.delete(
                webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.alerting.destinations.webhooks.with_raw_response.delete(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        webhook = client.alerting.destinations.webhooks.get(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Webhooks], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.alerting.destinations.webhooks.with_raw_response.get(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[Webhooks], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.alerting.destinations.webhooks.with_streaming_response.get(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[Webhooks], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.destinations.webhooks.with_raw_response.get(
                webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.alerting.destinations.webhooks.with_raw_response.get(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.destinations.webhooks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.destinations.webhooks.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            secret="secret",
        )
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.webhooks.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.webhooks.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.webhooks.with_raw_response.create(
                account_id="",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.destinations.webhooks.update(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.destinations.webhooks.update(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            secret="secret",
        )
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.webhooks.with_raw_response.update(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.webhooks.with_streaming_response.update(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="Slack Webhook",
            url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.webhooks.with_raw_response.update(
                webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.alerting.destinations.webhooks.with_raw_response.update(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                name="Slack Webhook",
                url="https://hooks.slack.com/services/Ds3fdBFbV/456464Gdd",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.destinations.webhooks.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Webhooks], webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.webhooks.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncSinglePage[Webhooks], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.webhooks.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncSinglePage[Webhooks], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.webhooks.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.destinations.webhooks.delete(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.webhooks.with_raw_response.delete(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.webhooks.with_streaming_response.delete(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.webhooks.with_raw_response.delete(
                webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.alerting.destinations.webhooks.with_raw_response.delete(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.alerting.destinations.webhooks.get(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[Webhooks], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.destinations.webhooks.with_raw_response.get(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[Webhooks], webhook, path=["response"])

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.destinations.webhooks.with_streaming_response.get(
            webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[Webhooks], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="prism errors - https://github.com/cloudflare/cloudflare-python/actions/runs/9327225061/job/25676826349?pr=482#step:5:4291"
    )
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.destinations.webhooks.with_raw_response.get(
                webhook_id="b115d5ec-15c6-41ee-8b76-92c449b5227b",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.alerting.destinations.webhooks.with_raw_response.get(
                webhook_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
