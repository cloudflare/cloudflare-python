# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.gateways import (
    ListUpdateResponse,
    ListDeleteResponse,
    ListGetResponse,
    ListZeroTrustListsCreateZeroTrustListResponse,
    ListZeroTrustListsListZeroTrustListsResponse,
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
from cloudflare.types.gateways import list_update_params
from cloudflare.types.gateways import list_zero_trust_lists_create_zero_trust_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        list = client.gateways.lists.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
        )
        assert_matches_type(ListUpdateResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        list = client.gateways.lists.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            description="The serial numbers for administrators",
        )
        assert_matches_type(ListUpdateResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.gateways.lists.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(ListUpdateResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.gateways.lists.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(ListUpdateResponse, list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.gateways.lists.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                name="Admin Serial Numbers",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        list = client.gateways.lists.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ListDeleteResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.gateways.lists.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(ListDeleteResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.gateways.lists.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(ListDeleteResponse, list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.gateways.lists.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        list = client.gateways.lists.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ListGetResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.gateways.lists.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(ListGetResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.gateways.lists.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(ListGetResponse, list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.gateways.lists.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_lists_create_zero_trust_list(self, client: Cloudflare) -> None:
        list = client.gateways.lists.zero_trust_lists_create_zero_trust_list(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="SERIAL",
        )
        assert_matches_type(ListZeroTrustListsCreateZeroTrustListResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_lists_create_zero_trust_list_with_all_params(self, client: Cloudflare) -> None:
        list = client.gateways.lists.zero_trust_lists_create_zero_trust_list(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="SERIAL",
            description="The serial numbers for administrators",
            items=[{"value": "8GE8721REF"}, {"value": "8GE8721REF"}, {"value": "8GE8721REF"}],
        )
        assert_matches_type(ListZeroTrustListsCreateZeroTrustListResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_lists_create_zero_trust_list(self, client: Cloudflare) -> None:
        response = client.gateways.lists.with_raw_response.zero_trust_lists_create_zero_trust_list(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="SERIAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(ListZeroTrustListsCreateZeroTrustListResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_lists_create_zero_trust_list(self, client: Cloudflare) -> None:
        with client.gateways.lists.with_streaming_response.zero_trust_lists_create_zero_trust_list(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="SERIAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(ListZeroTrustListsCreateZeroTrustListResponse, list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_lists_list_zero_trust_lists(self, client: Cloudflare) -> None:
        list = client.gateways.lists.zero_trust_lists_list_zero_trust_lists(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ListZeroTrustListsListZeroTrustListsResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_lists_list_zero_trust_lists(self, client: Cloudflare) -> None:
        response = client.gateways.lists.with_raw_response.zero_trust_lists_list_zero_trust_lists(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(Optional[ListZeroTrustListsListZeroTrustListsResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_lists_list_zero_trust_lists(self, client: Cloudflare) -> None:
        with client.gateways.lists.with_streaming_response.zero_trust_lists_list_zero_trust_lists(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(Optional[ListZeroTrustListsListZeroTrustListsResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.gateways.lists.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
        )
        assert_matches_type(ListUpdateResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.gateways.lists.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            description="The serial numbers for administrators",
        )
        assert_matches_type(ListUpdateResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.lists.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(ListUpdateResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.lists.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(ListUpdateResponse, list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.gateways.lists.with_raw_response.update(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                name="Admin Serial Numbers",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.gateways.lists.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ListDeleteResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.lists.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(ListDeleteResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.lists.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(ListDeleteResponse, list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.gateways.lists.with_raw_response.delete(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.gateways.lists.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ListGetResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.lists.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(ListGetResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.lists.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(ListGetResponse, list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.gateways.lists.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_lists_create_zero_trust_list(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.gateways.lists.zero_trust_lists_create_zero_trust_list(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="SERIAL",
        )
        assert_matches_type(ListZeroTrustListsCreateZeroTrustListResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_lists_create_zero_trust_list_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        list = await async_client.gateways.lists.zero_trust_lists_create_zero_trust_list(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="SERIAL",
            description="The serial numbers for administrators",
            items=[{"value": "8GE8721REF"}, {"value": "8GE8721REF"}, {"value": "8GE8721REF"}],
        )
        assert_matches_type(ListZeroTrustListsCreateZeroTrustListResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_lists_create_zero_trust_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.lists.with_raw_response.zero_trust_lists_create_zero_trust_list(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="SERIAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(ListZeroTrustListsCreateZeroTrustListResponse, list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_lists_create_zero_trust_list(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.lists.with_streaming_response.zero_trust_lists_create_zero_trust_list(
            "699d98642c564d2e855e9661899b7252",
            name="Admin Serial Numbers",
            type="SERIAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(ListZeroTrustListsCreateZeroTrustListResponse, list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_lists_list_zero_trust_lists(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.gateways.lists.zero_trust_lists_list_zero_trust_lists(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ListZeroTrustListsListZeroTrustListsResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_lists_list_zero_trust_lists(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.lists.with_raw_response.zero_trust_lists_list_zero_trust_lists(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(Optional[ListZeroTrustListsListZeroTrustListsResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_lists_list_zero_trust_lists(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.lists.with_streaming_response.zero_trust_lists_list_zero_trust_lists(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(Optional[ListZeroTrustListsListZeroTrustListsResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True
