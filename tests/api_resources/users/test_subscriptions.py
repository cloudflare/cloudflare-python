# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.users import (
    SubscriptionUpdateResponse,
    SubscriptionDeleteResponse,
    SubscriptionUserSubscriptionGetUserSubscriptionsResponse,
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
from cloudflare.types.users import subscription_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        subscription = client.users.subscriptions.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        subscription = client.users.subscriptions.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "string"},
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
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.users.subscriptions.with_raw_response.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.users.subscriptions.with_streaming_response.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.subscriptions.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        subscription = client.users.subscriptions.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.users.subscriptions.with_raw_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.users.subscriptions.with_streaming_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.users.subscriptions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_subscription_get_user_subscriptions(self, client: Cloudflare) -> None:
        subscription = client.users.subscriptions.user_subscription_get_user_subscriptions()
        assert_matches_type(
            Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse], subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_subscription_get_user_subscriptions(self, client: Cloudflare) -> None:
        response = client.users.subscriptions.with_raw_response.user_subscription_get_user_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(
            Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse], subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_subscription_get_user_subscriptions(self, client: Cloudflare) -> None:
        with client.users.subscriptions.with_streaming_response.user_subscription_get_user_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(
                Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse], subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.users.subscriptions.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.users.subscriptions.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
            app={"install_id": "string"},
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
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.subscriptions.with_raw_response.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.subscriptions.with_streaming_response.update(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.subscriptions.with_raw_response.update(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.users.subscriptions.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.subscriptions.with_raw_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.subscriptions.with_streaming_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.users.subscriptions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_subscription_get_user_subscriptions(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.users.subscriptions.user_subscription_get_user_subscriptions()
        assert_matches_type(
            Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse], subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_subscription_get_user_subscriptions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.subscriptions.with_raw_response.user_subscription_get_user_subscriptions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(
            Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse], subscription, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_subscription_get_user_subscriptions(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.subscriptions.with_streaming_response.user_subscription_get_user_subscriptions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(
                Optional[SubscriptionUserSubscriptionGetUserSubscriptionsResponse], subscription, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
