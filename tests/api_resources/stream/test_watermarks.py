# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.stream import (
    WatermarkDeleteResponse,
    WatermarkGetResponse,
    WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse,
    WatermarkStreamWatermarkProfileListWatermarkProfilesResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import watermark_stream_watermark_profile_create_watermark_profiles_via_basic_upload_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatermarks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        watermark = client.stream.watermarks.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WatermarkDeleteResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.watermarks.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = response.parse()
        assert_matches_type(WatermarkDeleteResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.watermarks.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = response.parse()
            assert_matches_type(WatermarkDeleteResponse, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.watermarks.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.watermarks.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        watermark = client.stream.watermarks.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WatermarkGetResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.stream.watermarks.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = response.parse()
        assert_matches_type(WatermarkGetResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.stream.watermarks.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = response.parse()
            assert_matches_type(WatermarkGetResponse, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.watermarks.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.watermarks.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self, client: Cloudflare
    ) -> None:
        watermark = client.stream.watermarks.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        )
        assert_matches_type(
            WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse, watermark, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_watermark_profile_create_watermark_profiles_via_basic_upload_with_all_params(
        self, client: Cloudflare
    ) -> None:
        watermark = client.stream.watermarks.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
            name="Marketing Videos",
            opacity=0.75,
            padding=0.1,
            position="center",
            scale=0.1,
        )
        assert_matches_type(
            WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse, watermark, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self, client: Cloudflare
    ) -> None:
        response = client.stream.watermarks.with_raw_response.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = response.parse()
        assert_matches_type(
            WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse, watermark, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self, client: Cloudflare
    ) -> None:
        with client.stream.watermarks.with_streaming_response.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = response.parse()
            assert_matches_type(
                WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse,
                watermark,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.watermarks.with_raw_response.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
                "",
                file="@/Users/rchen/Downloads/watermark.png",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_watermark_profile_list_watermark_profiles(self, client: Cloudflare) -> None:
        watermark = client.stream.watermarks.stream_watermark_profile_list_watermark_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WatermarkStreamWatermarkProfileListWatermarkProfilesResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_watermark_profile_list_watermark_profiles(self, client: Cloudflare) -> None:
        response = client.stream.watermarks.with_raw_response.stream_watermark_profile_list_watermark_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = response.parse()
        assert_matches_type(WatermarkStreamWatermarkProfileListWatermarkProfilesResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_watermark_profile_list_watermark_profiles(self, client: Cloudflare) -> None:
        with client.stream.watermarks.with_streaming_response.stream_watermark_profile_list_watermark_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = response.parse()
            assert_matches_type(
                WatermarkStreamWatermarkProfileListWatermarkProfilesResponse, watermark, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_watermark_profile_list_watermark_profiles(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.watermarks.with_raw_response.stream_watermark_profile_list_watermark_profiles(
                "",
            )


class TestAsyncWatermarks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        watermark = await async_client.stream.watermarks.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WatermarkDeleteResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.watermarks.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = await response.parse()
        assert_matches_type(WatermarkDeleteResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.watermarks.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = await response.parse()
            assert_matches_type(WatermarkDeleteResponse, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.watermarks.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.watermarks.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        watermark = await async_client.stream.watermarks.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WatermarkGetResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.watermarks.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = await response.parse()
        assert_matches_type(WatermarkGetResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.watermarks.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = await response.parse()
            assert_matches_type(WatermarkGetResponse, watermark, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.watermarks.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.watermarks.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self, async_client: AsyncCloudflare
    ) -> None:
        watermark = (
            await async_client.stream.watermarks.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
                "023e105f4ecef8ad9ca31a8372d0c353",
                file="@/Users/rchen/Downloads/watermark.png",
            )
        )
        assert_matches_type(
            WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse, watermark, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_watermark_profile_create_watermark_profiles_via_basic_upload_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        watermark = (
            await async_client.stream.watermarks.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
                "023e105f4ecef8ad9ca31a8372d0c353",
                file="@/Users/rchen/Downloads/watermark.png",
                name="Marketing Videos",
                opacity=0.75,
                padding=0.1,
                position="center",
                scale=0.1,
            )
        )
        assert_matches_type(
            WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse, watermark, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.stream.watermarks.with_raw_response.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = await response.parse()
        assert_matches_type(
            WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse, watermark, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.watermarks.with_streaming_response.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
            "023e105f4ecef8ad9ca31a8372d0c353",
            file="@/Users/rchen/Downloads/watermark.png",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = await response.parse()
            assert_matches_type(
                WatermarkStreamWatermarkProfileCreateWatermarkProfilesViaBasicUploadResponse,
                watermark,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_watermark_profile_create_watermark_profiles_via_basic_upload(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.watermarks.with_raw_response.stream_watermark_profile_create_watermark_profiles_via_basic_upload(
                "",
                file="@/Users/rchen/Downloads/watermark.png",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_watermark_profile_list_watermark_profiles(self, async_client: AsyncCloudflare) -> None:
        watermark = await async_client.stream.watermarks.stream_watermark_profile_list_watermark_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(WatermarkStreamWatermarkProfileListWatermarkProfilesResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_watermark_profile_list_watermark_profiles(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.stream.watermarks.with_raw_response.stream_watermark_profile_list_watermark_profiles(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watermark = await response.parse()
        assert_matches_type(WatermarkStreamWatermarkProfileListWatermarkProfilesResponse, watermark, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_watermark_profile_list_watermark_profiles(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.watermarks.with_streaming_response.stream_watermark_profile_list_watermark_profiles(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watermark = await response.parse()
            assert_matches_type(
                WatermarkStreamWatermarkProfileListWatermarkProfilesResponse, watermark, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_watermark_profile_list_watermark_profiles(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.watermarks.with_raw_response.stream_watermark_profile_list_watermark_profiles(
                "",
            )
