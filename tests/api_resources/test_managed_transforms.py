# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.managed_transforms import (
    ManagedTransformEditResponse,
    ManagedTransformListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManagedTransforms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        managed_transform = client.managed_transforms.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.managed_transforms.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = response.parse()
        assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.managed_transforms.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = response.parse()
            assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.managed_transforms.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        managed_transform = client.managed_transforms.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        )
        assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.managed_transforms.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = response.parse()
        assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.managed_transforms.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = response.parse()
            assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.managed_transforms.with_raw_response.edit(
                zone_id="",
                managed_request_headers=[{}, {}, {}],
                managed_response_headers=[{}, {}, {}],
            )


class TestAsyncManagedTransforms:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        managed_transform = await async_client.managed_transforms.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.managed_transforms.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = await response.parse()
        assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.managed_transforms.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = await response.parse()
            assert_matches_type(ManagedTransformListResponse, managed_transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.managed_transforms.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        managed_transform = await async_client.managed_transforms.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        )
        assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.managed_transforms.with_raw_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        managed_transform = await response.parse()
        assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.managed_transforms.with_streaming_response.edit(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            managed_request_headers=[{}, {}, {}],
            managed_response_headers=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            managed_transform = await response.parse()
            assert_matches_type(ManagedTransformEditResponse, managed_transform, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.managed_transforms.with_raw_response.edit(
                zone_id="",
                managed_request_headers=[{}, {}, {}],
                managed_response_headers=[{}, {}, {}],
            )
