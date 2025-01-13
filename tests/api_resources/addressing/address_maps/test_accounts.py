# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addressing.address_maps import AccountDeleteResponse, AccountUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        account = client.addressing.address_maps.accounts.update(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            body={},
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.accounts.with_raw_response.update(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.accounts.with_streaming_response.update(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.accounts.with_raw_response.update(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.accounts.with_raw_response.update(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                body={},
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        account = client.addressing.address_maps.accounts.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(AccountDeleteResponse, account, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.accounts.with_raw_response.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountDeleteResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.accounts.with_streaming_response.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountDeleteResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.accounts.with_raw_response.delete(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.accounts.with_raw_response.delete(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        account = await async_client.addressing.address_maps.accounts.update(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            body={},
        )
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.accounts.with_raw_response.update(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountUpdateResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.accounts.with_streaming_response.update(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountUpdateResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.accounts.with_raw_response.update(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.accounts.with_raw_response.update(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                body={},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        account = await async_client.addressing.address_maps.accounts.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(AccountDeleteResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.accounts.with_raw_response.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountDeleteResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.accounts.with_streaming_response.delete(
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountDeleteResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.accounts.with_raw_response.delete(
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.accounts.with_raw_response.delete(
                address_map_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )
