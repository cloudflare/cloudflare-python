# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.realtime_kit import (
    ActiveSessionCreatePollResponse,
    ActiveSessionGetActiveSessionResponse,
    ActiveSessionKickParticipantsResponse,
    ActiveSessionKickAllParticipantsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestActiveSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_create_poll(self, client: Cloudflare) -> None:
        active_session = client.realtime_kit.active_session.create_poll(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            options=["string"],
            question="question",
        )
        assert_matches_type(ActiveSessionCreatePollResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_create_poll_with_all_params(self, client: Cloudflare) -> None:
        active_session = client.realtime_kit.active_session.create_poll(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            options=["string"],
            question="question",
            anonymous=True,
            hide_votes=True,
        )
        assert_matches_type(ActiveSessionCreatePollResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_create_poll(self, client: Cloudflare) -> None:
        response = client.realtime_kit.active_session.with_raw_response.create_poll(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            options=["string"],
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_session = response.parse()
        assert_matches_type(ActiveSessionCreatePollResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_create_poll(self, client: Cloudflare) -> None:
        with client.realtime_kit.active_session.with_streaming_response.create_poll(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            options=["string"],
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_session = response.parse()
            assert_matches_type(ActiveSessionCreatePollResponse, active_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_create_poll(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.create_poll(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
                options=["string"],
                question="question",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.create_poll(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                options=["string"],
                question="question",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.create_poll(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                options=["string"],
                question="question",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_active_session(self, client: Cloudflare) -> None:
        active_session = client.realtime_kit.active_session.get_active_session(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(ActiveSessionGetActiveSessionResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_active_session(self, client: Cloudflare) -> None:
        response = client.realtime_kit.active_session.with_raw_response.get_active_session(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_session = response.parse()
        assert_matches_type(ActiveSessionGetActiveSessionResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_active_session(self, client: Cloudflare) -> None:
        with client.realtime_kit.active_session.with_streaming_response.get_active_session(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_session = response.parse()
            assert_matches_type(ActiveSessionGetActiveSessionResponse, active_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_active_session(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.get_active_session(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.get_active_session(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.get_active_session(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_kick_all_participants(self, client: Cloudflare) -> None:
        active_session = client.realtime_kit.active_session.kick_all_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(ActiveSessionKickAllParticipantsResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_kick_all_participants(self, client: Cloudflare) -> None:
        response = client.realtime_kit.active_session.with_raw_response.kick_all_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_session = response.parse()
        assert_matches_type(ActiveSessionKickAllParticipantsResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_kick_all_participants(self, client: Cloudflare) -> None:
        with client.realtime_kit.active_session.with_streaming_response.kick_all_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_session = response.parse()
            assert_matches_type(ActiveSessionKickAllParticipantsResponse, active_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_kick_all_participants(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.kick_all_participants(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.kick_all_participants(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.kick_all_participants(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_kick_participants(self, client: Cloudflare) -> None:
        active_session = client.realtime_kit.active_session.kick_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_ids=["string"],
            participant_ids=["string"],
        )
        assert_matches_type(ActiveSessionKickParticipantsResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_kick_participants(self, client: Cloudflare) -> None:
        response = client.realtime_kit.active_session.with_raw_response.kick_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_ids=["string"],
            participant_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_session = response.parse()
        assert_matches_type(ActiveSessionKickParticipantsResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_kick_participants(self, client: Cloudflare) -> None:
        with client.realtime_kit.active_session.with_streaming_response.kick_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_ids=["string"],
            participant_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_session = response.parse()
            assert_matches_type(ActiveSessionKickParticipantsResponse, active_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_kick_participants(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.kick_participants(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
                custom_participant_ids=["string"],
                participant_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.kick_participants(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                custom_participant_ids=["string"],
                participant_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.active_session.with_raw_response.kick_participants(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                custom_participant_ids=["string"],
                participant_ids=["string"],
            )


class TestAsyncActiveSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_create_poll(self, async_client: AsyncCloudflare) -> None:
        active_session = await async_client.realtime_kit.active_session.create_poll(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            options=["string"],
            question="question",
        )
        assert_matches_type(ActiveSessionCreatePollResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_create_poll_with_all_params(self, async_client: AsyncCloudflare) -> None:
        active_session = await async_client.realtime_kit.active_session.create_poll(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            options=["string"],
            question="question",
            anonymous=True,
            hide_votes=True,
        )
        assert_matches_type(ActiveSessionCreatePollResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_create_poll(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.active_session.with_raw_response.create_poll(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            options=["string"],
            question="question",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_session = await response.parse()
        assert_matches_type(ActiveSessionCreatePollResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_create_poll(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.active_session.with_streaming_response.create_poll(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            options=["string"],
            question="question",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_session = await response.parse()
            assert_matches_type(ActiveSessionCreatePollResponse, active_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_create_poll(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.create_poll(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
                options=["string"],
                question="question",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.create_poll(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                options=["string"],
                question="question",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.create_poll(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                options=["string"],
                question="question",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_active_session(self, async_client: AsyncCloudflare) -> None:
        active_session = await async_client.realtime_kit.active_session.get_active_session(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(ActiveSessionGetActiveSessionResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_active_session(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.active_session.with_raw_response.get_active_session(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_session = await response.parse()
        assert_matches_type(ActiveSessionGetActiveSessionResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_active_session(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.active_session.with_streaming_response.get_active_session(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_session = await response.parse()
            assert_matches_type(ActiveSessionGetActiveSessionResponse, active_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_active_session(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.get_active_session(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.get_active_session(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.get_active_session(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_kick_all_participants(self, async_client: AsyncCloudflare) -> None:
        active_session = await async_client.realtime_kit.active_session.kick_all_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(ActiveSessionKickAllParticipantsResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_kick_all_participants(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.active_session.with_raw_response.kick_all_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_session = await response.parse()
        assert_matches_type(ActiveSessionKickAllParticipantsResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_kick_all_participants(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.active_session.with_streaming_response.kick_all_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_session = await response.parse()
            assert_matches_type(ActiveSessionKickAllParticipantsResponse, active_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_kick_all_participants(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.kick_all_participants(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.kick_all_participants(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.kick_all_participants(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_kick_participants(self, async_client: AsyncCloudflare) -> None:
        active_session = await async_client.realtime_kit.active_session.kick_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_ids=["string"],
            participant_ids=["string"],
        )
        assert_matches_type(ActiveSessionKickParticipantsResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_kick_participants(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.active_session.with_raw_response.kick_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_ids=["string"],
            participant_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        active_session = await response.parse()
        assert_matches_type(ActiveSessionKickParticipantsResponse, active_session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_kick_participants(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.active_session.with_streaming_response.kick_participants(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_ids=["string"],
            participant_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            active_session = await response.parse()
            assert_matches_type(ActiveSessionKickParticipantsResponse, active_session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_kick_participants(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.kick_participants(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
                custom_participant_ids=["string"],
                participant_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.kick_participants(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                custom_participant_ids=["string"],
                participant_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.active_session.with_raw_response.kick_participants(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                custom_participant_ids=["string"],
                participant_ids=["string"],
            )
