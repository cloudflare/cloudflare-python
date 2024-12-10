# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.gateway import Location

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        location = client.zero_trust.gateway.locations.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        location = client.zero_trust.gateway.locations.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
            client_default=False,
            dns_destination_ips_id="0e4a32c6-6fb8-4858-9296-98f51631e8e6",
            ecs_support=False,
            endpoints={
                "doh": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                    "require_token": True,
                },
                "dot": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                },
                "ipv4": {"enabled": True},
                "ipv6": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                },
            },
            networks=[{"network": "192.0.2.1/32"}],
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.locations.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.locations.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(Optional[Location], location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.locations.with_raw_response.create(
                account_id="",
                name="Austin Office Location",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        location = client.zero_trust.gateway.locations.update(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        location = client.zero_trust.gateway.locations.update(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
            client_default=False,
            dns_destination_ips_id="0e4a32c6-6fb8-4858-9296-98f51631e8e6",
            ecs_support=False,
            endpoints={
                "doh": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                    "require_token": True,
                },
                "dot": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                },
                "ipv4": {"enabled": True},
                "ipv6": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                },
            },
            networks=[{"network": "192.0.2.1/32"}],
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.locations.with_raw_response.update(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.locations.with_streaming_response.update(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(Optional[Location], location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.locations.with_raw_response.update(
                location_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
                name="Austin Office Location",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location_id` but received ''"):
            client.zero_trust.gateway.locations.with_raw_response.update(
                location_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                name="Austin Office Location",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        location = client.zero_trust.gateway.locations.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[Location], location, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.locations.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(SyncSinglePage[Location], location, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.locations.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(SyncSinglePage[Location], location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.locations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        location = client.zero_trust.gateway.locations.delete(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(object, location, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.locations.with_raw_response.delete(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(object, location, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.locations.with_streaming_response.delete(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(object, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.locations.with_raw_response.delete(
                location_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location_id` but received ''"):
            client.zero_trust.gateway.locations.with_raw_response.delete(
                location_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        location = client.zero_trust.gateway.locations.get(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.locations.with_raw_response.get(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = response.parse()
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.locations.with_streaming_response.get(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = response.parse()
            assert_matches_type(Optional[Location], location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.locations.with_raw_response.get(
                location_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location_id` but received ''"):
            client.zero_trust.gateway.locations.with_raw_response.get(
                location_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncLocations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.zero_trust.gateway.locations.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.zero_trust.gateway.locations.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
            client_default=False,
            dns_destination_ips_id="0e4a32c6-6fb8-4858-9296-98f51631e8e6",
            ecs_support=False,
            endpoints={
                "doh": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                    "require_token": True,
                },
                "dot": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                },
                "ipv4": {"enabled": True},
                "ipv6": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                },
            },
            networks=[{"network": "192.0.2.1/32"}],
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.locations.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.locations.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(Optional[Location], location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.locations.with_raw_response.create(
                account_id="",
                name="Austin Office Location",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.zero_trust.gateway.locations.update(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.zero_trust.gateway.locations.update(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
            client_default=False,
            dns_destination_ips_id="0e4a32c6-6fb8-4858-9296-98f51631e8e6",
            ecs_support=False,
            endpoints={
                "doh": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                    "require_token": True,
                },
                "dot": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                },
                "ipv4": {"enabled": True},
                "ipv6": {
                    "enabled": True,
                    "networks": [{"network": "2001:85a3::/64"}],
                },
            },
            networks=[{"network": "192.0.2.1/32"}],
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.locations.with_raw_response.update(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.locations.with_streaming_response.update(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            name="Austin Office Location",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(Optional[Location], location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.locations.with_raw_response.update(
                location_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
                name="Austin Office Location",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location_id` but received ''"):
            await async_client.zero_trust.gateway.locations.with_raw_response.update(
                location_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                name="Austin Office Location",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.zero_trust.gateway.locations.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[Location], location, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.locations.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(AsyncSinglePage[Location], location, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.locations.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(AsyncSinglePage[Location], location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.locations.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.zero_trust.gateway.locations.delete(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(object, location, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.locations.with_raw_response.delete(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(object, location, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.locations.with_streaming_response.delete(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(object, location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.locations.with_raw_response.delete(
                location_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location_id` but received ''"):
            await async_client.zero_trust.gateway.locations.with_raw_response.delete(
                location_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        location = await async_client.zero_trust.gateway.locations.get(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.locations.with_raw_response.get(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        location = await response.parse()
        assert_matches_type(Optional[Location], location, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.locations.with_streaming_response.get(
            location_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            location = await response.parse()
            assert_matches_type(Optional[Location], location, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.locations.with_raw_response.get(
                location_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `location_id` but received ''"):
            await async_client.zero_trust.gateway.locations.with_raw_response.get(
                location_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
