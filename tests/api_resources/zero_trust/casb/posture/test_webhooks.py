# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.casb.posture import (
    WebhookGetResponse,
    WebhookListResponse,
    WebhookCreateResponse,
    WebhookDeleteResponse,
    WebhookUpdateResponse,
    WebhookEvaluateResponse,
    WebhookEvaluateExistingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
        )
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            headers=[
                {
                    "key": "Authorization",
                    "value": "Bearer token123",
                },
                {
                    "key": "X-Custom-Header",
                    "value": "value",
                },
            ],
            signing_secret="my-secret-key",
        )
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.webhooks.with_raw_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.webhooks.with_streaming_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.create(
                account_id="",
                authentication_type="Bearer Auth",
                destination_url="https://example.com/webhook",
                label="Send to Slack",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.update(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            status="enabled",
        )
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.update(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            status="enabled",
            headers=[
                {
                    "key": "Authorization",
                    "value": "Bearer token123",
                },
                {
                    "key": "X-Custom-Header",
                    "value": "value",
                },
            ],
            signing_secret="my-secret-key",
        )
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.webhooks.with_raw_response.update(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            status="enabled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.webhooks.with_streaming_response.update(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            status="enabled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.update(
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                authentication_type="Bearer Auth",
                destination_url="https://example.com/webhook",
                label="Send to Slack",
                status="enabled",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.update(
                webhook_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                authentication_type="Bearer Auth",
                destination_url="https://example.com/webhook",
                label="Send to Slack",
                status="enabled",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(SyncSinglePage[WebhookListResponse], webhook, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.webhooks.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(SyncSinglePage[WebhookListResponse], webhook, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.webhooks.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(SyncSinglePage[WebhookListResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.delete(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.webhooks.with_raw_response.delete(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.webhooks.with_streaming_response.delete(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.delete(
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.delete(
                webhook_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    def test_method_evaluate(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.evaluate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
        )
        assert_matches_type(Optional[WebhookEvaluateResponse], webhook, path=["response"])

    @parametrize
    def test_method_evaluate_with_all_params(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.evaluate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            headers=[
                {
                    "key": "Authorization",
                    "value": "Bearer token123",
                },
                {
                    "key": "X-Custom-Header",
                    "value": "value",
                },
            ],
            signing_secret="my-secret-key",
        )
        assert_matches_type(Optional[WebhookEvaluateResponse], webhook, path=["response"])

    @parametrize
    def test_raw_response_evaluate(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookEvaluateResponse], webhook, path=["response"])

    @parametrize
    def test_streaming_response_evaluate(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.webhooks.with_streaming_response.evaluate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookEvaluateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_evaluate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate(
                account_id="",
                authentication_type="Bearer Auth",
                destination_url="https://example.com/webhook",
            )

    @parametrize
    def test_method_evaluate_existing(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.evaluate_existing(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[WebhookEvaluateExistingResponse], webhook, path=["response"])

    @parametrize
    def test_raw_response_evaluate_existing(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate_existing(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookEvaluateExistingResponse], webhook, path=["response"])

    @parametrize
    def test_streaming_response_evaluate_existing(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.webhooks.with_streaming_response.evaluate_existing(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookEvaluateExistingResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_evaluate_existing(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate_existing(
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate_existing(
                webhook_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        webhook = client.zero_trust.casb.posture.webhooks.get(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[WebhookGetResponse], webhook, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.casb.posture.webhooks.with_raw_response.get(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Optional[WebhookGetResponse], webhook, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.casb.posture.webhooks.with_streaming_response.get(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Optional[WebhookGetResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.get(
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            client.zero_trust.casb.posture.webhooks.with_raw_response.get(
                webhook_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
        )
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            headers=[
                {
                    "key": "Authorization",
                    "value": "Bearer token123",
                },
                {
                    "key": "X-Custom-Header",
                    "value": "value",
                },
            ],
            signing_secret="my-secret-key",
        )
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.webhooks.with_raw_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.webhooks.with_streaming_response.create(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookCreateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.create(
                account_id="",
                authentication_type="Bearer Auth",
                destination_url="https://example.com/webhook",
                label="Send to Slack",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.update(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            status="enabled",
        )
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.update(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            status="enabled",
            headers=[
                {
                    "key": "Authorization",
                    "value": "Bearer token123",
                },
                {
                    "key": "X-Custom-Header",
                    "value": "value",
                },
            ],
            signing_secret="my-secret-key",
        )
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.webhooks.with_raw_response.update(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            status="enabled",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.webhooks.with_streaming_response.update(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            label="Send to Slack",
            status="enabled",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookUpdateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.update(
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                authentication_type="Bearer Auth",
                destination_url="https://example.com/webhook",
                label="Send to Slack",
                status="enabled",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.update(
                webhook_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
                authentication_type="Bearer Auth",
                destination_url="https://example.com/webhook",
                label="Send to Slack",
                status="enabled",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(AsyncSinglePage[WebhookListResponse], webhook, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.webhooks.with_raw_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(AsyncSinglePage[WebhookListResponse], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.webhooks.with_streaming_response.list(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(AsyncSinglePage[WebhookListResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.delete(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.webhooks.with_raw_response.delete(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.webhooks.with_streaming_response.delete(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookDeleteResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.delete(
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.delete(
                webhook_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    async def test_method_evaluate(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.evaluate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
        )
        assert_matches_type(Optional[WebhookEvaluateResponse], webhook, path=["response"])

    @parametrize
    async def test_method_evaluate_with_all_params(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.evaluate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
            headers=[
                {
                    "key": "Authorization",
                    "value": "Bearer token123",
                },
                {
                    "key": "X-Custom-Header",
                    "value": "value",
                },
            ],
            signing_secret="my-secret-key",
        )
        assert_matches_type(Optional[WebhookEvaluateResponse], webhook, path=["response"])

    @parametrize
    async def test_raw_response_evaluate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookEvaluateResponse], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.webhooks.with_streaming_response.evaluate(
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
            authentication_type="Bearer Auth",
            destination_url="https://example.com/webhook",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookEvaluateResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_evaluate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate(
                account_id="",
                authentication_type="Bearer Auth",
                destination_url="https://example.com/webhook",
            )

    @parametrize
    async def test_method_evaluate_existing(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.evaluate_existing(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[WebhookEvaluateExistingResponse], webhook, path=["response"])

    @parametrize
    async def test_raw_response_evaluate_existing(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate_existing(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookEvaluateExistingResponse], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate_existing(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.webhooks.with_streaming_response.evaluate_existing(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookEvaluateExistingResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_evaluate_existing(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate_existing(
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.evaluate_existing(
                webhook_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        webhook = await async_client.zero_trust.casb.posture.webhooks.get(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )
        assert_matches_type(Optional[WebhookGetResponse], webhook, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.casb.posture.webhooks.with_raw_response.get(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Optional[WebhookGetResponse], webhook, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.casb.posture.webhooks.with_streaming_response.get(
            webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="46148281d8a93d002ef242d8b0d5f9f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Optional[WebhookGetResponse], webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.get(
                webhook_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `webhook_id` but received ''"):
            await async_client.zero_trust.casb.posture.webhooks.with_raw_response.get(
                webhook_id="",
                account_id="46148281d8a93d002ef242d8b0d5f9f6",
            )
