# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.email_security.investigate import DetectionGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        detection = client.email_security.investigate.detections.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DetectionGetResponse, detection, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.email_security.investigate.detections.with_raw_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = response.parse()
        assert_matches_type(DetectionGetResponse, detection, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.email_security.investigate.detections.with_streaming_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = response.parse()
            assert_matches_type(DetectionGetResponse, detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.email_security.investigate.detections.with_raw_response.get(
                postfix_id="4Njp3P0STMz2c02Q",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `postfix_id` but received ''"):
            client.email_security.investigate.detections.with_raw_response.get(
                postfix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncDetections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        detection = await async_client.email_security.investigate.detections.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(DetectionGetResponse, detection, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.email_security.investigate.detections.with_raw_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detection = await response.parse()
        assert_matches_type(DetectionGetResponse, detection, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.email_security.investigate.detections.with_streaming_response.get(
            postfix_id="4Njp3P0STMz2c02Q",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detection = await response.parse()
            assert_matches_type(DetectionGetResponse, detection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.email_security.investigate.detections.with_raw_response.get(
                postfix_id="4Njp3P0STMz2c02Q",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `postfix_id` but received ''"):
            await async_client.email_security.investigate.detections.with_raw_response.get(
                postfix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )