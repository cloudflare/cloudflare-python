# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.realtime_kit import (
    SessionGetSessionsResponse,
    SessionGetSessionChatResponse,
    SessionGetSessionDetailsResponse,
    SessionGetSessionSummaryResponse,
    SessionGetSessionTranscriptsResponse,
    SessionGetSessionParticipantsResponse,
    SessionGetParticipantDataFromPeerIDResponse,
    SessionGetSessionParticipantDetailsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_generate_summary_of_transcripts(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.generate_summary_of_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert session is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_generate_summary_of_transcripts(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.generate_summary_of_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_generate_summary_of_transcripts(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.generate_summary_of_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_generate_summary_of_transcripts(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.generate_summary_of_transcripts(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.generate_summary_of_transcripts(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.generate_summary_of_transcripts(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_participant_data_from_peer_id(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_participant_data_from_peer_id(
            peer_id="peer_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetParticipantDataFromPeerIDResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_participant_data_from_peer_id_with_all_params(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_participant_data_from_peer_id(
            peer_id="peer_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            filters="device_info",
        )
        assert_matches_type(SessionGetParticipantDataFromPeerIDResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_participant_data_from_peer_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.get_participant_data_from_peer_id(
            peer_id="peer_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetParticipantDataFromPeerIDResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_participant_data_from_peer_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.get_participant_data_from_peer_id(
            peer_id="peer_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetParticipantDataFromPeerIDResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_participant_data_from_peer_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_participant_data_from_peer_id(
                peer_id="peer_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_participant_data_from_peer_id(
                peer_id="peer_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_participant_data_from_peer_id(
                peer_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_chat(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_chat(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionChatResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_session_chat(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.get_session_chat(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetSessionChatResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_session_chat(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.get_session_chat(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetSessionChatResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_session_chat(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_chat(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_chat(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_chat(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_details(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_details(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_details_with_all_params(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_details(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            include_breakout_rooms=True,
        )
        assert_matches_type(SessionGetSessionDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_session_details(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.get_session_details(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetSessionDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_session_details(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.get_session_details(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetSessionDetailsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_session_details(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_details(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_details(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_details(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_participant_details(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_participant_details(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            session_id="session_id",
        )
        assert_matches_type(SessionGetSessionParticipantDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_participant_details_with_all_params(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_participant_details(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            session_id="session_id",
            filters="device_info",
            include_peer_events=True,
        )
        assert_matches_type(SessionGetSessionParticipantDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_session_participant_details(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetSessionParticipantDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_session_participant_details(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.get_session_participant_details(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetSessionParticipantDetailsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_session_participant_details(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                session_id="session_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_participants(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_participants(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_participants_with_all_params(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_participants(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            include_peer_events=True,
            page_no=0,
            per_page=0,
            search="search",
            sort_by="joinedAt",
            sort_order="ASC",
            view="raw",
        )
        assert_matches_type(SessionGetSessionParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_session_participants(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.get_session_participants(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetSessionParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_session_participants(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.get_session_participants(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetSessionParticipantsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_session_participants(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_participants(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_participants(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_participants(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_summary(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_summary(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionSummaryResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_session_summary(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.get_session_summary(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetSessionSummaryResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_session_summary(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.get_session_summary(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetSessionSummaryResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_session_summary(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_summary(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_summary(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_summary(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_session_transcripts(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_session_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionTranscriptsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_session_transcripts(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.get_session_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetSessionTranscriptsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_session_transcripts(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.get_session_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetSessionTranscriptsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_session_transcripts(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_transcripts(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_transcripts(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_session_transcripts(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_sessions(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_sessions(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SessionGetSessionsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_sessions_with_all_params(self, client: Cloudflare) -> None:
        session = client.realtime_kit.sessions.get_sessions(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_id="associated_id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_no=0,
            participants="1:10",
            per_page=0,
            search="search",
            sort_by="minutesConsumed",
            sort_order="ASC",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="LIVE",
        )
        assert_matches_type(SessionGetSessionsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_sessions(self, client: Cloudflare) -> None:
        response = client.realtime_kit.sessions.with_raw_response.get_sessions(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetSessionsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_sessions(self, client: Cloudflare) -> None:
        with client.realtime_kit.sessions.with_streaming_response.get_sessions(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetSessionsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_sessions(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_sessions(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.sessions.with_raw_response.get_sessions(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_generate_summary_of_transcripts(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.generate_summary_of_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert session is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_generate_summary_of_transcripts(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.generate_summary_of_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_generate_summary_of_transcripts(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.generate_summary_of_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_generate_summary_of_transcripts(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.generate_summary_of_transcripts(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.generate_summary_of_transcripts(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.generate_summary_of_transcripts(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_participant_data_from_peer_id(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_participant_data_from_peer_id(
            peer_id="peer_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetParticipantDataFromPeerIDResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_participant_data_from_peer_id_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        session = await async_client.realtime_kit.sessions.get_participant_data_from_peer_id(
            peer_id="peer_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            filters="device_info",
        )
        assert_matches_type(SessionGetParticipantDataFromPeerIDResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_participant_data_from_peer_id(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.get_participant_data_from_peer_id(
            peer_id="peer_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetParticipantDataFromPeerIDResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_participant_data_from_peer_id(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.get_participant_data_from_peer_id(
            peer_id="peer_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetParticipantDataFromPeerIDResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_participant_data_from_peer_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_participant_data_from_peer_id(
                peer_id="peer_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_participant_data_from_peer_id(
                peer_id="peer_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `peer_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_participant_data_from_peer_id(
                peer_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_chat(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_chat(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionChatResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_session_chat(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.get_session_chat(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetSessionChatResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_session_chat(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.get_session_chat(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetSessionChatResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_session_chat(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_chat(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_chat(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_chat(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_details(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_details(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_details_with_all_params(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_details(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            include_breakout_rooms=True,
        )
        assert_matches_type(SessionGetSessionDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_session_details(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.get_session_details(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetSessionDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_session_details(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.get_session_details(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetSessionDetailsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_session_details(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_details(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_details(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_details(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_participant_details(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_participant_details(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            session_id="session_id",
        )
        assert_matches_type(SessionGetSessionParticipantDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_participant_details_with_all_params(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_participant_details(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            session_id="session_id",
            filters="device_info",
            include_peer_events=True,
        )
        assert_matches_type(SessionGetSessionParticipantDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_session_participant_details(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetSessionParticipantDetailsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_session_participant_details(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.get_session_participant_details(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetSessionParticipantDetailsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_session_participant_details(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                session_id="session_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_participant_details(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                session_id="session_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_participants(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_participants(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_participants_with_all_params(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_participants(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            include_peer_events=True,
            page_no=0,
            per_page=0,
            search="search",
            sort_by="joinedAt",
            sort_order="ASC",
            view="raw",
        )
        assert_matches_type(SessionGetSessionParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_session_participants(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.get_session_participants(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetSessionParticipantsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_session_participants(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.get_session_participants(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetSessionParticipantsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_session_participants(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_participants(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_participants(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_participants(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_summary(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_summary(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionSummaryResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_session_summary(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.get_session_summary(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetSessionSummaryResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_session_summary(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.get_session_summary(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetSessionSummaryResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_session_summary(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_summary(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_summary(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_summary(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_session_transcripts(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_session_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(SessionGetSessionTranscriptsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_session_transcripts(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.get_session_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetSessionTranscriptsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_session_transcripts(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.get_session_transcripts(
            session_id="session_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetSessionTranscriptsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_session_transcripts(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_transcripts(
                session_id="session_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_transcripts(
                session_id="session_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_session_transcripts(
                session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_sessions(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_sessions(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SessionGetSessionsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_sessions_with_all_params(self, async_client: AsyncCloudflare) -> None:
        session = await async_client.realtime_kit.sessions.get_sessions(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_id="associated_id",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_no=0,
            participants="1:10",
            per_page=0,
            search="search",
            sort_by="minutesConsumed",
            sort_order="ASC",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="LIVE",
        )
        assert_matches_type(SessionGetSessionsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_sessions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.sessions.with_raw_response.get_sessions(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetSessionsResponse, session, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_sessions(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.sessions.with_streaming_response.get_sessions(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetSessionsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_sessions(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_sessions(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.sessions.with_raw_response.get_sessions(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
