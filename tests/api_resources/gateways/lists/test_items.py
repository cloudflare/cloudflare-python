# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.gateways.lists import ItemZeroTrustListsZeroTrustListItemsResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_lists_zero_trust_list_items(self, client: Cloudflare) -> None:
        item = client.gateways.lists.items.zero_trust_lists_zero_trust_list_items(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ItemZeroTrustListsZeroTrustListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_lists_zero_trust_list_items(self, client: Cloudflare) -> None:
        response = client.gateways.lists.items.with_raw_response.zero_trust_lists_zero_trust_list_items(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemZeroTrustListsZeroTrustListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_lists_zero_trust_list_items(self, client: Cloudflare) -> None:
        with client.gateways.lists.items.with_streaming_response.zero_trust_lists_zero_trust_list_items(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemZeroTrustListsZeroTrustListItemsResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zero_trust_lists_zero_trust_list_items(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.gateways.lists.items.with_raw_response.zero_trust_lists_zero_trust_list_items(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_lists_zero_trust_list_items(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.gateways.lists.items.zero_trust_lists_zero_trust_list_items(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ItemZeroTrustListsZeroTrustListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_lists_zero_trust_list_items(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.lists.items.with_raw_response.zero_trust_lists_zero_trust_list_items(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemZeroTrustListsZeroTrustListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_lists_zero_trust_list_items(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.lists.items.with_streaming_response.zero_trust_lists_zero_trust_list_items(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemZeroTrustListsZeroTrustListItemsResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zero_trust_lists_zero_trust_list_items(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.gateways.lists.items.with_raw_response.zero_trust_lists_zero_trust_list_items(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )
