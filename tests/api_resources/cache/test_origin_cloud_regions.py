# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.cache import (
    OriginCloudRegion,
    OriginCloudRegionDeleteResponse,
    OriginCloudRegionBulkDeleteResponse,
    OriginCloudRegionBulkUpdateResponse,
    OriginCloudRegionSupportedRegionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOriginCloudRegions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        origin_cloud_region = client.cache.origin_cloud_regions.update(
            path_origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body_origin_ip="192.0.2.1",
            region="us-east-1",
            vendor="aws",
        )
        assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.cache.origin_cloud_regions.with_raw_response.update(
            path_origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body_origin_ip="192.0.2.1",
            region="us-east-1",
            vendor="aws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = response.parse()
        assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.cache.origin_cloud_regions.with_streaming_response.update(
            path_origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body_origin_ip="192.0.2.1",
            region="us-east-1",
            vendor="aws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = response.parse()
            assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.update(
                path_origin_ip="192.0.2.1",
                zone_id="",
                body_origin_ip="192.0.2.1",
                region="us-east-1",
                vendor="aws",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_origin_ip` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.update(
                path_origin_ip="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body_origin_ip="192.0.2.1",
                region="us-east-1",
                vendor="aws",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        origin_cloud_region = client.cache.origin_cloud_regions.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        origin_cloud_region = client.cache.origin_cloud_regions.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cache.origin_cloud_regions.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cache.origin_cloud_regions.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[OriginCloudRegion], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        origin_cloud_region = client.cache.origin_cloud_regions.delete(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCloudRegionDeleteResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.cache.origin_cloud_regions.with_raw_response.delete(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = response.parse()
        assert_matches_type(Optional[OriginCloudRegionDeleteResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.cache.origin_cloud_regions.with_streaming_response.delete(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = response.parse()
            assert_matches_type(Optional[OriginCloudRegionDeleteResponse], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.delete(
                origin_ip="192.0.2.1",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `origin_ip` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.delete(
                origin_ip="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_bulk_delete(self, client: Cloudflare) -> None:
        origin_cloud_region = client.cache.origin_cloud_regions.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCloudRegionBulkDeleteResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_bulk_delete(self, client: Cloudflare) -> None:
        response = client.cache.origin_cloud_regions.with_raw_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = response.parse()
        assert_matches_type(Optional[OriginCloudRegionBulkDeleteResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_bulk_delete(self, client: Cloudflare) -> None:
        with client.cache.origin_cloud_regions.with_streaming_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = response.parse()
            assert_matches_type(Optional[OriginCloudRegionBulkDeleteResponse], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_bulk_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.bulk_delete(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_bulk_update(self, client: Cloudflare) -> None:
        origin_cloud_region = client.cache.origin_cloud_regions.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "origin_ip": "192.0.2.1",
                    "region": "us-east-1",
                    "vendor": "aws",
                },
                {
                    "origin_ip": "2001:db8::1",
                    "region": "us-central1",
                    "vendor": "gcp",
                },
            ],
        )
        assert_matches_type(Optional[OriginCloudRegionBulkUpdateResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_bulk_update(self, client: Cloudflare) -> None:
        response = client.cache.origin_cloud_regions.with_raw_response.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "origin_ip": "192.0.2.1",
                    "region": "us-east-1",
                    "vendor": "aws",
                },
                {
                    "origin_ip": "2001:db8::1",
                    "region": "us-central1",
                    "vendor": "gcp",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = response.parse()
        assert_matches_type(Optional[OriginCloudRegionBulkUpdateResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_bulk_update(self, client: Cloudflare) -> None:
        with client.cache.origin_cloud_regions.with_streaming_response.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "origin_ip": "192.0.2.1",
                    "region": "us-east-1",
                    "vendor": "aws",
                },
                {
                    "origin_ip": "2001:db8::1",
                    "region": "us-central1",
                    "vendor": "gcp",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = response.parse()
            assert_matches_type(Optional[OriginCloudRegionBulkUpdateResponse], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_bulk_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.bulk_update(
                zone_id="",
                body=[
                    {
                        "origin_ip": "192.0.2.1",
                        "region": "us-east-1",
                        "vendor": "aws",
                    },
                    {
                        "origin_ip": "2001:db8::1",
                        "region": "us-central1",
                        "vendor": "gcp",
                    },
                ],
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        origin_cloud_region = client.cache.origin_cloud_regions.get(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cache.origin_cloud_regions.with_raw_response.get(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = response.parse()
        assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cache.origin_cloud_regions.with_streaming_response.get(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = response.parse()
            assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.get(
                origin_ip="192.0.2.1",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `origin_ip` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.get(
                origin_ip="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_method_supported_regions(self, client: Cloudflare) -> None:
        origin_cloud_region = client.cache.origin_cloud_regions.supported_regions(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCloudRegionSupportedRegionsResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_raw_response_supported_regions(self, client: Cloudflare) -> None:
        response = client.cache.origin_cloud_regions.with_raw_response.supported_regions(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = response.parse()
        assert_matches_type(Optional[OriginCloudRegionSupportedRegionsResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_streaming_response_supported_regions(self, client: Cloudflare) -> None:
        with client.cache.origin_cloud_regions.with_streaming_response.supported_regions(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = response.parse()
            assert_matches_type(
                Optional[OriginCloudRegionSupportedRegionsResponse], origin_cloud_region, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    def test_path_params_supported_regions(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.cache.origin_cloud_regions.with_raw_response.supported_regions(
                zone_id="",
            )


class TestAsyncOriginCloudRegions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        origin_cloud_region = await async_client.cache.origin_cloud_regions.update(
            path_origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body_origin_ip="192.0.2.1",
            region="us-east-1",
            vendor="aws",
        )
        assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.origin_cloud_regions.with_raw_response.update(
            path_origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body_origin_ip="192.0.2.1",
            region="us-east-1",
            vendor="aws",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = await response.parse()
        assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.origin_cloud_regions.with_streaming_response.update(
            path_origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body_origin_ip="192.0.2.1",
            region="us-east-1",
            vendor="aws",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = await response.parse()
            assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism -- route not in spec")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.update(
                path_origin_ip="192.0.2.1",
                zone_id="",
                body_origin_ip="192.0.2.1",
                region="us-east-1",
                vendor="aws",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_origin_ip` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.update(
                path_origin_ip="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                body_origin_ip="192.0.2.1",
                region="us-east-1",
                vendor="aws",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        origin_cloud_region = await async_client.cache.origin_cloud_regions.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        origin_cloud_region = await async_client.cache.origin_cloud_regions.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.origin_cloud_regions.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.origin_cloud_regions.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[OriginCloudRegion], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.list(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        origin_cloud_region = await async_client.cache.origin_cloud_regions.delete(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCloudRegionDeleteResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.origin_cloud_regions.with_raw_response.delete(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = await response.parse()
        assert_matches_type(Optional[OriginCloudRegionDeleteResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.origin_cloud_regions.with_streaming_response.delete(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = await response.parse()
            assert_matches_type(Optional[OriginCloudRegionDeleteResponse], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.delete(
                origin_ip="192.0.2.1",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `origin_ip` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.delete(
                origin_ip="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        origin_cloud_region = await async_client.cache.origin_cloud_regions.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCloudRegionBulkDeleteResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.origin_cloud_regions.with_raw_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = await response.parse()
        assert_matches_type(Optional[OriginCloudRegionBulkDeleteResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.origin_cloud_regions.with_streaming_response.bulk_delete(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = await response.parse()
            assert_matches_type(Optional[OriginCloudRegionBulkDeleteResponse], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_bulk_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.bulk_delete(
                zone_id="",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_bulk_update(self, async_client: AsyncCloudflare) -> None:
        origin_cloud_region = await async_client.cache.origin_cloud_regions.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "origin_ip": "192.0.2.1",
                    "region": "us-east-1",
                    "vendor": "aws",
                },
                {
                    "origin_ip": "2001:db8::1",
                    "region": "us-central1",
                    "vendor": "gcp",
                },
            ],
        )
        assert_matches_type(Optional[OriginCloudRegionBulkUpdateResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.origin_cloud_regions.with_raw_response.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "origin_ip": "192.0.2.1",
                    "region": "us-east-1",
                    "vendor": "aws",
                },
                {
                    "origin_ip": "2001:db8::1",
                    "region": "us-central1",
                    "vendor": "gcp",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = await response.parse()
        assert_matches_type(Optional[OriginCloudRegionBulkUpdateResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_bulk_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.origin_cloud_regions.with_streaming_response.bulk_update(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "origin_ip": "192.0.2.1",
                    "region": "us-east-1",
                    "vendor": "aws",
                },
                {
                    "origin_ip": "2001:db8::1",
                    "region": "us-central1",
                    "vendor": "gcp",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = await response.parse()
            assert_matches_type(Optional[OriginCloudRegionBulkUpdateResponse], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_bulk_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.bulk_update(
                zone_id="",
                body=[
                    {
                        "origin_ip": "192.0.2.1",
                        "region": "us-east-1",
                        "vendor": "aws",
                    },
                    {
                        "origin_ip": "2001:db8::1",
                        "region": "us-central1",
                        "vendor": "gcp",
                    },
                ],
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        origin_cloud_region = await async_client.cache.origin_cloud_regions.get(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.origin_cloud_regions.with_raw_response.get(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = await response.parse()
        assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.origin_cloud_regions.with_streaming_response.get(
            origin_ip="192.0.2.1",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = await response.parse()
            assert_matches_type(Optional[OriginCloudRegion], origin_cloud_region, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.get(
                origin_ip="192.0.2.1",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `origin_ip` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.get(
                origin_ip="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_method_supported_regions(self, async_client: AsyncCloudflare) -> None:
        origin_cloud_region = await async_client.cache.origin_cloud_regions.supported_regions(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCloudRegionSupportedRegionsResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_raw_response_supported_regions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cache.origin_cloud_regions.with_raw_response.supported_regions(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_cloud_region = await response.parse()
        assert_matches_type(Optional[OriginCloudRegionSupportedRegionsResponse], origin_cloud_region, path=["response"])

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_streaming_response_supported_regions(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cache.origin_cloud_regions.with_streaming_response.supported_regions(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_cloud_region = await response.parse()
            assert_matches_type(
                Optional[OriginCloudRegionSupportedRegionsResponse], origin_cloud_region, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="HTTP 404 error from prism")
    @parametrize
    async def test_path_params_supported_regions(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.cache.origin_cloud_regions.with_raw_response.supported_regions(
                zone_id="",
            )
