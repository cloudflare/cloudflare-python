# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_cloud_networking.on_ramps import (
    AddressSpaceEditResponse,
    AddressSpaceListResponse,
    AddressSpaceUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddressSpaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        address_space = client.magic_cloud_networking.on_ramps.address_spaces.update(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        )
        assert_matches_type(AddressSpaceUpdateResponse, address_space, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.update(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_space = response.parse()
        assert_matches_type(AddressSpaceUpdateResponse, address_space, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.address_spaces.with_streaming_response.update(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_space = response.parse()
            assert_matches_type(AddressSpaceUpdateResponse, address_space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.update(
                account_id="",
                prefixes=["192.168.0.0/16"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        address_space = client.magic_cloud_networking.on_ramps.address_spaces.list(
            account_id="account_id",
        )
        assert_matches_type(AddressSpaceListResponse, address_space, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_space = response.parse()
        assert_matches_type(AddressSpaceListResponse, address_space, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.address_spaces.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_space = response.parse()
            assert_matches_type(AddressSpaceListResponse, address_space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        address_space = client.magic_cloud_networking.on_ramps.address_spaces.edit(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        )
        assert_matches_type(AddressSpaceEditResponse, address_space, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.edit(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_space = response.parse()
        assert_matches_type(AddressSpaceEditResponse, address_space, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_cloud_networking.on_ramps.address_spaces.with_streaming_response.edit(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_space = response.parse()
            assert_matches_type(AddressSpaceEditResponse, address_space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.edit(
                account_id="",
                prefixes=["192.168.0.0/16"],
            )


class TestAsyncAddressSpaces:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        address_space = await async_client.magic_cloud_networking.on_ramps.address_spaces.update(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        )
        assert_matches_type(AddressSpaceUpdateResponse, address_space, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.update(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_space = await response.parse()
        assert_matches_type(AddressSpaceUpdateResponse, address_space, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.address_spaces.with_streaming_response.update(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_space = await response.parse()
            assert_matches_type(AddressSpaceUpdateResponse, address_space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.update(
                account_id="",
                prefixes=["192.168.0.0/16"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        address_space = await async_client.magic_cloud_networking.on_ramps.address_spaces.list(
            account_id="account_id",
        )
        assert_matches_type(AddressSpaceListResponse, address_space, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_space = await response.parse()
        assert_matches_type(AddressSpaceListResponse, address_space, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.address_spaces.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_space = await response.parse()
            assert_matches_type(AddressSpaceListResponse, address_space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        address_space = await async_client.magic_cloud_networking.on_ramps.address_spaces.edit(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        )
        assert_matches_type(AddressSpaceEditResponse, address_space, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.edit(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_space = await response.parse()
        assert_matches_type(AddressSpaceEditResponse, address_space, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_cloud_networking.on_ramps.address_spaces.with_streaming_response.edit(
            account_id="account_id",
            prefixes=["192.168.0.0/16"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_space = await response.parse()
            assert_matches_type(AddressSpaceEditResponse, address_space, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_cloud_networking.on_ramps.address_spaces.with_raw_response.edit(
                account_id="",
                prefixes=["192.168.0.0/16"],
            )
