# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.user import Subscription
from cloudflare.types.zones import SubscriptionGetResponse, SubscriptionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        subscription = client.zones.subscriptions.create(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        subscription = client.zones.subscriptions.create(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "install_id"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zones.subscriptions.with_raw_response.create(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zones.subscriptions.with_streaming_response.create(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.zones.subscriptions.with_raw_response.create(
                identifier="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        subscription = client.zones.subscriptions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[Subscription], subscription, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zones.subscriptions.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncSinglePage[Subscription], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zones.subscriptions.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncSinglePage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zones.subscriptions.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        subscription = client.zones.subscriptions.get(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zones.subscriptions.with_raw_response.get(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.subscriptions.with_streaming_response.get(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.zones.subscriptions.with_raw_response.get(
                "",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.zones.subscriptions.create(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.zones.subscriptions.create(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "install_id"},
            component_values=[
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
                {
                    "default": 5,
                    "name": "page_rules",
                    "price": 5,
                    "value": 20,
                },
            ],
            frequency="monthly",
            rate_plan={
                "currency": "USD",
                "externally_managed": False,
                "id": "free",
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.subscriptions.with_raw_response.create(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.subscriptions.with_streaming_response.create(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionCreateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.zones.subscriptions.with_raw_response.create(
                identifier="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.zones.subscriptions.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.subscriptions.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(AsyncSinglePage[Subscription], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.subscriptions.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncSinglePage[Subscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zones.subscriptions.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.zones.subscriptions.get(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.subscriptions.with_raw_response.get(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.subscriptions.with_streaming_response.get(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionGetResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.zones.subscriptions.with_raw_response.get(
                "",
            )
