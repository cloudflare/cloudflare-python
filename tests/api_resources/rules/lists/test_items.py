# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.rules.lists import ItemCreateResponse, ItemUpdateResponse, ItemDeleteResponse, ItemGetResponse

from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rules.lists import item_create_params
from cloudflare.types.rules.lists import item_update_params
from cloudflare.types.rules.lists import item_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.create(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(Optional[ItemCreateResponse], item, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.create(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemCreateResponse], item, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.create(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemCreateResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.items.with_raw_response.create(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.create(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(Optional[ItemUpdateResponse], item, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemUpdateResponse], item, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemUpdateResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.items.with_raw_response.update(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.update(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.list(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncCursorPagination[object], item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.list(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="zzz",
            per_page=1,
            search="1.1.1.",
        )
        assert_matches_type(SyncCursorPagination[object], item, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.list(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(SyncCursorPagination[object], item, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.list(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(SyncCursorPagination[object], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.items.with_raw_response.list(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.list(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.items.with_raw_response.delete(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.delete(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        item = client.rules.lists.items.get(
            item_id="34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        )
        assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rules.lists.items.with_raw_response.get(
            item_id="34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rules.lists.items.with_streaming_response.get(
            item_id="34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.rules.lists.items.with_raw_response.get(
                item_id="34b12448945f11eaa1b71c4d701ab86e",
                account_identifier="",
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.items.with_raw_response.get(
                item_id="34b12448945f11eaa1b71c4d701ab86e",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.rules.lists.items.with_raw_response.get(
                item_id="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            )


class TestAsyncItems:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.create(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(Optional[ItemCreateResponse], item, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.create(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemCreateResponse], item, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.create(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemCreateResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.create(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.create(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(Optional[ItemUpdateResponse], item, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemUpdateResponse], item, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.update(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemUpdateResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.update(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.update(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.list(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncCursorPagination[object], item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.list(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="zzz",
            per_page=1,
            search="1.1.1.",
        )
        assert_matches_type(AsyncCursorPagination[object], item, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.list(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(AsyncCursorPagination[object], item, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.list(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(AsyncCursorPagination[object], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.list(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.list(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.delete(
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemDeleteResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.delete(
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.delete(
                list_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        item = await async_client.rules.lists.items.get(
            item_id="34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        )
        assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.items.with_raw_response.get(
            item_id="34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.items.with_streaming_response.get(
            item_id="34b12448945f11eaa1b71c4d701ab86e",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Optional[ItemGetResponse], item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.rules.lists.items.with_raw_response.get(
                item_id="34b12448945f11eaa1b71c4d701ab86e",
                account_identifier="",
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.get(
                item_id="34b12448945f11eaa1b71c4d701ab86e",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.rules.lists.items.with_raw_response.get(
                item_id="",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                list_id="2c0fc9fa937b11eaa1b71c4d701ab86e",
            )
