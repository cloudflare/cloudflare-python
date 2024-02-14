# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.rules.lists import (
    ItemDeleteResponse,
    ItemGetResponse,
    ItemListsCreateListItemsResponse,
    ItemListsGetListItemsResponse,
    ItemListsUpdateAllListItemsResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rules.lists import item_delete_params
from cloudflare.types.rules.lists import item_lists_create_list_items_params
from cloudflare.types.rules.lists import item_lists_get_list_items_params
from cloudflare.types.rules.lists import item_lists_update_all_list_items_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            items=[{"id": "34b12448945f11eaa1b71c4d701ab86e"}],
        )
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.items.with_raw_response.delete(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.get(
            "34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        )
        assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.get(
            "34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.get(
            "34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.rules.lists.items.with_raw_response.get(
                "34b12448945f11eaa1b71c4d701ab86e",
                account_identifier="",
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.get(
                "34b12448945f11eaa1b71c4d701ab86e",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.rules.lists.items.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_lists_create_list_items(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.lists_create_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(Optional[ItemListsCreateListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_lists_create_list_items(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.lists_create_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemListsCreateListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_lists_create_list_items(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.lists_create_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemListsCreateListItemsResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_lists_create_list_items(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.items.with_raw_response.lists_create_list_items(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.lists_create_list_items(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_lists_get_list_items(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.lists_get_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ItemListsGetListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_lists_get_list_items_with_all_params(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.lists_get_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="zzz",
            per_page=1,
            search="1.1.1.",
        )
        assert_matches_type(Optional[ItemListsGetListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_lists_get_list_items(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.lists_get_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemListsGetListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_lists_get_list_items(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.lists_get_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemListsGetListItemsResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_lists_get_list_items(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.items.with_raw_response.lists_get_list_items(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.lists_get_list_items(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_lists_update_all_list_items(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.lists_update_all_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(Optional[ItemListsUpdateAllListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_lists_update_all_list_items(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.lists_update_all_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemListsUpdateAllListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_lists_update_all_list_items(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.lists_update_all_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemListsUpdateAllListItemsResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_lists_update_all_list_items(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.items.with_raw_response.lists_update_all_list_items(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.lists_update_all_list_items(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            items=[{"id": "34b12448945f11eaa1b71c4d701ab86e"}],
        )
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.delete(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.get(
            "34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        )
        assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.get(
            "34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.get(
            "34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.rules.lists.items.with_raw_response.get(
                "34b12448945f11eaa1b71c4d701ab86e",
                account_identifier="",
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.get(
                "34b12448945f11eaa1b71c4d701ab86e",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_lists_create_list_items(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.lists_create_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(Optional[ItemListsCreateListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_lists_create_list_items(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.lists_create_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemListsCreateListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_lists_create_list_items(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.lists_create_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemListsCreateListItemsResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_lists_create_list_items(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.lists_create_list_items(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.lists_create_list_items(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_lists_get_list_items(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.lists_get_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ItemListsGetListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_lists_get_list_items_with_all_params(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.lists_get_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="zzz",
            per_page=1,
            search="1.1.1.",
        )
        assert_matches_type(Optional[ItemListsGetListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_lists_get_list_items(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.lists_get_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemListsGetListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_lists_get_list_items(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.lists_get_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemListsGetListItemsResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_lists_get_list_items(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.lists_get_list_items(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.lists_get_list_items(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_lists_update_all_list_items(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.lists_update_all_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(Optional[ItemListsUpdateAllListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_lists_update_all_list_items(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.lists_update_all_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemListsUpdateAllListItemsResponse], item, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_lists_update_all_list_items(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.lists_update_all_list_items(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemListsUpdateAllListItemsResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_lists_update_all_list_items(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.lists_update_all_list_items(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.lists_update_all_list_items(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )
