# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.user import Invite

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvites:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        invite = client.user.invites.list()
        assert_matches_type(SyncSinglePage[Invite], invite, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.user.invites.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(SyncSinglePage[Invite], invite, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.user.invites.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(SyncSinglePage[Invite], invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        invite = client.user.invites.edit(
            invite_id="4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        )
        assert_matches_type(Optional[Invite], invite, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.user.invites.with_raw_response.edit(
            invite_id="4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(Optional[Invite], invite, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.user.invites.with_streaming_response.edit(
            invite_id="4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(Optional[Invite], invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.user.invites.with_raw_response.edit(
                invite_id="",
                status="accepted",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        invite = client.user.invites.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        )
        assert_matches_type(Optional[Invite], invite, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.user.invites.with_raw_response.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(Optional[Invite], invite, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.user.invites.with_streaming_response.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(Optional[Invite], invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            client.user.invites.with_raw_response.get(
                "",
            )


class TestAsyncInvites:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        invite = await async_client.user.invites.list()
        assert_matches_type(AsyncSinglePage[Invite], invite, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.invites.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(AsyncSinglePage[Invite], invite, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.invites.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(AsyncSinglePage[Invite], invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        invite = await async_client.user.invites.edit(
            invite_id="4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        )
        assert_matches_type(Optional[Invite], invite, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.invites.with_raw_response.edit(
            invite_id="4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(Optional[Invite], invite, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.invites.with_streaming_response.edit(
            invite_id="4f5f0c14a2a41d5063dd301b2f829f04",
            status="accepted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(Optional[Invite], invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.user.invites.with_raw_response.edit(
                invite_id="",
                status="accepted",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        invite = await async_client.user.invites.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        )
        assert_matches_type(Optional[Invite], invite, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.user.invites.with_raw_response.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(Optional[Invite], invite, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.user.invites.with_streaming_response.get(
            "4f5f0c14a2a41d5063dd301b2f829f04",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(Optional[Invite], invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invite_id` but received ''"):
            await async_client.user.invites.with_raw_response.get(
                "",
            )
