# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addressing.address_maps import IPDeleteResponse, IPUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ip = client.addressing.address_maps.ips.update(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            body={},
        )
        assert_matches_type(IPUpdateResponse, ip, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.ips.with_raw_response.update(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert_matches_type(IPUpdateResponse, ip, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.ips.with_streaming_response.update(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert_matches_type(IPUpdateResponse, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.ips.with_raw_response.update(
                ip_address="192.0.2.1",
                account_id="",
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.ips.with_raw_response.update(
                ip_address="192.0.2.1",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                address_map_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            client.addressing.address_maps.ips.with_raw_response.update(
                ip_address="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                body={},
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ip = client.addressing.address_maps.ips.delete(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
        )
        assert_matches_type(IPDeleteResponse, ip, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addressing.address_maps.ips.with_raw_response.delete(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = response.parse()
        assert_matches_type(IPDeleteResponse, ip, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addressing.address_maps.ips.with_streaming_response.delete(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = response.parse()
            assert_matches_type(IPDeleteResponse, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.address_maps.ips.with_raw_response.delete(
                ip_address="192.0.2.1",
                account_id="",
                address_map_id="055817b111884e0227e1be16a0be6ee0",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            client.addressing.address_maps.ips.with_raw_response.delete(
                ip_address="192.0.2.1",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                address_map_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            client.addressing.address_maps.ips.with_raw_response.delete(
                ip_address="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                address_map_id="055817b111884e0227e1be16a0be6ee0",
            )


class TestAsyncIPs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.addressing.address_maps.ips.update(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            body={},
        )
        assert_matches_type(IPUpdateResponse, ip, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.ips.with_raw_response.update(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert_matches_type(IPUpdateResponse, ip, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.ips.with_streaming_response.update(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert_matches_type(IPUpdateResponse, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.ips.with_raw_response.update(
                ip_address="192.0.2.1",
                account_id="",
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.ips.with_raw_response.update(
                ip_address="192.0.2.1",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                address_map_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            await async_client.addressing.address_maps.ips.with_raw_response.update(
                ip_address="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                address_map_id="055817b111884e0227e1be16a0be6ee0",
                body={},
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ip = await async_client.addressing.address_maps.ips.delete(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
        )
        assert_matches_type(IPDeleteResponse, ip, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.address_maps.ips.with_raw_response.delete(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ip = await response.parse()
        assert_matches_type(IPDeleteResponse, ip, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.address_maps.ips.with_streaming_response.delete(
            ip_address="192.0.2.1",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            address_map_id="055817b111884e0227e1be16a0be6ee0",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ip = await response.parse()
            assert_matches_type(IPDeleteResponse, ip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.address_maps.ips.with_raw_response.delete(
                ip_address="192.0.2.1",
                account_id="",
                address_map_id="055817b111884e0227e1be16a0be6ee0",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address_map_id` but received ''"):
            await async_client.addressing.address_maps.ips.with_raw_response.delete(
                ip_address="192.0.2.1",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                address_map_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_address` but received ''"):
            await async_client.addressing.address_maps.ips.with_raw_response.delete(
                ip_address="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                address_map_id="055817b111884e0227e1be16a0be6ee0",
            )
