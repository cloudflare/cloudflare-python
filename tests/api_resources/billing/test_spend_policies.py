# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.billing import (
    SpendPolicyGetResponse,
    SpendPolicyListResponse,
    SpendPolicyCreateResponse,
    SpendPolicyDeleteResponse,
    SpendPolicyUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpendPolicies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        spend_policy = client.billing.spend_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Durable Objects alert",
            product_id="durable_objects",
            threshold_cents=100,
        )
        assert_matches_type(SpendPolicyCreateResponse, spend_policy, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        spend_policy = client.billing.spend_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Durable Objects alert",
            product_id="durable_objects",
            threshold_cents=100,
            notification_email="billing@example.com",
        )
        assert_matches_type(SpendPolicyCreateResponse, spend_policy, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.billing.spend_policies.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Durable Objects alert",
            product_id="durable_objects",
            threshold_cents=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = response.parse()
        assert_matches_type(SpendPolicyCreateResponse, spend_policy, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.billing.spend_policies.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Durable Objects alert",
            product_id="durable_objects",
            threshold_cents=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = response.parse()
            assert_matches_type(SpendPolicyCreateResponse, spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.billing.spend_policies.with_raw_response.create(
                account_id="",
                action="notification",
                enabled=True,
                name="Durable Objects alert",
                product_id="durable_objects",
                threshold_cents=100,
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        spend_policy = client.billing.spend_policies.update(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Workers cap",
            product_id="workers",
            threshold_cents=100,
            if_match='"3"',
        )
        assert_matches_type(SpendPolicyUpdateResponse, spend_policy, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        spend_policy = client.billing.spend_policies.update(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Workers cap",
            product_id="workers",
            threshold_cents=100,
            if_match='"3"',
            notification_email="billing@example.com",
        )
        assert_matches_type(SpendPolicyUpdateResponse, spend_policy, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.billing.spend_policies.with_raw_response.update(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Workers cap",
            product_id="workers",
            threshold_cents=100,
            if_match='"3"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = response.parse()
        assert_matches_type(SpendPolicyUpdateResponse, spend_policy, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.billing.spend_policies.with_streaming_response.update(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Workers cap",
            product_id="workers",
            threshold_cents=100,
            if_match='"3"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = response.parse()
            assert_matches_type(SpendPolicyUpdateResponse, spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.billing.spend_policies.with_raw_response.update(
                policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                account_id="",
                action="notification",
                enabled=True,
                name="Workers cap",
                product_id="workers",
                threshold_cents=100,
                if_match='"3"',
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.billing.spend_policies.with_raw_response.update(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="notification",
                enabled=True,
                name="Workers cap",
                product_id="workers",
                threshold_cents=100,
                if_match='"3"',
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        spend_policy = client.billing.spend_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[SpendPolicyListResponse], spend_policy, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.billing.spend_policies.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = response.parse()
        assert_matches_type(SyncSinglePage[SpendPolicyListResponse], spend_policy, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.billing.spend_policies.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = response.parse()
            assert_matches_type(SyncSinglePage[SpendPolicyListResponse], spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.billing.spend_policies.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        spend_policy = client.billing.spend_policies.delete(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"3"',
        )
        assert_matches_type(SpendPolicyDeleteResponse, spend_policy, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.billing.spend_policies.with_raw_response.delete(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"3"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = response.parse()
        assert_matches_type(SpendPolicyDeleteResponse, spend_policy, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.billing.spend_policies.with_streaming_response.delete(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"3"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = response.parse()
            assert_matches_type(SpendPolicyDeleteResponse, spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.billing.spend_policies.with_raw_response.delete(
                policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                account_id="",
                if_match='"3"',
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.billing.spend_policies.with_raw_response.delete(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                if_match='"3"',
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        spend_policy = client.billing.spend_policies.get(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SpendPolicyGetResponse, spend_policy, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.billing.spend_policies.with_raw_response.get(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = response.parse()
        assert_matches_type(SpendPolicyGetResponse, spend_policy, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.billing.spend_policies.with_streaming_response.get(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = response.parse()
            assert_matches_type(SpendPolicyGetResponse, spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.billing.spend_policies.with_raw_response.get(
                policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            client.billing.spend_policies.with_raw_response.get(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSpendPolicies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        spend_policy = await async_client.billing.spend_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Durable Objects alert",
            product_id="durable_objects",
            threshold_cents=100,
        )
        assert_matches_type(SpendPolicyCreateResponse, spend_policy, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        spend_policy = await async_client.billing.spend_policies.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Durable Objects alert",
            product_id="durable_objects",
            threshold_cents=100,
            notification_email="billing@example.com",
        )
        assert_matches_type(SpendPolicyCreateResponse, spend_policy, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.billing.spend_policies.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Durable Objects alert",
            product_id="durable_objects",
            threshold_cents=100,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = await response.parse()
        assert_matches_type(SpendPolicyCreateResponse, spend_policy, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.billing.spend_policies.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Durable Objects alert",
            product_id="durable_objects",
            threshold_cents=100,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = await response.parse()
            assert_matches_type(SpendPolicyCreateResponse, spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.billing.spend_policies.with_raw_response.create(
                account_id="",
                action="notification",
                enabled=True,
                name="Durable Objects alert",
                product_id="durable_objects",
                threshold_cents=100,
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        spend_policy = await async_client.billing.spend_policies.update(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Workers cap",
            product_id="workers",
            threshold_cents=100,
            if_match='"3"',
        )
        assert_matches_type(SpendPolicyUpdateResponse, spend_policy, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        spend_policy = await async_client.billing.spend_policies.update(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Workers cap",
            product_id="workers",
            threshold_cents=100,
            if_match='"3"',
            notification_email="billing@example.com",
        )
        assert_matches_type(SpendPolicyUpdateResponse, spend_policy, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.billing.spend_policies.with_raw_response.update(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Workers cap",
            product_id="workers",
            threshold_cents=100,
            if_match='"3"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = await response.parse()
        assert_matches_type(SpendPolicyUpdateResponse, spend_policy, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.billing.spend_policies.with_streaming_response.update(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            action="notification",
            enabled=True,
            name="Workers cap",
            product_id="workers",
            threshold_cents=100,
            if_match='"3"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = await response.parse()
            assert_matches_type(SpendPolicyUpdateResponse, spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.billing.spend_policies.with_raw_response.update(
                policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                account_id="",
                action="notification",
                enabled=True,
                name="Workers cap",
                product_id="workers",
                threshold_cents=100,
                if_match='"3"',
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.billing.spend_policies.with_raw_response.update(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                action="notification",
                enabled=True,
                name="Workers cap",
                product_id="workers",
                threshold_cents=100,
                if_match='"3"',
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        spend_policy = await async_client.billing.spend_policies.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[SpendPolicyListResponse], spend_policy, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.billing.spend_policies.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = await response.parse()
        assert_matches_type(AsyncSinglePage[SpendPolicyListResponse], spend_policy, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.billing.spend_policies.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = await response.parse()
            assert_matches_type(AsyncSinglePage[SpendPolicyListResponse], spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.billing.spend_policies.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        spend_policy = await async_client.billing.spend_policies.delete(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"3"',
        )
        assert_matches_type(SpendPolicyDeleteResponse, spend_policy, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.billing.spend_policies.with_raw_response.delete(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"3"',
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = await response.parse()
        assert_matches_type(SpendPolicyDeleteResponse, spend_policy, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.billing.spend_policies.with_streaming_response.delete(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            if_match='"3"',
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = await response.parse()
            assert_matches_type(SpendPolicyDeleteResponse, spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.billing.spend_policies.with_raw_response.delete(
                policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                account_id="",
                if_match='"3"',
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.billing.spend_policies.with_raw_response.delete(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                if_match='"3"',
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        spend_policy = await async_client.billing.spend_policies.get(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SpendPolicyGetResponse, spend_policy, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.billing.spend_policies.with_raw_response.get(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        spend_policy = await response.parse()
        assert_matches_type(SpendPolicyGetResponse, spend_policy, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.billing.spend_policies.with_streaming_response.get(
            policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            spend_policy = await response.parse()
            assert_matches_type(SpendPolicyGetResponse, spend_policy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.billing.spend_policies.with_raw_response.get(
                policy_id="6f1c2b8e-3d4a-4f5b-9c6d-7e8f9a0b1c2d",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `policy_id` but received ''"):
            await async_client.billing.spend_policies.with_raw_response.get(
                policy_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
