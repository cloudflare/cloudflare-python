# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.addresses.prefixes.bgps import (
    StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse,
    StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addresses.prefixes.bgps import (
    status_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status_params,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatuses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_address_management_dynamic_advertisement_get_advertisement_status(
        self, client: Cloudflare
    ) -> None:
        status = client.addresses.prefixes.bgps.statuses.ip_address_management_dynamic_advertisement_get_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse, status, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_address_management_dynamic_advertisement_get_advertisement_status(
        self, client: Cloudflare
    ) -> None:
        response = client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_get_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(
            StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse, status, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_address_management_dynamic_advertisement_get_advertisement_status(
        self, client: Cloudflare
    ) -> None:
        with client.addresses.prefixes.bgps.statuses.with_streaming_response.ip_address_management_dynamic_advertisement_get_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(
                StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse, status, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_ip_address_management_dynamic_advertisement_get_advertisement_status(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_get_advertisement_status(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_get_advertisement_status(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self, client: Cloudflare
    ) -> None:
        status = client.addresses.prefixes.bgps.statuses.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            advertised=True,
        )
        assert_matches_type(
            StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
            status,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self, client: Cloudflare
    ) -> None:
        response = client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            advertised=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(
            StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
            status,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self, client: Cloudflare
    ) -> None:
        with client.addresses.prefixes.bgps.statuses.with_streaming_response.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            advertised=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(
                StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
                status,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                advertised=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                advertised=True,
            )


class TestAsyncStatuses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_address_management_dynamic_advertisement_get_advertisement_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        status = await async_client.addresses.prefixes.bgps.statuses.ip_address_management_dynamic_advertisement_get_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse, status, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_address_management_dynamic_advertisement_get_advertisement_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_get_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(
            StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse, status, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_address_management_dynamic_advertisement_get_advertisement_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.addresses.prefixes.bgps.statuses.with_streaming_response.ip_address_management_dynamic_advertisement_get_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(
                StatusIPAddressManagementDynamicAdvertisementGetAdvertisementStatusResponse, status, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_ip_address_management_dynamic_advertisement_get_advertisement_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_get_advertisement_status(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_get_advertisement_status(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        status = await async_client.addresses.prefixes.bgps.statuses.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            advertised=True,
        )
        assert_matches_type(
            StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
            status,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            advertised=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(
            StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
            status,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.addresses.prefixes.bgps.statuses.with_streaming_response.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            advertised=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(
                StatusIPAddressManagementDynamicAdvertisementUpdatePrefixDynamicAdvertisementStatusResponse,
                status,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                advertised=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addresses.prefixes.bgps.statuses.with_raw_response.ip_address_management_dynamic_advertisement_update_prefix_dynamic_advertisement_status(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                advertised=True,
            )
