# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.user import SubscriptionUpdateResponse, SubscriptionDeleteResponse, SubscriptionEditResponse, SubscriptionGetResponse

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.user import subscription_update_params
from cloudflare.types.user import subscription_edit_params
from cloudflare.types.user import RatePlan
from cloudflare.types.user import SubscriptionZone
from cloudflare.types.user import RatePlan
from cloudflare.types.user import SubscriptionZone

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        subscription = client.user.subscriptions.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=['response'])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        subscription = client.user.subscriptions.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={
                "install_id": "install_id"
            },
            component_values=[{
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }, {
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }, {
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }],
            frequency="weekly",
            rate_plan={
                "id": "free",
                "currency": "USD",
                "externally_managed": False,
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:

        response = client.user.subscriptions.with_raw_response.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subscription = response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.user.subscriptions.with_streaming_response.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subscription = response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          client.user.subscriptions.with_raw_response.update(
              identifier="",
          )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        subscription = client.user.subscriptions.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        response = client.user.subscriptions.with_raw_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subscription = response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.user.subscriptions.with_streaming_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subscription = response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          client.user.subscriptions.with_raw_response.delete(
              "",
          )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        subscription = client.user.subscriptions.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionEditResponse, subscription, path=['response'])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        subscription = client.user.subscriptions.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={
                "install_id": "install_id"
            },
            component_values=[{
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }, {
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }, {
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }],
            frequency="weekly",
            rate_plan={
                "id": "free",
                "currency": "USD",
                "externally_managed": False,
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionEditResponse, subscription, path=['response'])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:

        response = client.user.subscriptions.with_raw_response.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subscription = response.parse()
        assert_matches_type(SubscriptionEditResponse, subscription, path=['response'])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.user.subscriptions.with_streaming_response.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subscription = response.parse()
            assert_matches_type(SubscriptionEditResponse, subscription, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          client.user.subscriptions.with_raw_response.edit(
              identifier="",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        subscription = client.user.subscriptions.get()
        assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.user.subscriptions.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subscription = response.parse()
        assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.user.subscriptions.with_streaming_response.get() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subscription = response.parse()
            assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.user.subscriptions.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=['response'])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.user.subscriptions.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={
                "install_id": "install_id"
            },
            component_values=[{
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }, {
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }, {
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }],
            frequency="weekly",
            rate_plan={
                "id": "free",
                "currency": "USD",
                "externally_managed": False,
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.user.subscriptions.with_raw_response.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subscription = await response.parse()
        assert_matches_type(SubscriptionUpdateResponse, subscription, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.subscriptions.with_streaming_response.update(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subscription = await response.parse()
            assert_matches_type(SubscriptionUpdateResponse, subscription, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          await async_client.user.subscriptions.with_raw_response.update(
              identifier="",
          )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.user.subscriptions.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.user.subscriptions.with_raw_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subscription = await response.parse()
        assert_matches_type(SubscriptionDeleteResponse, subscription, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.subscriptions.with_streaming_response.delete(
            "506e3185e9c882d175a2d0cb0093d9f2",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subscription = await response.parse()
            assert_matches_type(SubscriptionDeleteResponse, subscription, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          await async_client.user.subscriptions.with_raw_response.delete(
              "",
          )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.user.subscriptions.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )
        assert_matches_type(SubscriptionEditResponse, subscription, path=['response'])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.user.subscriptions.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
            app={
                "install_id": "install_id"
            },
            component_values=[{
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }, {
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }, {
                "default": 5,
                "name": "page_rules",
                "price": 5,
                "value": 20,
            }],
            frequency="weekly",
            rate_plan={
                "id": "free",
                "currency": "USD",
                "externally_managed": False,
                "is_contract": False,
                "public_name": "Business Plan",
                "scope": "zone",
                "sets": ["string", "string", "string"],
            },
            zone={},
        )
        assert_matches_type(SubscriptionEditResponse, subscription, path=['response'])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.user.subscriptions.with_raw_response.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subscription = await response.parse()
        assert_matches_type(SubscriptionEditResponse, subscription, path=['response'])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.subscriptions.with_streaming_response.edit(
            identifier="506e3185e9c882d175a2d0cb0093d9f2",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subscription = await response.parse()
            assert_matches_type(SubscriptionEditResponse, subscription, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
          await async_client.user.subscriptions.with_raw_response.edit(
              identifier="",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        subscription = await async_client.user.subscriptions.get()
        assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.user.subscriptions.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        subscription = await response.parse()
        assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.subscriptions.with_streaming_response.get() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            subscription = await response.parse()
            assert_matches_type(Optional[SubscriptionGetResponse], subscription, path=['response'])

        assert cast(Any, response.is_closed) is True