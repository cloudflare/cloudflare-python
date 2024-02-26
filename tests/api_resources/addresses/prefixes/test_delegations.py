# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addresses.prefixes import (
    DelegationListResponse,
    DelegationCreateResponse,
    DelegationDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDelegations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        delegation = client.addresses.prefixes.delegations.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            delegated_account_id="b1946ac92492d2347c6235b4d2611184",
        )
        assert_matches_type(DelegationCreateResponse, delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.addresses.prefixes.delegations.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            delegated_account_id="b1946ac92492d2347c6235b4d2611184",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegation = response.parse()
        assert_matches_type(DelegationCreateResponse, delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.addresses.prefixes.delegations.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            delegated_account_id="b1946ac92492d2347c6235b4d2611184",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegation = response.parse()
            assert_matches_type(DelegationCreateResponse, delegation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addresses.prefixes.delegations.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                cidr="192.0.2.0/24",
                delegated_account_id="b1946ac92492d2347c6235b4d2611184",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addresses.prefixes.delegations.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                cidr="192.0.2.0/24",
                delegated_account_id="b1946ac92492d2347c6235b4d2611184",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        delegation = client.addresses.prefixes.delegations.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DelegationListResponse], delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addresses.prefixes.delegations.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegation = response.parse()
        assert_matches_type(Optional[DelegationListResponse], delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addresses.prefixes.delegations.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegation = response.parse()
            assert_matches_type(Optional[DelegationListResponse], delegation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addresses.prefixes.delegations.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addresses.prefixes.delegations.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        delegation = client.addresses.prefixes.delegations.delete(
            "d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DelegationDeleteResponse, delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addresses.prefixes.delegations.with_raw_response.delete(
            "d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegation = response.parse()
        assert_matches_type(DelegationDeleteResponse, delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addresses.prefixes.delegations.with_streaming_response.delete(
            "d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegation = response.parse()
            assert_matches_type(DelegationDeleteResponse, delegation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addresses.prefixes.delegations.with_raw_response.delete(
                "d933b1530bc56c9953cf8ce166da8004",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addresses.prefixes.delegations.with_raw_response.delete(
                "d933b1530bc56c9953cf8ce166da8004",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delegation_id` but received ''"):
            client.addresses.prefixes.delegations.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDelegations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        delegation = await async_client.addresses.prefixes.delegations.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            delegated_account_id="b1946ac92492d2347c6235b4d2611184",
        )
        assert_matches_type(DelegationCreateResponse, delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.prefixes.delegations.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            delegated_account_id="b1946ac92492d2347c6235b4d2611184",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegation = await response.parse()
        assert_matches_type(DelegationCreateResponse, delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.prefixes.delegations.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cidr="192.0.2.0/24",
            delegated_account_id="b1946ac92492d2347c6235b4d2611184",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegation = await response.parse()
            assert_matches_type(DelegationCreateResponse, delegation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addresses.prefixes.delegations.with_raw_response.create(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                cidr="192.0.2.0/24",
                delegated_account_id="b1946ac92492d2347c6235b4d2611184",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addresses.prefixes.delegations.with_raw_response.create(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                cidr="192.0.2.0/24",
                delegated_account_id="b1946ac92492d2347c6235b4d2611184",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        delegation = await async_client.addresses.prefixes.delegations.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[DelegationListResponse], delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.prefixes.delegations.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegation = await response.parse()
        assert_matches_type(Optional[DelegationListResponse], delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.prefixes.delegations.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegation = await response.parse()
            assert_matches_type(Optional[DelegationListResponse], delegation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addresses.prefixes.delegations.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addresses.prefixes.delegations.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        delegation = await async_client.addresses.prefixes.delegations.delete(
            "d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DelegationDeleteResponse, delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addresses.prefixes.delegations.with_raw_response.delete(
            "d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delegation = await response.parse()
        assert_matches_type(DelegationDeleteResponse, delegation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addresses.prefixes.delegations.with_streaming_response.delete(
            "d933b1530bc56c9953cf8ce166da8004",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delegation = await response.parse()
            assert_matches_type(DelegationDeleteResponse, delegation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addresses.prefixes.delegations.with_raw_response.delete(
                "d933b1530bc56c9953cf8ce166da8004",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addresses.prefixes.delegations.with_raw_response.delete(
                "d933b1530bc56c9953cf8ce166da8004",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delegation_id` but received ''"):
            await async_client.addresses.prefixes.delegations.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
