# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addresses import (
    PrefixGetResponse,
    PrefixDeleteResponse,
    PrefixUpdateResponse,
    PrefixIPAddressManagementPrefixesAddPrefixResponse,
    PrefixIPAddressManagementPrefixesListPrefixesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrefixes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        prefix = client.addresses.prefixes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="Internal test prefix",
        )
        assert_matches_type(PrefixUpdateResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.addresses.prefixes.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="Internal test prefix",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(PrefixUpdateResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.addresses.prefixes.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="Internal test prefix",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(PrefixUpdateResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.prefixes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                description="Internal test prefix",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            client.addresses.prefixes.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                description="Internal test prefix",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        prefix = client.addresses.prefixes.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PrefixDeleteResponse], prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addresses.prefixes.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(Optional[PrefixDeleteResponse], prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addresses.prefixes.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(Optional[PrefixDeleteResponse], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.prefixes.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            client.addresses.prefixes.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        prefix = client.addresses.prefixes.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PrefixGetResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addresses.prefixes.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(PrefixGetResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addresses.prefixes.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(PrefixGetResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.prefixes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            client.addresses.prefixes.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_address_management_prefixes_add_prefix(self, client: Cloudflare) -> None:
        prefix = client.addresses.prefixes.ip_address_management_prefixes_add_prefix(
            "023e105f4ecef8ad9ca31a8372d0c353",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        )
        assert_matches_type(PrefixIPAddressManagementPrefixesAddPrefixResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_address_management_prefixes_add_prefix(self, client: Cloudflare) -> None:
        response = client.addresses.prefixes.with_raw_response.ip_address_management_prefixes_add_prefix(
            "023e105f4ecef8ad9ca31a8372d0c353",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(PrefixIPAddressManagementPrefixesAddPrefixResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_address_management_prefixes_add_prefix(self, client: Cloudflare) -> None:
        with client.addresses.prefixes.with_streaming_response.ip_address_management_prefixes_add_prefix(
            "023e105f4ecef8ad9ca31a8372d0c353",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(PrefixIPAddressManagementPrefixesAddPrefixResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_ip_address_management_prefixes_add_prefix(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.prefixes.with_raw_response.ip_address_management_prefixes_add_prefix(
                "",
                asn=209242,
                cidr="192.0.2.0/24",
                loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_address_management_prefixes_list_prefixes(self, client: Cloudflare) -> None:
        prefix = client.addresses.prefixes.ip_address_management_prefixes_list_prefixes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse], prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_address_management_prefixes_list_prefixes(self, client: Cloudflare) -> None:
        response = client.addresses.prefixes.with_raw_response.ip_address_management_prefixes_list_prefixes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse], prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_address_management_prefixes_list_prefixes(self, client: Cloudflare) -> None:
        with client.addresses.prefixes.with_streaming_response.ip_address_management_prefixes_list_prefixes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(
                Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse], prefix, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_ip_address_management_prefixes_list_prefixes(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.prefixes.with_raw_response.ip_address_management_prefixes_list_prefixes(
                "",
            )


class TestAsyncPrefixes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addresses.prefixes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="Internal test prefix",
        )
        assert_matches_type(PrefixUpdateResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.prefixes.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="Internal test prefix",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(PrefixUpdateResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.prefixes.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            description="Internal test prefix",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(PrefixUpdateResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.prefixes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                description="Internal test prefix",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            await async_client.addresses.prefixes.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                description="Internal test prefix",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addresses.prefixes.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PrefixDeleteResponse], prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.prefixes.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(Optional[PrefixDeleteResponse], prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.prefixes.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(Optional[PrefixDeleteResponse], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.prefixes.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            await async_client.addresses.prefixes.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addresses.prefixes.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(PrefixGetResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.prefixes.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(PrefixGetResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.prefixes.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(PrefixGetResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.prefixes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_identifier` but received ''"):
            await async_client.addresses.prefixes.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_address_management_prefixes_add_prefix(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addresses.prefixes.ip_address_management_prefixes_add_prefix(
            "023e105f4ecef8ad9ca31a8372d0c353",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        )
        assert_matches_type(PrefixIPAddressManagementPrefixesAddPrefixResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_address_management_prefixes_add_prefix(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.prefixes.with_raw_response.ip_address_management_prefixes_add_prefix(
            "023e105f4ecef8ad9ca31a8372d0c353",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(PrefixIPAddressManagementPrefixesAddPrefixResponse, prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_address_management_prefixes_add_prefix(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.addresses.prefixes.with_streaming_response.ip_address_management_prefixes_add_prefix(
            "023e105f4ecef8ad9ca31a8372d0c353",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(PrefixIPAddressManagementPrefixesAddPrefixResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_ip_address_management_prefixes_add_prefix(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.prefixes.with_raw_response.ip_address_management_prefixes_add_prefix(
                "",
                asn=209242,
                cidr="192.0.2.0/24",
                loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_address_management_prefixes_list_prefixes(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addresses.prefixes.ip_address_management_prefixes_list_prefixes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse], prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_address_management_prefixes_list_prefixes(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.addresses.prefixes.with_raw_response.ip_address_management_prefixes_list_prefixes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse], prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_address_management_prefixes_list_prefixes(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.addresses.prefixes.with_streaming_response.ip_address_management_prefixes_list_prefixes(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(
                Optional[PrefixIPAddressManagementPrefixesListPrefixesResponse], prefix, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_ip_address_management_prefixes_list_prefixes(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.prefixes.with_raw_response.ip_address_management_prefixes_list_prefixes(
                "",
            )
