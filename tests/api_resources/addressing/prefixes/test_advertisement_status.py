# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addressing.prefixes import (
    AdvertisementStatusGetResponse,
    AdvertisementStatusEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdvertisementStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        advertisement_status = client.addressing.prefixes.advertisement_status.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            advertised=True,
        )
        assert_matches_type(Optional[AdvertisementStatusEditResponse], advertisement_status, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.advertisement_status.with_raw_response.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            advertised=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advertisement_status = response.parse()
        assert_matches_type(Optional[AdvertisementStatusEditResponse], advertisement_status, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.advertisement_status.with_streaming_response.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            advertised=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advertisement_status = response.parse()
            assert_matches_type(Optional[AdvertisementStatusEditResponse], advertisement_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.advertisement_status.with_raw_response.edit(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
                advertised=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.advertisement_status.with_raw_response.edit(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                advertised=True,
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        advertisement_status = client.addressing.prefixes.advertisement_status.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[AdvertisementStatusGetResponse], advertisement_status, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.advertisement_status.with_raw_response.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advertisement_status = response.parse()
        assert_matches_type(Optional[AdvertisementStatusGetResponse], advertisement_status, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.advertisement_status.with_streaming_response.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advertisement_status = response.parse()
            assert_matches_type(Optional[AdvertisementStatusGetResponse], advertisement_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.advertisement_status.with_raw_response.get(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.advertisement_status.with_raw_response.get(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )


class TestAsyncAdvertisementStatus:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        advertisement_status = await async_client.addressing.prefixes.advertisement_status.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            advertised=True,
        )
        assert_matches_type(Optional[AdvertisementStatusEditResponse], advertisement_status, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.advertisement_status.with_raw_response.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            advertised=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advertisement_status = await response.parse()
        assert_matches_type(Optional[AdvertisementStatusEditResponse], advertisement_status, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.advertisement_status.with_streaming_response.edit(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            advertised=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advertisement_status = await response.parse()
            assert_matches_type(Optional[AdvertisementStatusEditResponse], advertisement_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.advertisement_status.with_raw_response.edit(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
                advertised=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.advertisement_status.with_raw_response.edit(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                advertised=True,
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        advertisement_status = await async_client.addressing.prefixes.advertisement_status.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[AdvertisementStatusGetResponse], advertisement_status, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.advertisement_status.with_raw_response.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advertisement_status = await response.parse()
        assert_matches_type(Optional[AdvertisementStatusGetResponse], advertisement_status, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.advertisement_status.with_streaming_response.get(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advertisement_status = await response.parse()
            assert_matches_type(Optional[AdvertisementStatusGetResponse], advertisement_status, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.advertisement_status.with_raw_response.get(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.advertisement_status.with_raw_response.get(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )
