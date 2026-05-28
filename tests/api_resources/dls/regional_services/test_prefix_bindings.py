# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorPagination, AsyncCursorPagination
from cloudflare.types.dls.regional_services import (
    PrefixBindingGetResponse,
    PrefixBindingEditResponse,
    PrefixBindingListResponse,
    PrefixBindingCreateResponse,
    PrefixBindingDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrefixBindings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        prefix_binding = client.dls.regional_services.prefix_bindings.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="10.0.1.0/24",
            prefix_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            region_key="eu",
        )
        assert_matches_type(PrefixBindingCreateResponse, prefix_binding, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.dls.regional_services.prefix_bindings.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="10.0.1.0/24",
            prefix_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            region_key="eu",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = response.parse()
        assert_matches_type(PrefixBindingCreateResponse, prefix_binding, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.dls.regional_services.prefix_bindings.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="10.0.1.0/24",
            prefix_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            region_key="eu",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = response.parse()
            assert_matches_type(PrefixBindingCreateResponse, prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dls.regional_services.prefix_bindings.with_raw_response.create(
                account_id="",
                cidr="10.0.1.0/24",
                prefix_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                region_key="eu",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        prefix_binding = client.dls.regional_services.prefix_bindings.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncCursorPagination[PrefixBindingListResponse], prefix_binding, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        prefix_binding = client.dls.regional_services.prefix_bindings.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="cursor",
            per_page=1,
        )
        assert_matches_type(SyncCursorPagination[PrefixBindingListResponse], prefix_binding, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dls.regional_services.prefix_bindings.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = response.parse()
        assert_matches_type(SyncCursorPagination[PrefixBindingListResponse], prefix_binding, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dls.regional_services.prefix_bindings.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = response.parse()
            assert_matches_type(SyncCursorPagination[PrefixBindingListResponse], prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dls.regional_services.prefix_bindings.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        prefix_binding = client.dls.regional_services.prefix_bindings.delete(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PrefixBindingDeleteResponse, prefix_binding, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.dls.regional_services.prefix_bindings.with_raw_response.delete(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = response.parse()
        assert_matches_type(PrefixBindingDeleteResponse, prefix_binding, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.dls.regional_services.prefix_bindings.with_streaming_response.delete(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = response.parse()
            assert_matches_type(PrefixBindingDeleteResponse, prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dls.regional_services.prefix_bindings.with_raw_response.delete(
                binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            client.dls.regional_services.prefix_bindings.with_raw_response.delete(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        prefix_binding = client.dls.regional_services.prefix_bindings.edit(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="eu",
        )
        assert_matches_type(PrefixBindingEditResponse, prefix_binding, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.dls.regional_services.prefix_bindings.with_raw_response.edit(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="eu",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = response.parse()
        assert_matches_type(PrefixBindingEditResponse, prefix_binding, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.dls.regional_services.prefix_bindings.with_streaming_response.edit(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="eu",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = response.parse()
            assert_matches_type(PrefixBindingEditResponse, prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dls.regional_services.prefix_bindings.with_raw_response.edit(
                binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                account_id="",
                region_key="eu",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            client.dls.regional_services.prefix_bindings.with_raw_response.edit(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                region_key="eu",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        prefix_binding = client.dls.regional_services.prefix_bindings.get(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PrefixBindingGetResponse, prefix_binding, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.dls.regional_services.prefix_bindings.with_raw_response.get(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = response.parse()
        assert_matches_type(PrefixBindingGetResponse, prefix_binding, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.dls.regional_services.prefix_bindings.with_streaming_response.get(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = response.parse()
            assert_matches_type(PrefixBindingGetResponse, prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dls.regional_services.prefix_bindings.with_raw_response.get(
                binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            client.dls.regional_services.prefix_bindings.with_raw_response.get(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPrefixBindings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        prefix_binding = await async_client.dls.regional_services.prefix_bindings.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="10.0.1.0/24",
            prefix_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            region_key="eu",
        )
        assert_matches_type(PrefixBindingCreateResponse, prefix_binding, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dls.regional_services.prefix_bindings.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="10.0.1.0/24",
            prefix_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            region_key="eu",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = await response.parse()
        assert_matches_type(PrefixBindingCreateResponse, prefix_binding, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dls.regional_services.prefix_bindings.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="10.0.1.0/24",
            prefix_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            region_key="eu",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = await response.parse()
            assert_matches_type(PrefixBindingCreateResponse, prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dls.regional_services.prefix_bindings.with_raw_response.create(
                account_id="",
                cidr="10.0.1.0/24",
                prefix_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                region_key="eu",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        prefix_binding = await async_client.dls.regional_services.prefix_bindings.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncCursorPagination[PrefixBindingListResponse], prefix_binding, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        prefix_binding = await async_client.dls.regional_services.prefix_bindings.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="cursor",
            per_page=1,
        )
        assert_matches_type(AsyncCursorPagination[PrefixBindingListResponse], prefix_binding, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dls.regional_services.prefix_bindings.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = await response.parse()
        assert_matches_type(AsyncCursorPagination[PrefixBindingListResponse], prefix_binding, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dls.regional_services.prefix_bindings.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = await response.parse()
            assert_matches_type(AsyncCursorPagination[PrefixBindingListResponse], prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dls.regional_services.prefix_bindings.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        prefix_binding = await async_client.dls.regional_services.prefix_bindings.delete(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PrefixBindingDeleteResponse, prefix_binding, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dls.regional_services.prefix_bindings.with_raw_response.delete(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = await response.parse()
        assert_matches_type(PrefixBindingDeleteResponse, prefix_binding, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dls.regional_services.prefix_bindings.with_streaming_response.delete(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = await response.parse()
            assert_matches_type(PrefixBindingDeleteResponse, prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dls.regional_services.prefix_bindings.with_raw_response.delete(
                binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            await async_client.dls.regional_services.prefix_bindings.with_raw_response.delete(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        prefix_binding = await async_client.dls.regional_services.prefix_bindings.edit(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="eu",
        )
        assert_matches_type(PrefixBindingEditResponse, prefix_binding, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dls.regional_services.prefix_bindings.with_raw_response.edit(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="eu",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = await response.parse()
        assert_matches_type(PrefixBindingEditResponse, prefix_binding, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dls.regional_services.prefix_bindings.with_streaming_response.edit(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            region_key="eu",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = await response.parse()
            assert_matches_type(PrefixBindingEditResponse, prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dls.regional_services.prefix_bindings.with_raw_response.edit(
                binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                account_id="",
                region_key="eu",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            await async_client.dls.regional_services.prefix_bindings.with_raw_response.edit(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                region_key="eu",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        prefix_binding = await async_client.dls.regional_services.prefix_bindings.get(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PrefixBindingGetResponse, prefix_binding, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dls.regional_services.prefix_bindings.with_raw_response.get(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix_binding = await response.parse()
        assert_matches_type(PrefixBindingGetResponse, prefix_binding, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dls.regional_services.prefix_bindings.with_streaming_response.get(
            binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix_binding = await response.parse()
            assert_matches_type(PrefixBindingGetResponse, prefix_binding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dls.regional_services.prefix_bindings.with_raw_response.get(
                binding_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `binding_id` but received ''"):
            await async_client.dls.regional_services.prefix_bindings.with_raw_response.get(
                binding_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
