# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import (
    FilterDeleteResponse,
    FilterUpdateResponse,
    FilterWorkerFiltersDeprecatedListFiltersResponse,
    FilterWorkerFiltersDeprecatedCreateFilterResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFilters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        filter = client.workers.filters.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        )
        assert_matches_type(FilterUpdateResponse, filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers.filters.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FilterUpdateResponse, filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers.filters.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(FilterUpdateResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.filters.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                enabled=True,
                pattern="example.net/*",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
            client.workers.filters.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                enabled=True,
                pattern="example.net/*",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        filter = client.workers.filters.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.filters.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.filters.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.filters.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
            client.workers.filters.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_filters_deprecated_create_filter(self, client: Cloudflare) -> None:
        filter = client.workers.filters.worker_filters_deprecated_create_filter(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        )
        assert_matches_type(Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_filters_deprecated_create_filter(self, client: Cloudflare) -> None:
        response = client.workers.filters.with_raw_response.worker_filters_deprecated_create_filter(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_filters_deprecated_create_filter(self, client: Cloudflare) -> None:
        with client.workers.filters.with_streaming_response.worker_filters_deprecated_create_filter(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_filters_deprecated_create_filter(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.filters.with_raw_response.worker_filters_deprecated_create_filter(
                "",
                enabled=True,
                pattern="example.net/*",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_worker_filters_deprecated_list_filters(self, client: Cloudflare) -> None:
        filter = client.workers.filters.worker_filters_deprecated_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FilterWorkerFiltersDeprecatedListFiltersResponse, filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_worker_filters_deprecated_list_filters(self, client: Cloudflare) -> None:
        response = client.workers.filters.with_raw_response.worker_filters_deprecated_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = response.parse()
        assert_matches_type(FilterWorkerFiltersDeprecatedListFiltersResponse, filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_worker_filters_deprecated_list_filters(self, client: Cloudflare) -> None:
        with client.workers.filters.with_streaming_response.worker_filters_deprecated_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = response.parse()
            assert_matches_type(FilterWorkerFiltersDeprecatedListFiltersResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_worker_filters_deprecated_list_filters(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.workers.filters.with_raw_response.worker_filters_deprecated_list_filters(
                "",
            )


class TestAsyncFilters:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.workers.filters.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        )
        assert_matches_type(FilterUpdateResponse, filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.filters.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FilterUpdateResponse, filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.filters.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(FilterUpdateResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.filters.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                enabled=True,
                pattern="example.net/*",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
            await async_client.workers.filters.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                enabled=True,
                pattern="example.net/*",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.workers.filters.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.filters.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.filters.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(Optional[FilterDeleteResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.filters.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `filter_id` but received ''"):
            await async_client.workers.filters.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_filters_deprecated_create_filter(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.workers.filters.worker_filters_deprecated_create_filter(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        )
        assert_matches_type(Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_filters_deprecated_create_filter(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.filters.with_raw_response.worker_filters_deprecated_create_filter(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse], filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_filters_deprecated_create_filter(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.workers.filters.with_streaming_response.worker_filters_deprecated_create_filter(
            "023e105f4ecef8ad9ca31a8372d0c353",
            enabled=True,
            pattern="example.net/*",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(Optional[FilterWorkerFiltersDeprecatedCreateFilterResponse], filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_filters_deprecated_create_filter(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.filters.with_raw_response.worker_filters_deprecated_create_filter(
                "",
                enabled=True,
                pattern="example.net/*",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_worker_filters_deprecated_list_filters(self, async_client: AsyncCloudflare) -> None:
        filter = await async_client.workers.filters.worker_filters_deprecated_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(FilterWorkerFiltersDeprecatedListFiltersResponse, filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_worker_filters_deprecated_list_filters(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.filters.with_raw_response.worker_filters_deprecated_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        filter = await response.parse()
        assert_matches_type(FilterWorkerFiltersDeprecatedListFiltersResponse, filter, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_worker_filters_deprecated_list_filters(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.workers.filters.with_streaming_response.worker_filters_deprecated_list_filters(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            filter = await response.parse()
            assert_matches_type(FilterWorkerFiltersDeprecatedListFiltersResponse, filter, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_worker_filters_deprecated_list_filters(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.workers.filters.with_raw_response.worker_filters_deprecated_list_filters(
                "",
            )
