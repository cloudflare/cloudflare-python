# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust import SeatEditResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        seat = client.zero_trust.seats.edit(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
            ],
        )
        assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.seats.with_raw_response.edit(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = response.parse()
        assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.seats.with_streaming_response.edit(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = response.parse()
            assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.seats.with_raw_response.edit(
                account_id="",
                body=[
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                    },
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                    },
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                    },
                ],
            )


class TestAsyncSeats:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        seat = await async_client.zero_trust.seats.edit(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
            ],
        )
        assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.seats.with_raw_response.edit(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        seat = await response.parse()
        assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.seats.with_streaming_response.edit(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
                {
                    "access_seat": False,
                    "gateway_seat": False,
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            seat = await response.parse()
            assert_matches_type(Optional[SeatEditResponse], seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.seats.with_raw_response.edit(
                account_id="",
                body=[
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                    },
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                    },
                    {
                        "access_seat": False,
                        "gateway_seat": False,
                    },
                ],
            )
