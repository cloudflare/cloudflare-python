# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.alerting.v3s import HistoryNotificationHistoryListHistoryResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.alerting.v3s import history_notification_history_list_history_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_notification_history_list_history(self, client: Cloudflare) -> None:
        history = client.alerting.v3s.histories.notification_history_list_history(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HistoryNotificationHistoryListHistoryResponse], history, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_notification_history_list_history_with_all_params(self, client: Cloudflare) -> None:
        history = client.alerting.v3s.histories.notification_history_list_history(
            "023e105f4ecef8ad9ca31a8372d0c353",
            before=parse_datetime("2022-05-20T20:29:58.679897Z"),
            page=1,
            per_page=5,
            since=parse_datetime("2022-05-19T20:29:58.679897Z"),
        )
        assert_matches_type(Optional[HistoryNotificationHistoryListHistoryResponse], history, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_notification_history_list_history(self, client: Cloudflare) -> None:
        response = client.alerting.v3s.histories.with_raw_response.notification_history_list_history(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(Optional[HistoryNotificationHistoryListHistoryResponse], history, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_notification_history_list_history(self, client: Cloudflare) -> None:
        with client.alerting.v3s.histories.with_streaming_response.notification_history_list_history(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(Optional[HistoryNotificationHistoryListHistoryResponse], history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_notification_history_list_history(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3s.histories.with_raw_response.notification_history_list_history(
                "",
            )


class TestAsyncHistories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_notification_history_list_history(self, async_client: AsyncCloudflare) -> None:
        history = await async_client.alerting.v3s.histories.notification_history_list_history(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HistoryNotificationHistoryListHistoryResponse], history, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_notification_history_list_history_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        history = await async_client.alerting.v3s.histories.notification_history_list_history(
            "023e105f4ecef8ad9ca31a8372d0c353",
            before=parse_datetime("2022-05-20T20:29:58.679897Z"),
            page=1,
            per_page=5,
            since=parse_datetime("2022-05-19T20:29:58.679897Z"),
        )
        assert_matches_type(Optional[HistoryNotificationHistoryListHistoryResponse], history, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_notification_history_list_history(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.alerting.v3s.histories.with_raw_response.notification_history_list_history(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(Optional[HistoryNotificationHistoryListHistoryResponse], history, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_notification_history_list_history(self, async_client: AsyncCloudflare) -> None:
        async with async_client.alerting.v3s.histories.with_streaming_response.notification_history_list_history(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(Optional[HistoryNotificationHistoryListHistoryResponse], history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_notification_history_list_history(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3s.histories.with_raw_response.notification_history_list_history(
                "",
            )
