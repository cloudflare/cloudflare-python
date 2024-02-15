# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types import (
    SpeedAPIAvailabilitiesListResponse,
    SpeedAPIPagesListResponse,
    SpeedAPIScheduleDeleteResponse,
    SpeedAPIScheduleGetResponse,
    SpeedAPITestsCreateResponse,
    SpeedAPITestsDeleteResponse,
    SpeedAPITestsGetResponse,
    SpeedAPITestsListResponse,
    SpeedAPITrendsListResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import speed_api_schedule_delete_params
from cloudflare.types import speed_api_schedule_get_params
from cloudflare.types import speed_api_tests_create_params
from cloudflare.types import speed_api_tests_delete_params
from cloudflare.types import speed_api_tests_list_params
from cloudflare.types import speed_api_trends_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpeedAPI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_availabilities_list(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.availabilities_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPIAvailabilitiesListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_availabilities_list(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.availabilities_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(Optional[SpeedAPIAvailabilitiesListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_availabilities_list(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.availabilities_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(Optional[SpeedAPIAvailabilitiesListResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_availabilities_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.availabilities_list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_pages_list(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.pages_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPIPagesListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_pages_list(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.pages_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(Optional[SpeedAPIPagesListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_pages_list(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.pages_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(Optional[SpeedAPIPagesListResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_pages_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.pages_list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_schedule_delete(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.schedule_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPIScheduleDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_schedule_delete_with_all_params(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.schedule_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedAPIScheduleDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_schedule_delete(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.schedule_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(Optional[SpeedAPIScheduleDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_schedule_delete(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.schedule_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(Optional[SpeedAPIScheduleDeleteResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_schedule_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.schedule_delete(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed_api.with_raw_response.schedule_delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_schedule_get(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPIScheduleGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_schedule_get_with_all_params(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedAPIScheduleGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_schedule_get(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(Optional[SpeedAPIScheduleGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_schedule_get(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(Optional[SpeedAPIScheduleGetResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_schedule_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.schedule_get(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed_api.with_raw_response.schedule_get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_tests_create(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.tests_create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPITestsCreateResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_tests_create_with_all_params(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.tests_create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedAPITestsCreateResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tests_create(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.tests_create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(Optional[SpeedAPITestsCreateResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tests_create(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.tests_create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(Optional[SpeedAPITestsCreateResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tests_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.tests_create(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed_api.with_raw_response.tests_create(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_tests_delete(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.tests_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPITestsDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_tests_delete_with_all_params(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.tests_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedAPITestsDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tests_delete(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.tests_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(Optional[SpeedAPITestsDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tests_delete(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.tests_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(Optional[SpeedAPITestsDeleteResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tests_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.tests_delete(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed_api.with_raw_response.tests_delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_tests_get(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.tests_get(
            "string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        )
        assert_matches_type(Optional[SpeedAPITestsGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tests_get(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.tests_get(
            "string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(Optional[SpeedAPITestsGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tests_get(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.tests_get(
            "string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(Optional[SpeedAPITestsGetResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tests_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.tests_get(
                "string",
                zone_id="",
                url="example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed_api.with_raw_response.tests_get(
                "string",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                url="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            client.speed_api.with_raw_response.tests_get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                url="example.com",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_tests_list(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.tests_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SpeedAPITestsListResponse, speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_tests_list_with_all_params(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.tests_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=20,
            region="us-central1",
        )
        assert_matches_type(SpeedAPITestsListResponse, speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_tests_list(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.tests_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(SpeedAPITestsListResponse, speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_tests_list(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.tests_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(SpeedAPITestsListResponse, speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_tests_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.tests_list(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed_api.with_raw_response.tests_list(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_trends_list(self, client: Cloudflare) -> None:
        speed_api = client.speed_api.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        )
        assert_matches_type(Optional[SpeedAPITrendsListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_trends_list(self, client: Cloudflare) -> None:
        response = client.speed_api.with_raw_response.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = response.parse()
        assert_matches_type(Optional[SpeedAPITrendsListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_trends_list(self, client: Cloudflare) -> None:
        with client.speed_api.with_streaming_response.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = response.parse()
            assert_matches_type(Optional[SpeedAPITrendsListResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_trends_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.speed_api.with_raw_response.trends_list(
                "example.com",
                zone_id="",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="us-central1",
                tz="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            client.speed_api.with_raw_response.trends_list(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="us-central1",
                tz="string",
            )


class TestAsyncSpeedAPI:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_availabilities_list(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.availabilities_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPIAvailabilitiesListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_availabilities_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.availabilities_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(Optional[SpeedAPIAvailabilitiesListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_availabilities_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.availabilities_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(Optional[SpeedAPIAvailabilitiesListResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_availabilities_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.availabilities_list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_pages_list(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.pages_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPIPagesListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_pages_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.pages_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(Optional[SpeedAPIPagesListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_pages_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.pages_list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(Optional[SpeedAPIPagesListResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_pages_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.pages_list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_schedule_delete(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.schedule_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPIScheduleDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_schedule_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.schedule_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedAPIScheduleDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_schedule_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.schedule_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(Optional[SpeedAPIScheduleDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_schedule_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.schedule_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(Optional[SpeedAPIScheduleDeleteResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_schedule_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.schedule_delete(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed_api.with_raw_response.schedule_delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_schedule_get(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPIScheduleGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_schedule_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedAPIScheduleGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_schedule_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(Optional[SpeedAPIScheduleGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_schedule_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.schedule_get(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(Optional[SpeedAPIScheduleGetResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_schedule_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.schedule_get(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed_api.with_raw_response.schedule_get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tests_create(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.tests_create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPITestsCreateResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_tests_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.tests_create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedAPITestsCreateResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tests_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.tests_create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(Optional[SpeedAPITestsCreateResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tests_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.tests_create(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(Optional[SpeedAPITestsCreateResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tests_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.tests_create(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed_api.with_raw_response.tests_create(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tests_delete(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.tests_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SpeedAPITestsDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_tests_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.tests_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            region="us-central1",
        )
        assert_matches_type(Optional[SpeedAPITestsDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tests_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.tests_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(Optional[SpeedAPITestsDeleteResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tests_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.tests_delete(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(Optional[SpeedAPITestsDeleteResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tests_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.tests_delete(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed_api.with_raw_response.tests_delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tests_get(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.tests_get(
            "string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        )
        assert_matches_type(Optional[SpeedAPITestsGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tests_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.tests_get(
            "string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(Optional[SpeedAPITestsGetResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tests_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.tests_get(
            "string",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            url="example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(Optional[SpeedAPITestsGetResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tests_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.tests_get(
                "string",
                zone_id="",
                url="example.com",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed_api.with_raw_response.tests_get(
                "string",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                url="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_id` but received ''"):
            await async_client.speed_api.with_raw_response.tests_get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                url="example.com",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_tests_list(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.tests_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SpeedAPITestsListResponse, speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_tests_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.tests_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=20,
            region="us-central1",
        )
        assert_matches_type(SpeedAPITestsListResponse, speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_tests_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.tests_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(SpeedAPITestsListResponse, speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_tests_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.tests_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(SpeedAPITestsListResponse, speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_tests_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.tests_list(
                "example.com",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed_api.with_raw_response.tests_list(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_trends_list(self, async_client: AsyncCloudflare) -> None:
        speed_api = await async_client.speed_api.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        )
        assert_matches_type(Optional[SpeedAPITrendsListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_trends_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.speed_api.with_raw_response.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        speed_api = await response.parse()
        assert_matches_type(Optional[SpeedAPITrendsListResponse], speed_api, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_trends_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.speed_api.with_streaming_response.trends_list(
            "example.com",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            device_type="DESKTOP",
            metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
            region="us-central1",
            tz="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            speed_api = await response.parse()
            assert_matches_type(Optional[SpeedAPITrendsListResponse], speed_api, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_trends_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.speed_api.with_raw_response.trends_list(
                "example.com",
                zone_id="",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="us-central1",
                tz="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `url` but received ''"):
            await async_client.speed_api.with_raw_response.trends_list(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                device_type="DESKTOP",
                metrics="performanceScore,ttfb,fcp,si,lcp,tti,tbt,cls",
                region="us-central1",
                tz="string",
            )
