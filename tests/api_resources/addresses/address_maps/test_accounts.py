# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.addresses.address_maps import AccountUpdateResponse, AccountDeleteResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        account = client.addresses.address_maps.accounts.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AccountUpdateResponse], account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.accounts.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Optional[AccountUpdateResponse], account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.accounts.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Optional[AccountUpdateResponse], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier1` but received ''"):
            client.addresses.address_maps.accounts.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier1="",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            client.addresses.address_maps.accounts.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.accounts.with_raw_response.update(
                "",
                account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        account = client.addresses.address_maps.accounts.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AccountDeleteResponse], account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addresses.address_maps.accounts.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Optional[AccountDeleteResponse], account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addresses.address_maps.accounts.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Optional[AccountDeleteResponse], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier1` but received ''"):
            client.addresses.address_maps.accounts.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier1="",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            client.addresses.address_maps.accounts.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.address_maps.accounts.with_raw_response.delete(
                "",
                account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        account = await async_client.addresses.address_maps.accounts.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AccountUpdateResponse], account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.accounts.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Optional[AccountUpdateResponse], account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.accounts.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Optional[AccountUpdateResponse], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier1` but received ''"):
            await async_client.addresses.address_maps.accounts.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier1="",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            await async_client.addresses.address_maps.accounts.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.accounts.with_raw_response.update(
                "",
                account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        account = await async_client.addresses.address_maps.accounts.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AccountDeleteResponse], account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.address_maps.accounts.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(Optional[AccountDeleteResponse], account, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.address_maps.accounts.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
            address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Optional[AccountDeleteResponse], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier1` but received ''"):
            await async_client.addresses.address_maps.accounts.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier1="",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `address_map_identifier` but received ''"
        ):
            await async_client.addresses.address_maps.accounts.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.address_maps.accounts.with_raw_response.delete(
                "",
                account_identifier1="023e105f4ecef8ad9ca31a8372d0c353",
                address_map_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
