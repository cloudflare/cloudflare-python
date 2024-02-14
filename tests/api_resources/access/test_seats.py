# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.access import SeatZeroTrustSeatsUpdateAUserSeatResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import seat_zero_trust_seats_update_a_user_seat_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSeats:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_seats_update_a_user_seat(self, client: Cloudflare) -> None:
        seat = client.access.seats.zero_trust_seats_update_a_user_seat(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse], seat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_seats_update_a_user_seat(self, client: Cloudflare) -> None:
        response = client.access.seats.with_raw_response.zero_trust_seats_update_a_user_seat(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse], seat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_seats_update_a_user_seat(self, client: Cloudflare) -> None:
        with client.access.seats.with_streaming_response.zero_trust_seats_update_a_user_seat(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
            assert_matches_type(Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse], seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zero_trust_seats_update_a_user_seat(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.seats.with_raw_response.zero_trust_seats_update_a_user_seat(
                "",
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

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_seats_update_a_user_seat(self, async_client: AsyncCloudflare) -> None:
        seat = await async_client.access.seats.zero_trust_seats_update_a_user_seat(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse], seat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_seats_update_a_user_seat(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.seats.with_raw_response.zero_trust_seats_update_a_user_seat(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
        assert_matches_type(Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse], seat, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_seats_update_a_user_seat(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.seats.with_streaming_response.zero_trust_seats_update_a_user_seat(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
            assert_matches_type(Optional[SeatZeroTrustSeatsUpdateAUserSeatResponse], seat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zero_trust_seats_update_a_user_seat(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.seats.with_raw_response.zero_trust_seats_update_a_user_seat(
                "",
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
