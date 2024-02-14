# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.addresses import (
    AddressMapCreateResponse,
    AddressMapUpdateResponse,
    AddressMapListResponse,
    AddressMapDeleteResponse,
    AddressMapGetResponse,
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
from cloudflare.types.addresses import address_map_create_params
from cloudflare.types.addresses import address_map_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddressMaps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        address_map = client.addresses.address_maps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressMapCreateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        address_map = client.addresses.address_maps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="My Ecommerce zones",
            enabled=True,
        )
        assert_matches_type(AddressMapCreateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(AddressMapCreateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(AddressMapCreateResponse, address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.with_raw_response.create(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        address_map = client.addresses.address_maps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressMapUpdateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        address_map = client.addresses.address_maps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            default_sni="*.example.com",
            description="My Ecommerce zones",
            enabled=True,
        )
        assert_matches_type(AddressMapUpdateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(AddressMapUpdateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(AddressMapUpdateResponse, address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            client.addresses.address_maps.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        address_map = client.addresses.address_maps.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapListResponse], address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMapListResponse], address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMapListResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        address_map = client.addresses.address_maps.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            client.addresses.address_maps.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        address_map = client.addresses.address_maps.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressMapGetResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = response.parse()
        assert_matches_type(AddressMapGetResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = response.parse()
            assert_matches_type(AddressMapGetResponse, address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            client.addresses.address_maps.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAddressMaps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addresses.address_maps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressMapCreateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addresses.address_maps.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            description="My Ecommerce zones",
            enabled=True,
        )
        assert_matches_type(AddressMapCreateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(AddressMapCreateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(AddressMapCreateResponse, address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.with_raw_response.create(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addresses.address_maps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressMapUpdateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addresses.address_maps.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            default_sni="*.example.com",
            description="My Ecommerce zones",
            enabled=True,
        )
        assert_matches_type(AddressMapUpdateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(AddressMapUpdateResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(AddressMapUpdateResponse, address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            await async_client.addresses.address_maps.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addresses.address_maps.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapListResponse], address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMapListResponse], address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMapListResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addresses.address_maps.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(Optional[AddressMapDeleteResponse], address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            await async_client.addresses.address_maps.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        address_map = await async_client.addresses.address_maps.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressMapGetResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address_map = await response.parse()
        assert_matches_type(AddressMapGetResponse, address_map, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address_map = await response.parse()
            assert_matches_type(AddressMapGetResponse, address_map, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            await async_client.addresses.address_maps.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
