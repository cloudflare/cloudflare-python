# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.users.billings import HistoryUserBillingHistoryBillingHistoryDetailsResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users.billings import history_user_billing_history_billing_history_details_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_user_billing_history_billing_history_details(self, client: Cloudflare) -> None:
        history = client.users.billings.histories.user_billing_history_billing_history_details()
        assert_matches_type(
            Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse], history, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_user_billing_history_billing_history_details_with_all_params(self, client: Cloudflare) -> None:
        history = client.users.billings.histories.user_billing_history_billing_history_details(
            order="occured_at",
            page=1,
            per_page=5,
        )
        assert_matches_type(
            Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse], history, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_user_billing_history_billing_history_details(self, client: Cloudflare) -> None:
        response = client.users.billings.histories.with_raw_response.user_billing_history_billing_history_details()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(
            Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse], history, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_user_billing_history_billing_history_details(self, client: Cloudflare) -> None:
        with client.users.billings.histories.with_streaming_response.user_billing_history_billing_history_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(
                Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse], history, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncHistories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_billing_history_billing_history_details(self, async_client: AsyncCloudflare) -> None:
        history = await async_client.users.billings.histories.user_billing_history_billing_history_details()
        assert_matches_type(
            Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse], history, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_user_billing_history_billing_history_details_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        history = await async_client.users.billings.histories.user_billing_history_billing_history_details(
            order="occured_at",
            page=1,
            per_page=5,
        )
        assert_matches_type(
            Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse], history, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_user_billing_history_billing_history_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.users.billings.histories.with_raw_response.user_billing_history_billing_history_details()
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(
            Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse], history, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_user_billing_history_billing_history_details(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.billings.histories.with_streaming_response.user_billing_history_billing_history_details() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(
                Optional[HistoryUserBillingHistoryBillingHistoryDetailsResponse], history, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
