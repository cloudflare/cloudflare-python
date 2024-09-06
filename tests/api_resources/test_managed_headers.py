# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.managed_headers import ManagedHeaderListResponse, ManagedHeaderEditResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.managed_headers import managed_header_edit_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManagedHeaders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        managed_header = client.managed_headers.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ManagedHeaderListResponse, managed_header, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.managed_headers.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_header = response.parse()
        assert_matches_type(ManagedHeaderListResponse, managed_header, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.managed_headers.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_header = response.parse()
            assert_matches_type(ManagedHeaderListResponse, managed_header, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.managed_headers.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        managed_header = client.managed_headers.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        )
        assert_matches_type(ManagedHeaderEditResponse, managed_header, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.managed_headers.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_header = response.parse()
        assert_matches_type(ManagedHeaderEditResponse, managed_header, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.managed_headers.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_header = response.parse()
            assert_matches_type(ManagedHeaderEditResponse, managed_header, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.managed_headers.with_raw_response.edit(
                zone_id="",
                managed_request_headers=[{}, {}, {}],
                managed_response_headers=[{}, {}, {}],
            )


class TestAsyncManagedHeaders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        managed_header = await async_client.managed_headers.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ManagedHeaderListResponse, managed_header, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.managed_headers.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_header = await response.parse()
        assert_matches_type(ManagedHeaderListResponse, managed_header, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.managed_headers.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_header = await response.parse()
            assert_matches_type(ManagedHeaderListResponse, managed_header, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.managed_headers.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        managed_header = await async_client.managed_headers.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        )
        assert_matches_type(ManagedHeaderEditResponse, managed_header, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.managed_headers.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_header = await response.parse()
        assert_matches_type(ManagedHeaderEditResponse, managed_header, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.managed_headers.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_header = await response.parse()
            assert_matches_type(ManagedHeaderEditResponse, managed_header, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.managed_headers.with_raw_response.edit(
                zone_id="",
                managed_request_headers=[{}, {}, {}],
                managed_response_headers=[{}, {}, {}],
            )
