# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.rules import (
    ListGetResponse,
    ListListResponse,
    ListCreateResponse,
    ListDeleteResponse,
    ListUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        list = client.rules.lists.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        )
        assert_matches_type(Optional[ListCreateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        list = client.rules.lists.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
            description="This is a note",
        )
        assert_matches_type(Optional[ListCreateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(Optional[ListCreateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(Optional[ListCreateResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.create(
                "",
                kind="ip",
                name="list1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        list = client.rules.lists.update(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ListUpdateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        list = client.rules.lists.update(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is a note",
        )
        assert_matches_type(Optional[ListUpdateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.update(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(Optional[ListUpdateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.update(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(Optional[ListUpdateResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.update(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        list = client.rules.lists.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ListListResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(Optional[ListListResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(Optional[ListListResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        list = client.rules.lists.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ListDeleteResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(Optional[ListDeleteResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(Optional[ListDeleteResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.delete(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        list = client.rules.lists.get(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ListGetResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.rules.lists.with_raw_response.get(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = response.parse()
        assert_matches_type(Optional[ListGetResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.rules.lists.with_streaming_response.get(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = response.parse()
            assert_matches_type(Optional[ListGetResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.rules.lists.with_raw_response.get(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.rules.lists.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncLists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.rules.lists.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        )
        assert_matches_type(Optional[ListCreateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.rules.lists.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
            description="This is a note",
        )
        assert_matches_type(Optional[ListCreateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(Optional[ListCreateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            kind="ip",
            name="list1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(Optional[ListCreateResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.create(
                "",
                kind="ip",
                name="list1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.rules.lists.update(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ListUpdateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.rules.lists.update(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            description="This is a note",
        )
        assert_matches_type(Optional[ListUpdateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.update(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(Optional[ListUpdateResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.update(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(Optional[ListUpdateResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.update(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.rules.lists.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ListListResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(Optional[ListListResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(Optional[ListListResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.rules.lists.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ListDeleteResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(Optional[ListDeleteResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.delete(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(Optional[ListDeleteResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.delete(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        list = await async_client.rules.lists.get(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[ListGetResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.rules.lists.with_raw_response.get(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list = await response.parse()
        assert_matches_type(Optional[ListGetResponse], list, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.rules.lists.with_streaming_response.get(
            "2c0fc9fa937b11eaa1b71c4d701ab86e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list = await response.parse()
            assert_matches_type(Optional[ListGetResponse], list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.rules.lists.with_raw_response.get(
                "2c0fc9fa937b11eaa1b71c4d701ab86e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.rules.lists.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
