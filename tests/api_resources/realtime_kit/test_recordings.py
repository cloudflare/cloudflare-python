# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.realtime_kit import (
    RecordingGetRecordingsResponse,
    RecordingGetOneRecordingResponse,
    RecordingStartRecordingsResponse,
    RecordingGetActiveRecordingsResponse,
    RecordingPauseResumeStopRecordingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecordings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_active_recordings(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.get_active_recordings(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(RecordingGetActiveRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_active_recordings(self, client: Cloudflare) -> None:
        response = client.realtime_kit.recordings.with_raw_response.get_active_recordings(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingGetActiveRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_active_recordings(self, client: Cloudflare) -> None:
        with client.realtime_kit.recordings.with_streaming_response.get_active_recordings(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingGetActiveRecordingsResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_active_recordings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.get_active_recordings(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.get_active_recordings(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.get_active_recordings(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_one_recording(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.get_one_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(RecordingGetOneRecordingResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_one_recording(self, client: Cloudflare) -> None:
        response = client.realtime_kit.recordings.with_raw_response.get_one_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingGetOneRecordingResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_one_recording(self, client: Cloudflare) -> None:
        with client.realtime_kit.recordings.with_streaming_response.get_one_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingGetOneRecordingResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_one_recording(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.get_one_recording(
                recording_id="recording_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.get_one_recording(
                recording_id="recording_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.get_one_recording(
                recording_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_recordings(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.get_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RecordingGetRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_recordings_with_all_params(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.get_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            expired=True,
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_no=0,
            per_page=0,
            search="search",
            sort_by="invokedTime",
            sort_order="ASC",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["INVOKED"],
        )
        assert_matches_type(RecordingGetRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_recordings(self, client: Cloudflare) -> None:
        response = client.realtime_kit.recordings.with_raw_response.get_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingGetRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_recordings(self, client: Cloudflare) -> None:
        with client.realtime_kit.recordings.with_streaming_response.get_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingGetRecordingsResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_recordings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.get_recordings(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.get_recordings(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_pause_resume_stop_recording(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.pause_resume_stop_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="2a95132c15732412d22c1476fa83f27a",
            action="stop",
        )
        assert_matches_type(RecordingPauseResumeStopRecordingResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_pause_resume_stop_recording(self, client: Cloudflare) -> None:
        response = client.realtime_kit.recordings.with_raw_response.pause_resume_stop_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="2a95132c15732412d22c1476fa83f27a",
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingPauseResumeStopRecordingResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_pause_resume_stop_recording(self, client: Cloudflare) -> None:
        with client.realtime_kit.recordings.with_streaming_response.pause_resume_stop_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="2a95132c15732412d22c1476fa83f27a",
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingPauseResumeStopRecordingResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_pause_resume_stop_recording(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.pause_resume_stop_recording(
                recording_id="recording_id",
                account_id="",
                app_id="2a95132c15732412d22c1476fa83f27a",
                action="stop",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.pause_resume_stop_recording(
                recording_id="recording_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                action="stop",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.pause_resume_stop_recording(
                recording_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="2a95132c15732412d22c1476fa83f27a",
                action="stop",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_start_recordings(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.start_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RecordingStartRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_start_recordings_with_all_params(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.start_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allow_multiple_recordings=False,
            audio_config={
                "channel": "stereo",
                "codec": "AAC",
                "export_file": True,
            },
            file_name_prefix="string",
            interactive_config={"type": "ID3"},
            max_seconds=60,
            meeting_id="97440c6a-140b-40a9-9499-b23fd7a3868a",
            realtimekit_bucket_config={"enabled": True},
            rtmp_out_config={"rtmp_url": "rtmp://a.rtmp.youtube.com/live2"},
            storage_config={
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
            url="https://example.com",
            video_config={
                "codec": "H264",
                "export_file": True,
                "height": 720,
                "watermark": {
                    "position": "left top",
                    "size": {
                        "height": 1,
                        "width": 1,
                    },
                    "url": "http://example.com",
                },
                "width": 1280,
            },
        )
        assert_matches_type(RecordingStartRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_start_recordings(self, client: Cloudflare) -> None:
        response = client.realtime_kit.recordings.with_raw_response.start_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert_matches_type(RecordingStartRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_start_recordings(self, client: Cloudflare) -> None:
        with client.realtime_kit.recordings.with_streaming_response.start_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert_matches_type(RecordingStartRecordingsResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_start_recordings(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.start_recordings(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.start_recordings(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_start_track_recording(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.start_track_recording(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            layers={
                "default": {},
                "default-video": {},
            },
            meeting_id="string",
        )
        assert recording is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_start_track_recording_with_all_params(self, client: Cloudflare) -> None:
        recording = client.realtime_kit.recordings.start_track_recording(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            layers={
                "default": {
                    "file_name_prefix": "string",
                    "outputs": [
                        {
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
                            "type": "REALTIMEKIT_BUCKET",
                        }
                    ],
                },
                "default-video": {
                    "file_name_prefix": "string",
                    "outputs": [
                        {
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
                            "type": "REALTIMEKIT_BUCKET",
                        }
                    ],
                },
            },
            meeting_id="string",
            max_seconds=60,
        )
        assert recording is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_start_track_recording(self, client: Cloudflare) -> None:
        response = client.realtime_kit.recordings.with_raw_response.start_track_recording(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            layers={
                "default": {},
                "default-video": {},
            },
            meeting_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = response.parse()
        assert recording is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_start_track_recording(self, client: Cloudflare) -> None:
        with client.realtime_kit.recordings.with_streaming_response.start_track_recording(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            layers={
                "default": {},
                "default-video": {},
            },
            meeting_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = response.parse()
            assert recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_start_track_recording(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.start_track_recording(
                app_id="app_id",
                account_id="",
                layers={
                    "default": {},
                    "default-video": {},
                },
                meeting_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.recordings.with_raw_response.start_track_recording(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                layers={
                    "default": {},
                    "default-video": {},
                },
                meeting_id="string",
            )


class TestAsyncRecordings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_active_recordings(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.get_active_recordings(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(RecordingGetActiveRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_active_recordings(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.recordings.with_raw_response.get_active_recordings(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingGetActiveRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_active_recordings(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.recordings.with_streaming_response.get_active_recordings(
            meeting_id="meeting_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingGetActiveRecordingsResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_active_recordings(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.get_active_recordings(
                meeting_id="meeting_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.get_active_recordings(
                meeting_id="meeting_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.get_active_recordings(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_one_recording(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.get_one_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(RecordingGetOneRecordingResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_one_recording(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.recordings.with_raw_response.get_one_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingGetOneRecordingResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_one_recording(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.recordings.with_streaming_response.get_one_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingGetOneRecordingResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_one_recording(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.get_one_recording(
                recording_id="recording_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.get_one_recording(
                recording_id="recording_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.get_one_recording(
                recording_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_recordings(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.get_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RecordingGetRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_recordings_with_all_params(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.get_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            expired=True,
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_no=0,
            per_page=0,
            search="search",
            sort_by="invokedTime",
            sort_order="ASC",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status=["INVOKED"],
        )
        assert_matches_type(RecordingGetRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_recordings(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.recordings.with_raw_response.get_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingGetRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_recordings(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.recordings.with_streaming_response.get_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingGetRecordingsResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_recordings(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.get_recordings(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.get_recordings(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_pause_resume_stop_recording(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.pause_resume_stop_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="2a95132c15732412d22c1476fa83f27a",
            action="stop",
        )
        assert_matches_type(RecordingPauseResumeStopRecordingResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_pause_resume_stop_recording(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.recordings.with_raw_response.pause_resume_stop_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="2a95132c15732412d22c1476fa83f27a",
            action="stop",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingPauseResumeStopRecordingResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_pause_resume_stop_recording(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.recordings.with_streaming_response.pause_resume_stop_recording(
            recording_id="recording_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="2a95132c15732412d22c1476fa83f27a",
            action="stop",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingPauseResumeStopRecordingResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_pause_resume_stop_recording(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.pause_resume_stop_recording(
                recording_id="recording_id",
                account_id="",
                app_id="2a95132c15732412d22c1476fa83f27a",
                action="stop",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.pause_resume_stop_recording(
                recording_id="recording_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
                action="stop",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `recording_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.pause_resume_stop_recording(
                recording_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="2a95132c15732412d22c1476fa83f27a",
                action="stop",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_start_recordings(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.start_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(RecordingStartRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_start_recordings_with_all_params(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.start_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            allow_multiple_recordings=False,
            audio_config={
                "channel": "stereo",
                "codec": "AAC",
                "export_file": True,
            },
            file_name_prefix="string",
            interactive_config={"type": "ID3"},
            max_seconds=60,
            meeting_id="97440c6a-140b-40a9-9499-b23fd7a3868a",
            realtimekit_bucket_config={"enabled": True},
            rtmp_out_config={"rtmp_url": "rtmp://a.rtmp.youtube.com/live2"},
            storage_config={
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
            url="https://example.com",
            video_config={
                "codec": "H264",
                "export_file": True,
                "height": 720,
                "watermark": {
                    "position": "left top",
                    "size": {
                        "height": 1,
                        "width": 1,
                    },
                    "url": "http://example.com",
                },
                "width": 1280,
            },
        )
        assert_matches_type(RecordingStartRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_start_recordings(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.recordings.with_raw_response.start_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert_matches_type(RecordingStartRecordingsResponse, recording, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_start_recordings(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.recordings.with_streaming_response.start_recordings(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert_matches_type(RecordingStartRecordingsResponse, recording, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_start_recordings(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.start_recordings(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.start_recordings(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_start_track_recording(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.start_track_recording(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            layers={
                "default": {},
                "default-video": {},
            },
            meeting_id="string",
        )
        assert recording is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_start_track_recording_with_all_params(self, async_client: AsyncCloudflare) -> None:
        recording = await async_client.realtime_kit.recordings.start_track_recording(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            layers={
                "default": {
                    "file_name_prefix": "string",
                    "outputs": [
                        {
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
                            "type": "REALTIMEKIT_BUCKET",
                        }
                    ],
                },
                "default-video": {
                    "file_name_prefix": "string",
                    "outputs": [
                        {
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
                            "type": "REALTIMEKIT_BUCKET",
                        }
                    ],
                },
            },
            meeting_id="string",
            max_seconds=60,
        )
        assert recording is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_start_track_recording(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.recordings.with_raw_response.start_track_recording(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            layers={
                "default": {},
                "default-video": {},
            },
            meeting_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recording = await response.parse()
        assert recording is None

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_start_track_recording(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.recordings.with_streaming_response.start_track_recording(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            layers={
                "default": {},
                "default-video": {},
            },
            meeting_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recording = await response.parse()
            assert recording is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_start_track_recording(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.start_track_recording(
                app_id="app_id",
                account_id="",
                layers={
                    "default": {},
                    "default-video": {},
                },
                meeting_id="string",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.recordings.with_raw_response.start_track_recording(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                layers={
                    "default": {},
                    "default-video": {},
                },
                meeting_id="string",
            )
