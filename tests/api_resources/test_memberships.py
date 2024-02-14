# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types import (
    MembershipUpdateResponse,
    MembershipDeleteResponse,
    MembershipGetResponse,
    MembershipUserSAccountMembershipsListMembershipsResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import membership_update_params
from cloudflare.types import membership_user_s_account_memberships_list_memberships_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemberships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        membership = client.memberships.update(
            "4536bcfad5faccb111b47003c79917fa",
            status="accepted",
        )
        assert_matches_type(MembershipUpdateResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.memberships.with_raw_response.update(
            "4536bcfad5faccb111b47003c79917fa",
            status="accepted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipUpdateResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.memberships.with_streaming_response.update(
            "4536bcfad5faccb111b47003c79917fa",
            status="accepted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipUpdateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `membership_id` but received ''"):
            client.memberships.with_raw_response.update(
                "",
                status="accepted",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        membership = client.memberships.delete(
            "4536bcfad5faccb111b47003c79917fa",
        )
        assert_matches_type(MembershipDeleteResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.memberships.with_raw_response.delete(
            "4536bcfad5faccb111b47003c79917fa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipDeleteResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.memberships.with_streaming_response.delete(
            "4536bcfad5faccb111b47003c79917fa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipDeleteResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `membership_id` but received ''"):
            client.memberships.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        membership = client.memberships.get(
            "4536bcfad5faccb111b47003c79917fa",
        )
        assert_matches_type(MembershipGetResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.memberships.with_raw_response.get(
            "4536bcfad5faccb111b47003c79917fa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipGetResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.memberships.with_streaming_response.get(
            "4536bcfad5faccb111b47003c79917fa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipGetResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `membership_id` but received ''"):
            client.memberships.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_s_account_memberships_list_memberships(self, client: Cloudflare) -> None:
        membership = client.memberships.user_s_account_memberships_list_memberships()
        assert_matches_type(
            Optional[MembershipUserSAccountMembershipsListMembershipsResponse], membership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_s_account_memberships_list_memberships_with_all_params(self, client: Cloudflare) -> None:
        membership = client.memberships.user_s_account_memberships_list_memberships(
            account={"name": "Demo Account"},
            direction="desc",
            name="Demo Account",
            order="status",
            page=1,
            per_page=5,
            status="accepted",
        )
        assert_matches_type(
            Optional[MembershipUserSAccountMembershipsListMembershipsResponse], membership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_s_account_memberships_list_memberships(self, client: Cloudflare) -> None:
        response = client.memberships.with_raw_response.user_s_account_memberships_list_memberships()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(
            Optional[MembershipUserSAccountMembershipsListMembershipsResponse], membership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_s_account_memberships_list_memberships(self, client: Cloudflare) -> None:
        with client.memberships.with_streaming_response.user_s_account_memberships_list_memberships() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(
                Optional[MembershipUserSAccountMembershipsListMembershipsResponse], membership, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncMemberships:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        membership = await async_client.memberships.update(
            "4536bcfad5faccb111b47003c79917fa",
            status="accepted",
        )
        assert_matches_type(MembershipUpdateResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.memberships.with_raw_response.update(
            "4536bcfad5faccb111b47003c79917fa",
            status="accepted",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipUpdateResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.memberships.with_streaming_response.update(
            "4536bcfad5faccb111b47003c79917fa",
            status="accepted",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipUpdateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `membership_id` but received ''"):
            await async_client.memberships.with_raw_response.update(
                "",
                status="accepted",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        membership = await async_client.memberships.delete(
            "4536bcfad5faccb111b47003c79917fa",
        )
        assert_matches_type(MembershipDeleteResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.memberships.with_raw_response.delete(
            "4536bcfad5faccb111b47003c79917fa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipDeleteResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.memberships.with_streaming_response.delete(
            "4536bcfad5faccb111b47003c79917fa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipDeleteResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `membership_id` but received ''"):
            await async_client.memberships.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        membership = await async_client.memberships.get(
            "4536bcfad5faccb111b47003c79917fa",
        )
        assert_matches_type(MembershipGetResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.memberships.with_raw_response.get(
            "4536bcfad5faccb111b47003c79917fa",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipGetResponse, membership, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.memberships.with_streaming_response.get(
            "4536bcfad5faccb111b47003c79917fa",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipGetResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `membership_id` but received ''"):
            await async_client.memberships.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_s_account_memberships_list_memberships(self, async_client: AsyncCloudflare) -> None:
        membership = await async_client.memberships.user_s_account_memberships_list_memberships()
        assert_matches_type(
            Optional[MembershipUserSAccountMembershipsListMembershipsResponse], membership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_s_account_memberships_list_memberships_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        membership = await async_client.memberships.user_s_account_memberships_list_memberships(
            account={"name": "Demo Account"},
            direction="desc",
            name="Demo Account",
            order="status",
            page=1,
            per_page=5,
            status="accepted",
        )
        assert_matches_type(
            Optional[MembershipUserSAccountMembershipsListMembershipsResponse], membership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_s_account_memberships_list_memberships(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.memberships.with_raw_response.user_s_account_memberships_list_memberships()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(
            Optional[MembershipUserSAccountMembershipsListMembershipsResponse], membership, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_s_account_memberships_list_memberships(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.memberships.with_streaming_response.user_s_account_memberships_list_memberships() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(
                Optional[MembershipUserSAccountMembershipsListMembershipsResponse], membership, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
