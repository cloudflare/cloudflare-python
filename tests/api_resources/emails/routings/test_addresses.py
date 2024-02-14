# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.emails.routings import (
    AddressGetResponse,
    AddressDeleteResponse,
    AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse,
    AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAddresses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        address = client.emails.routings.addresses.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.emails.routings.addresses.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.emails.routings.addresses.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressDeleteResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.emails.routings.addresses.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `destination_address_identifier` but received ''"
        ):
            client.emails.routings.addresses.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_destination_addresses_create_a_destination_address(self, client: Cloudflare) -> None:
        address = client.emails.routings.addresses.email_routing_destination_addresses_create_a_destination_address(
            "023e105f4ecef8ad9ca31a8372d0c353",
            email="user@example.com",
        )
        assert_matches_type(
            AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse, address, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_email_routing_destination_addresses_create_a_destination_address(
        self, client: Cloudflare
    ) -> None:
        response = client.emails.routings.addresses.with_raw_response.email_routing_destination_addresses_create_a_destination_address(
            "023e105f4ecef8ad9ca31a8372d0c353",
            email="user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(
            AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse, address, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_email_routing_destination_addresses_create_a_destination_address(
        self, client: Cloudflare
    ) -> None:
        with client.emails.routings.addresses.with_streaming_response.email_routing_destination_addresses_create_a_destination_address(
            "023e105f4ecef8ad9ca31a8372d0c353",
            email="user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(
                AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse, address, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_email_routing_destination_addresses_create_a_destination_address(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.emails.routings.addresses.with_raw_response.email_routing_destination_addresses_create_a_destination_address(
                "",
                email="user@example.com",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_destination_addresses_list_destination_addresses(self, client: Cloudflare) -> None:
        address = client.emails.routings.addresses.email_routing_destination_addresses_list_destination_addresses(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
            address,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_email_routing_destination_addresses_list_destination_addresses_with_all_params(
        self, client: Cloudflare
    ) -> None:
        address = client.emails.routings.addresses.email_routing_destination_addresses_list_destination_addresses(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            page=1,
            per_page=5,
            verified=True,
        )
        assert_matches_type(
            Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
            address,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_email_routing_destination_addresses_list_destination_addresses(
        self, client: Cloudflare
    ) -> None:
        response = client.emails.routings.addresses.with_raw_response.email_routing_destination_addresses_list_destination_addresses(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(
            Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
            address,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_email_routing_destination_addresses_list_destination_addresses(
        self, client: Cloudflare
    ) -> None:
        with client.emails.routings.addresses.with_streaming_response.email_routing_destination_addresses_list_destination_addresses(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(
                Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
                address,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_email_routing_destination_addresses_list_destination_addresses(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.emails.routings.addresses.with_raw_response.email_routing_destination_addresses_list_destination_addresses(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        address = client.emails.routings.addresses.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressGetResponse, address, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.emails.routings.addresses.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = response.parse()
        assert_matches_type(AddressGetResponse, address, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.emails.routings.addresses.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = response.parse()
            assert_matches_type(AddressGetResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.emails.routings.addresses.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `destination_address_identifier` but received ''"
        ):
            client.emails.routings.addresses.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncAddresses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        address = await async_client.emails.routings.addresses.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.emails.routings.addresses.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressDeleteResponse, address, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.emails.routings.addresses.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressDeleteResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.emails.routings.addresses.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `destination_address_identifier` but received ''"
        ):
            await async_client.emails.routings.addresses.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_destination_addresses_create_a_destination_address(
        self, async_client: AsyncCloudflare
    ) -> None:
        address = await async_client.emails.routings.addresses.email_routing_destination_addresses_create_a_destination_address(
            "023e105f4ecef8ad9ca31a8372d0c353",
            email="user@example.com",
        )
        assert_matches_type(
            AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse, address, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_email_routing_destination_addresses_create_a_destination_address(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.emails.routings.addresses.with_raw_response.email_routing_destination_addresses_create_a_destination_address(
            "023e105f4ecef8ad9ca31a8372d0c353",
            email="user@example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(
            AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse, address, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_email_routing_destination_addresses_create_a_destination_address(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.emails.routings.addresses.with_streaming_response.email_routing_destination_addresses_create_a_destination_address(
            "023e105f4ecef8ad9ca31a8372d0c353",
            email="user@example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(
                AddressEmailRoutingDestinationAddressesCreateADestinationAddressResponse, address, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_email_routing_destination_addresses_create_a_destination_address(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.emails.routings.addresses.with_raw_response.email_routing_destination_addresses_create_a_destination_address(
                "",
                email="user@example.com",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_destination_addresses_list_destination_addresses(
        self, async_client: AsyncCloudflare
    ) -> None:
        address = (
            await async_client.emails.routings.addresses.email_routing_destination_addresses_list_destination_addresses(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )
        assert_matches_type(
            Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
            address,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_email_routing_destination_addresses_list_destination_addresses_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        address = (
            await async_client.emails.routings.addresses.email_routing_destination_addresses_list_destination_addresses(
                "023e105f4ecef8ad9ca31a8372d0c353",
                direction="asc",
                page=1,
                per_page=5,
                verified=True,
            )
        )
        assert_matches_type(
            Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
            address,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_email_routing_destination_addresses_list_destination_addresses(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.emails.routings.addresses.with_raw_response.email_routing_destination_addresses_list_destination_addresses(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(
            Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
            address,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_email_routing_destination_addresses_list_destination_addresses(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.emails.routings.addresses.with_streaming_response.email_routing_destination_addresses_list_destination_addresses(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(
                Optional[AddressEmailRoutingDestinationAddressesListDestinationAddressesResponse],
                address,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_email_routing_destination_addresses_list_destination_addresses(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.emails.routings.addresses.with_raw_response.email_routing_destination_addresses_list_destination_addresses(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        address = await async_client.emails.routings.addresses.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AddressGetResponse, address, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.emails.routings.addresses.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        address = await response.parse()
        assert_matches_type(AddressGetResponse, address, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.emails.routings.addresses.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            address = await response.parse()
            assert_matches_type(AddressGetResponse, address, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.emails.routings.addresses.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                account_identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `destination_address_identifier` but received ''"
        ):
            await async_client.emails.routings.addresses.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
