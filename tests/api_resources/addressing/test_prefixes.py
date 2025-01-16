# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.addressing import Prefix, PrefixDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrefixes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        )
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.with_raw_response.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.with_streaming_response.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(Optional[Prefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.with_raw_response.create(
                account_id="",
                asn=209242,
                cidr="192.0.2.0/24",
                loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(SyncSinglePage[Prefix], prefix, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.with_raw_response.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(SyncSinglePage[Prefix], prefix, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.with_streaming_response.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(SyncSinglePage[Prefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.delete(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(PrefixDeleteResponse, prefix, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.with_raw_response.delete(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(PrefixDeleteResponse, prefix, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.with_streaming_response.delete(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(PrefixDeleteResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.with_raw_response.delete(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.with_raw_response.delete(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            description="Internal test prefix",
        )
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.with_raw_response.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            description="Internal test prefix",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.with_streaming_response.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            description="Internal test prefix",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(Optional[Prefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.with_raw_response.edit(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
                description="Internal test prefix",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.with_raw_response.edit(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                description="Internal test prefix",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.with_raw_response.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.with_streaming_response.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(Optional[Prefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.with_raw_response.get(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.with_raw_response.get(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )


class TestAsyncPrefixes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        )
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.with_raw_response.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.with_streaming_response.create(
            account_id="258def64c72dae45f3e4c8516e2111f2",
            asn=209242,
            cidr="192.0.2.0/24",
            loa_document_id="d933b1530bc56c9953cf8ce166da8004",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(Optional[Prefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.with_raw_response.create(
                account_id="",
                asn=209242,
                cidr="192.0.2.0/24",
                loa_document_id="d933b1530bc56c9953cf8ce166da8004",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(AsyncSinglePage[Prefix], prefix, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.with_raw_response.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(AsyncSinglePage[Prefix], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.with_streaming_response.list(
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(AsyncSinglePage[Prefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.delete(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(PrefixDeleteResponse, prefix, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.with_raw_response.delete(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(PrefixDeleteResponse, prefix, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.with_streaming_response.delete(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(PrefixDeleteResponse, prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.with_raw_response.delete(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.with_raw_response.delete(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            description="Internal test prefix",
        )
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.with_raw_response.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            description="Internal test prefix",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.with_streaming_response.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            description="Internal test prefix",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(Optional[Prefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.with_raw_response.edit(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
                description="Internal test prefix",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.with_raw_response.edit(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                description="Internal test prefix",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.with_raw_response.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(Optional[Prefix], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.with_streaming_response.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(Optional[Prefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.with_raw_response.get(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.with_raw_response.get(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )
