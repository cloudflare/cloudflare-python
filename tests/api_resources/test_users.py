# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import UserUserEditUserResponse, UserUserUserDetailsResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import user_user_edit_user_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_user_edit_user(self, client: Cloudflare) -> None:
        user = client.users.user_edit_user()
        assert_matches_type(UserUserEditUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_user_edit_user_with_all_params(self, client: Cloudflare) -> None:
        user = client.users.user_edit_user(
            country="US",
            first_name="John",
            last_name="Appleseed",
            telephone="+1 123-123-1234",
            zipcode="12345",
        )
        assert_matches_type(UserUserEditUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_edit_user(self, client: Cloudflare) -> None:
        response = client.users.with_raw_response.user_edit_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUserEditUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_edit_user(self, client: Cloudflare) -> None:
        with client.users.with_streaming_response.user_edit_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUserEditUserResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_user_user_details(self, client: Cloudflare) -> None:
        user = client.users.user_user_details()
        assert_matches_type(UserUserUserDetailsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_user_details(self, client: Cloudflare) -> None:
        response = client.users.with_raw_response.user_user_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserUserUserDetailsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_user_details(self, client: Cloudflare) -> None:
        with client.users.with_streaming_response.user_user_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserUserUserDetailsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_edit_user(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.users.user_edit_user()
        assert_matches_type(UserUserEditUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_edit_user_with_all_params(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.users.user_edit_user(
            country="US",
            first_name="John",
            last_name="Appleseed",
            telephone="+1 123-123-1234",
            zipcode="12345",
        )
        assert_matches_type(UserUserEditUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_edit_user(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.with_raw_response.user_edit_user()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUserEditUserResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_edit_user(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.with_streaming_response.user_edit_user() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUserEditUserResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_user_details(self, async_client: AsyncCloudflare) -> None:
        user = await async_client.users.user_user_details()
        assert_matches_type(UserUserUserDetailsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_user_details(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.users.with_raw_response.user_user_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserUserUserDetailsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_user_details(self, async_client: AsyncCloudflare) -> None:
        async with async_client.users.with_streaming_response.user_user_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserUserUserDetailsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
