# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.access.logs import AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccessRequests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_access_authentication_logs_get_access_authentication_logs(self, client: Cloudflare) -> None:
        access_request = client.access.logs.access_requests.access_authentication_logs_get_access_authentication_logs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse],
            access_request,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_authentication_logs_get_access_authentication_logs(self, client: Cloudflare) -> None:
        response = client.access.logs.access_requests.with_raw_response.access_authentication_logs_get_access_authentication_logs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_request = response.parse()
        assert_matches_type(
            Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse],
            access_request,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_authentication_logs_get_access_authentication_logs(
        self, client: Cloudflare
    ) -> None:
        with client.access.logs.access_requests.with_streaming_response.access_authentication_logs_get_access_authentication_logs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_request = response.parse()
            assert_matches_type(
                Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse],
                access_request,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_authentication_logs_get_access_authentication_logs(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.access.logs.access_requests.with_raw_response.access_authentication_logs_get_access_authentication_logs(
                "",
            )


class TestAsyncAccessRequests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_authentication_logs_get_access_authentication_logs(
        self, async_client: AsyncCloudflare
    ) -> None:
        access_request = (
            await async_client.access.logs.access_requests.access_authentication_logs_get_access_authentication_logs(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )
        assert_matches_type(
            Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse],
            access_request,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_authentication_logs_get_access_authentication_logs(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.access.logs.access_requests.with_raw_response.access_authentication_logs_get_access_authentication_logs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        access_request = await response.parse()
        assert_matches_type(
            Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse],
            access_request,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_authentication_logs_get_access_authentication_logs(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.logs.access_requests.with_streaming_response.access_authentication_logs_get_access_authentication_logs(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            access_request = await response.parse()
            assert_matches_type(
                Optional[AccessRequestAccessAuthenticationLogsGetAccessAuthenticationLogsResponse],
                access_request,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_authentication_logs_get_access_authentication_logs(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.access.logs.access_requests.with_raw_response.access_authentication_logs_get_access_authentication_logs(
                "",
            )
