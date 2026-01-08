# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.realtime_kit import (
    MeetingGetResponse,
    MeetingCreateResponse,
    MeetingAddParticipantResponse,
    MeetingGetMeetingByIDResponse,
    MeetingEditParticipantResponse,
    MeetingUpdateMeetingByIDResponse,
    MeetingReplaceMeetingByIDResponse,
    MeetingGetMeetingParticipantResponse,
    MeetingGetMeetingParticipantsResponse,
    MeetingRefreshParticipantTokenResponse,
    MeetingDeleteMeetingParticipantResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMeetings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MeetingCreateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ai_config={
                "summarization": {
                    "summary_type": "general",
                    "text_format": "plain_text",
                    "word_limit": 150,
                },
                "transcription": {
                    "keywords": ["string"],
                    "language": "en-US",
                    "profanity_filter": True,
                },
            },
            live_stream_on_start=True,
            persist_chat=True,
            record_on_start=True,
            recording_config={
                "audio_config": {
                    "channel": "mono",
                    "codec": "MP3",
                    "export_file": True,
                },
                "file_name_prefix": "file_name_prefix",
                "live_streaming_config": {"rtmp_url": "rtmp://a.rtmp.youtube.com/live2"},
                "max_seconds": 60,
                "realtimekit_bucket_config": {"enabled": True},
                "storage_config": {
                    "type": "aws",
                    "access_key": "access_key",
                    "auth_method": "KEY",
                    "bucket": "bucket",
                    "host": "host",
                    "password": "password",
                    "path": "path",
                    "port": 0,
                    "private_key": "private_key",
                    "region": "us-east-1",
                    "secret": "secret",
                    "username": "username",
                },
                "video_config": {
                    "codec": "H264",
                    "export_file": True,
                    "height": 720,
                    "watermark": {
                        "position": "left top",
                        "size": {
                            "height": 1,
                            "width": 1,
                        },
                        "url": "https://example.com",
                    },
                    "width": 1280,
                },
            },
            session_keep_alive_time_in_secs=60,
            summarize_on_end=True,
            title="title",
        )
        assert_matches_type(MeetingCreateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingCreateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingCreateResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.create(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.create(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_add_participant(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.add_participant(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_id="custom_participant_id",
            preset_name="preset_name",
        )
        assert_matches_type(MeetingAddParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_add_participant_with_all_params(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.add_participant(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_id="custom_participant_id",
            preset_name="preset_name",
            name="Mary Sue",
            picture="https://i.imgur.com/test.jpg",
        )
        assert_matches_type(MeetingAddParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_add_participant(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.add_participant(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_id="custom_participant_id",
            preset_name="preset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingAddParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_add_participant(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.add_participant(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_id="custom_participant_id",
            preset_name="preset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingAddParticipantResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_add_participant(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.add_participant(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
                custom_participant_id="custom_participant_id",
                preset_name="preset_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.add_participant(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                custom_participant_id="custom_participant_id",
                preset_name="preset_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.add_participant(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                custom_participant_id="custom_participant_id",
                preset_name="preset_name",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_delete_meeting_participant(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.delete_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MeetingDeleteMeetingParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_delete_meeting_participant(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingDeleteMeetingParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_delete_meeting_participant(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.delete_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingDeleteMeetingParticipantResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_delete_meeting_participant(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_edit_participant(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.edit_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MeetingEditParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_edit_participant_with_all_params(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.edit_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Jane Doe",
            picture="https://example.com",
            preset_name="preset_name",
        )
        assert_matches_type(MeetingEditParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_edit_participant(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.edit_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingEditParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_edit_participant(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.edit_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingEditParticipantResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_edit_participant(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.edit_participant(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.edit_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.edit_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.edit_participant(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MeetingGetResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_no=0,
            per_page=0,
            search="search",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MeetingGetResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingGetResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingGetResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_meeting_by_id(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.get_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(MeetingGetMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_meeting_by_id_with_all_params(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.get_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            name="name",
        )
        assert_matches_type(MeetingGetMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_meeting_by_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.get_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingGetMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_meeting_by_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.get_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingGetMeetingByIDResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_meeting_by_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_by_id(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_meeting_participant(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.get_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MeetingGetMeetingParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_meeting_participant(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingGetMeetingParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_meeting_participant(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.get_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingGetMeetingParticipantResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_meeting_participant(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_meeting_participants(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.get_meeting_participants(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(MeetingGetMeetingParticipantsResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_meeting_participants_with_all_params(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.get_meeting_participants(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            page_no=0,
            per_page=0,
        )
        assert_matches_type(MeetingGetMeetingParticipantsResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_meeting_participants(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.get_meeting_participants(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingGetMeetingParticipantsResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_meeting_participants(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.get_meeting_participants(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingGetMeetingParticipantsResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_meeting_participants(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_participants(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_participants(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.get_meeting_participants(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_refresh_participant_token(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.refresh_participant_token(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MeetingRefreshParticipantTokenResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_refresh_participant_token(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingRefreshParticipantTokenResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_refresh_participant_token(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.refresh_participant_token(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingRefreshParticipantTokenResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_refresh_participant_token(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_replace_meeting_by_id(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.replace_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(MeetingReplaceMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_replace_meeting_by_id_with_all_params(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.replace_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            ai_config={
                "summarization": {
                    "summary_type": "general",
                    "text_format": "plain_text",
                    "word_limit": 150,
                },
                "transcription": {
                    "keywords": ["string"],
                    "language": "en-US",
                    "profanity_filter": True,
                },
            },
            live_stream_on_start=True,
            persist_chat=True,
            record_on_start=True,
            recording_config={
                "audio_config": {
                    "channel": "mono",
                    "codec": "MP3",
                    "export_file": True,
                },
                "file_name_prefix": "file_name_prefix",
                "live_streaming_config": {"rtmp_url": "rtmp://a.rtmp.youtube.com/live2"},
                "max_seconds": 60,
                "realtimekit_bucket_config": {"enabled": True},
                "storage_config": {
                    "type": "aws",
                    "access_key": "access_key",
                    "auth_method": "KEY",
                    "bucket": "bucket",
                    "host": "host",
                    "password": "password",
                    "path": "path",
                    "port": 0,
                    "private_key": "private_key",
                    "region": "us-east-1",
                    "secret": "secret",
                    "username": "username",
                },
                "video_config": {
                    "codec": "H264",
                    "export_file": True,
                    "height": 720,
                    "watermark": {
                        "position": "left top",
                        "size": {
                            "height": 1,
                            "width": 1,
                        },
                        "url": "https://example.com",
                    },
                    "width": 1280,
                },
            },
            session_keep_alive_time_in_secs=60,
            summarize_on_end=True,
            title="title",
        )
        assert_matches_type(MeetingReplaceMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_replace_meeting_by_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.replace_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingReplaceMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_replace_meeting_by_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.replace_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingReplaceMeetingByIDResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_replace_meeting_by_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.replace_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.replace_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.replace_meeting_by_id(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_update_meeting_by_id(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.update_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(MeetingUpdateMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_update_meeting_by_id_with_all_params(self, client: Cloudflare) -> None:
        meeting = client.realtime_kit.meetings.update_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            ai_config={
                "summarization": {
                    "summary_type": "general",
                    "text_format": "plain_text",
                    "word_limit": 150,
                },
                "transcription": {
                    "keywords": ["string"],
                    "language": "en-US",
                    "profanity_filter": True,
                },
            },
            live_stream_on_start=True,
            persist_chat=True,
            record_on_start=True,
            session_keep_alive_time_in_secs=60,
            status="INACTIVE",
            summarize_on_end=True,
            title="title",
        )
        assert_matches_type(MeetingUpdateMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_update_meeting_by_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.meetings.with_raw_response.update_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = response.parse()
        assert_matches_type(MeetingUpdateMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_update_meeting_by_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.meetings.with_streaming_response.update_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = response.parse()
            assert_matches_type(MeetingUpdateMeetingByIDResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_update_meeting_by_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.update_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.update_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.meetings.with_raw_response.update_meeting_by_id(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )


class TestAsyncMeetings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MeetingCreateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            ai_config={
                "summarization": {
                    "summary_type": "general",
                    "text_format": "plain_text",
                    "word_limit": 150,
                },
                "transcription": {
                    "keywords": ["string"],
                    "language": "en-US",
                    "profanity_filter": True,
                },
            },
            live_stream_on_start=True,
            persist_chat=True,
            record_on_start=True,
            recording_config={
                "audio_config": {
                    "channel": "mono",
                    "codec": "MP3",
                    "export_file": True,
                },
                "file_name_prefix": "file_name_prefix",
                "live_streaming_config": {"rtmp_url": "rtmp://a.rtmp.youtube.com/live2"},
                "max_seconds": 60,
                "realtimekit_bucket_config": {"enabled": True},
                "storage_config": {
                    "type": "aws",
                    "access_key": "access_key",
                    "auth_method": "KEY",
                    "bucket": "bucket",
                    "host": "host",
                    "password": "password",
                    "path": "path",
                    "port": 0,
                    "private_key": "private_key",
                    "region": "us-east-1",
                    "secret": "secret",
                    "username": "username",
                },
                "video_config": {
                    "codec": "H264",
                    "export_file": True,
                    "height": 720,
                    "watermark": {
                        "position": "left top",
                        "size": {
                            "height": 1,
                            "width": 1,
                        },
                        "url": "https://example.com",
                    },
                    "width": 1280,
                },
            },
            session_keep_alive_time_in_secs=60,
            summarize_on_end=True,
            title="title",
        )
        assert_matches_type(MeetingCreateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingCreateResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.create(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingCreateResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.create(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.create(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_add_participant(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.add_participant(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_id="custom_participant_id",
            preset_name="preset_name",
        )
        assert_matches_type(MeetingAddParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_add_participant_with_all_params(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.add_participant(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_id="custom_participant_id",
            preset_name="preset_name",
            name="Mary Sue",
            picture="https://i.imgur.com/test.jpg",
        )
        assert_matches_type(MeetingAddParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_add_participant(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.add_participant(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_id="custom_participant_id",
            preset_name="preset_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingAddParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_add_participant(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.add_participant(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            custom_participant_id="custom_participant_id",
            preset_name="preset_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingAddParticipantResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_add_participant(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.add_participant(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
                custom_participant_id="custom_participant_id",
                preset_name="preset_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.add_participant(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                custom_participant_id="custom_participant_id",
                preset_name="preset_name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.add_participant(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                custom_participant_id="custom_participant_id",
                preset_name="preset_name",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_delete_meeting_participant(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.delete_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MeetingDeleteMeetingParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_delete_meeting_participant(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingDeleteMeetingParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_delete_meeting_participant(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.delete_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingDeleteMeetingParticipantResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_delete_meeting_participant(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.delete_meeting_participant(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_edit_participant(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.edit_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MeetingEditParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_edit_participant_with_all_params(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.edit_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Jane Doe",
            picture="https://example.com",
            preset_name="preset_name",
        )
        assert_matches_type(MeetingEditParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_edit_participant(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.edit_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingEditParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_edit_participant(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.edit_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingEditParticipantResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_edit_participant(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.edit_participant(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.edit_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.edit_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.edit_participant(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MeetingGetResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            page_no=0,
            per_page=0,
            search="search",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(MeetingGetResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingGetResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.get(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingGetResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.get_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(MeetingGetMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_meeting_by_id_with_all_params(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.get_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            name="name",
        )
        assert_matches_type(MeetingGetMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.get_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingGetMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.get_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingGetMeetingByIDResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_by_id(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_meeting_participant(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.get_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MeetingGetMeetingParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_meeting_participant(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingGetMeetingParticipantResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_meeting_participant(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.get_meeting_participant(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingGetMeetingParticipantResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_meeting_participant(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participant(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_meeting_participants(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.get_meeting_participants(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(MeetingGetMeetingParticipantsResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_meeting_participants_with_all_params(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.get_meeting_participants(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            page_no=0,
            per_page=0,
        )
        assert_matches_type(MeetingGetMeetingParticipantsResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_meeting_participants(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participants(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingGetMeetingParticipantsResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_meeting_participants(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.get_meeting_participants(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingGetMeetingParticipantsResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_meeting_participants(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participants(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participants(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.get_meeting_participants(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_refresh_participant_token(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.refresh_participant_token(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MeetingRefreshParticipantTokenResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_refresh_participant_token(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingRefreshParticipantTokenResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_refresh_participant_token(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.refresh_participant_token(
            participant_id="participant_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingRefreshParticipantTokenResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_refresh_participant_token(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
                participant_id="participant_id",
                account_id="",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
                participant_id="participant_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `participant_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.refresh_participant_token(
                participant_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_replace_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.replace_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(MeetingReplaceMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_replace_meeting_by_id_with_all_params(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.replace_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            ai_config={
                "summarization": {
                    "summary_type": "general",
                    "text_format": "plain_text",
                    "word_limit": 150,
                },
                "transcription": {
                    "keywords": ["string"],
                    "language": "en-US",
                    "profanity_filter": True,
                },
            },
            live_stream_on_start=True,
            persist_chat=True,
            record_on_start=True,
            recording_config={
                "audio_config": {
                    "channel": "mono",
                    "codec": "MP3",
                    "export_file": True,
                },
                "file_name_prefix": "file_name_prefix",
                "live_streaming_config": {"rtmp_url": "rtmp://a.rtmp.youtube.com/live2"},
                "max_seconds": 60,
                "realtimekit_bucket_config": {"enabled": True},
                "storage_config": {
                    "type": "aws",
                    "access_key": "access_key",
                    "auth_method": "KEY",
                    "bucket": "bucket",
                    "host": "host",
                    "password": "password",
                    "path": "path",
                    "port": 0,
                    "private_key": "private_key",
                    "region": "us-east-1",
                    "secret": "secret",
                    "username": "username",
                },
                "video_config": {
                    "codec": "H264",
                    "export_file": True,
                    "height": 720,
                    "watermark": {
                        "position": "left top",
                        "size": {
                            "height": 1,
                            "width": 1,
                        },
                        "url": "https://example.com",
                    },
                    "width": 1280,
                },
            },
            session_keep_alive_time_in_secs=60,
            summarize_on_end=True,
            title="title",
        )
        assert_matches_type(MeetingReplaceMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_replace_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.replace_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingReplaceMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_replace_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.replace_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingReplaceMeetingByIDResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_replace_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.replace_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.replace_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.replace_meeting_by_id(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_update_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.update_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(MeetingUpdateMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_update_meeting_by_id_with_all_params(self, async_client: AsyncCloudflare) -> None:
        meeting = await async_client.realtime_kit.meetings.update_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            ai_config={
                "summarization": {
                    "summary_type": "general",
                    "text_format": "plain_text",
                    "word_limit": 150,
                },
                "transcription": {
                    "keywords": ["string"],
                    "language": "en-US",
                    "profanity_filter": True,
                },
            },
            live_stream_on_start=True,
            persist_chat=True,
            record_on_start=True,
            session_keep_alive_time_in_secs=60,
            status="INACTIVE",
            summarize_on_end=True,
            title="title",
        )
        assert_matches_type(MeetingUpdateMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_update_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.meetings.with_raw_response.update_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        meeting = await response.parse()
        assert_matches_type(MeetingUpdateMeetingByIDResponse, meeting, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_update_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.meetings.with_streaming_response.update_meeting_by_id(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            meeting = await response.parse()
            assert_matches_type(MeetingUpdateMeetingByIDResponse, meeting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_update_meeting_by_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.update_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.update_meeting_by_id(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.meetings.with_raw_response.update_meeting_by_id(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
