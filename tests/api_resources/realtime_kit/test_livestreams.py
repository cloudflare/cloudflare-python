# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.realtime_kit import (
    LivestreamGetOrgAnalyticsResponse,
    LivestreamGetAllLivestreamsResponse,
    LivestreamStopLivestreamingAMeetingResponse,
    LivestreamStartLivestreamingAMeetingResponse,
    LivestreamCreateIndependentLivestreamResponse,
    LivestreamGetMeetingActiveLivestreamsResponse,
    LivestreamGetLivestreamAnalyticsCompleteResponse,
    LivestreamGetActiveLivestreamsForLivestreamIDResponse,
    LivestreamGetLivestreamSessionForLivestreamIDResponse,
    LivestreamGetLivestreamSessionDetailsForSessionIDResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLivestreams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_create_independent_livestream(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.create_independent_livestream(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LivestreamCreateIndependentLivestreamResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_create_independent_livestream_with_all_params(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.create_independent_livestream(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="prdmmp-xhycsl",
        )
        assert_matches_type(LivestreamCreateIndependentLivestreamResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_create_independent_livestream(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.create_independent_livestream(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamCreateIndependentLivestreamResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_create_independent_livestream(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.create_independent_livestream(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamCreateIndependentLivestreamResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_create_independent_livestream(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.create_independent_livestream(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.create_independent_livestream(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_active_livestreams_for_livestream_id(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_active_livestreams_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamGetActiveLivestreamsForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_active_livestreams_for_livestream_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.get_active_livestreams_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamGetActiveLivestreamsForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_active_livestreams_for_livestream_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.get_active_livestreams_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamGetActiveLivestreamsForLivestreamIDResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_active_livestreams_for_livestream_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_active_livestreams_for_livestream_id(
                livestream_id="livestream_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_active_livestreams_for_livestream_id(
                livestream_id="livestream_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `livestream_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_active_livestreams_for_livestream_id(
                livestream_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_all_livestreams(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_all_livestreams(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LivestreamGetAllLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_all_livestreams_with_all_params(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_all_livestreams(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            exclude_meetings=True,
            page_no=0,
            per_page=0,
            sort_order="ASC",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="LIVE",
        )
        assert_matches_type(LivestreamGetAllLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_all_livestreams(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.get_all_livestreams(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamGetAllLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_all_livestreams(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.get_all_livestreams(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamGetAllLivestreamsResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_all_livestreams(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_all_livestreams(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_all_livestreams(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_livestream_analytics_complete(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_livestream_analytics_complete(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LivestreamGetLivestreamAnalyticsCompleteResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_livestream_analytics_complete_with_all_params(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_livestream_analytics_complete(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LivestreamGetLivestreamAnalyticsCompleteResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_livestream_analytics_complete(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.get_livestream_analytics_complete(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamGetLivestreamAnalyticsCompleteResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_livestream_analytics_complete(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.get_livestream_analytics_complete(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamGetLivestreamAnalyticsCompleteResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_livestream_analytics_complete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_livestream_analytics_complete(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_livestream_analytics_complete(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_livestream_session_details_for_session_id(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_livestream_session_details_for_session_id(
            livestream_session_id="livestream-session-id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamGetLivestreamSessionDetailsForSessionIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_livestream_session_details_for_session_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.get_livestream_session_details_for_session_id(
            livestream_session_id="livestream-session-id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamGetLivestreamSessionDetailsForSessionIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_livestream_session_details_for_session_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.get_livestream_session_details_for_session_id(
            livestream_session_id="livestream-session-id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(
                LivestreamGetLivestreamSessionDetailsForSessionIDResponse, livestream, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_livestream_session_details_for_session_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_livestream_session_details_for_session_id(
                livestream_session_id="livestream-session-id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_livestream_session_details_for_session_id(
                livestream_session_id="livestream-session-id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `livestream_session_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_livestream_session_details_for_session_id(
                livestream_session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_livestream_session_for_livestream_id(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_livestream_session_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamGetLivestreamSessionForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_livestream_session_for_livestream_id_with_all_params(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_livestream_session_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            page_no=0,
            per_page=0,
        )
        assert_matches_type(LivestreamGetLivestreamSessionForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_livestream_session_for_livestream_id(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.get_livestream_session_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamGetLivestreamSessionForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_livestream_session_for_livestream_id(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.get_livestream_session_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamGetLivestreamSessionForLivestreamIDResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_livestream_session_for_livestream_id(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_livestream_session_for_livestream_id(
                livestream_id="livestream_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_livestream_session_for_livestream_id(
                livestream_id="livestream_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `livestream_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_livestream_session_for_livestream_id(
                livestream_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_meeting_active_livestreams(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_meeting_active_livestreams(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamGetMeetingActiveLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_meeting_active_livestreams(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.get_meeting_active_livestreams(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamGetMeetingActiveLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_meeting_active_livestreams(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.get_meeting_active_livestreams(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamGetMeetingActiveLivestreamsResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_meeting_active_livestreams(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_meeting_active_livestreams(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_meeting_active_livestreams(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_meeting_active_livestreams(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_org_analytics(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LivestreamGetOrgAnalyticsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_get_org_analytics_with_all_params(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_date="2022-09-22",
            start_date="2022-09-01",
        )
        assert_matches_type(LivestreamGetOrgAnalyticsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_get_org_analytics(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamGetOrgAnalyticsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_get_org_analytics(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamGetOrgAnalyticsResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_get_org_analytics(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_org_analytics(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.get_org_analytics(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_start_livestreaming_a_meeting(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.start_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamStartLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_start_livestreaming_a_meeting_with_all_params(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.start_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            name="prdmmp-xhycsl",
            video_config={
                "height": 0,
                "width": 0,
            },
        )
        assert_matches_type(LivestreamStartLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_start_livestreaming_a_meeting(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.start_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamStartLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_start_livestreaming_a_meeting(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.start_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamStartLivestreamingAMeetingResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_start_livestreaming_a_meeting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.start_livestreaming_a_meeting(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.start_livestreaming_a_meeting(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.start_livestreaming_a_meeting(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_method_stop_livestreaming_a_meeting(self, client: Cloudflare) -> None:
        livestream = client.realtime_kit.livestreams.stop_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamStopLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_raw_response_stop_livestreaming_a_meeting(self, client: Cloudflare) -> None:
        response = client.realtime_kit.livestreams.with_raw_response.stop_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = response.parse()
        assert_matches_type(LivestreamStopLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_streaming_response_stop_livestreaming_a_meeting(self, client: Cloudflare) -> None:
        with client.realtime_kit.livestreams.with_streaming_response.stop_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = response.parse()
            assert_matches_type(LivestreamStopLivestreamingAMeetingResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    def test_path_params_stop_livestreaming_a_meeting(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.stop_livestreaming_a_meeting(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.stop_livestreaming_a_meeting(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            client.realtime_kit.livestreams.with_raw_response.stop_livestreaming_a_meeting(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )


class TestAsyncLivestreams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_create_independent_livestream(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.create_independent_livestream(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LivestreamCreateIndependentLivestreamResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_create_independent_livestream_with_all_params(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.create_independent_livestream(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            name="prdmmp-xhycsl",
        )
        assert_matches_type(LivestreamCreateIndependentLivestreamResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_create_independent_livestream(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.livestreams.with_raw_response.create_independent_livestream(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamCreateIndependentLivestreamResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_create_independent_livestream(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.livestreams.with_streaming_response.create_independent_livestream(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamCreateIndependentLivestreamResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_create_independent_livestream(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.create_independent_livestream(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.create_independent_livestream(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_active_livestreams_for_livestream_id(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_active_livestreams_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamGetActiveLivestreamsForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_active_livestreams_for_livestream_id(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.realtime_kit.livestreams.with_raw_response.get_active_livestreams_for_livestream_id(
                livestream_id="livestream_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamGetActiveLivestreamsForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_active_livestreams_for_livestream_id(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with (
            async_client.realtime_kit.livestreams.with_streaming_response.get_active_livestreams_for_livestream_id(
                livestream_id="livestream_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamGetActiveLivestreamsForLivestreamIDResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_active_livestreams_for_livestream_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_active_livestreams_for_livestream_id(
                livestream_id="livestream_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_active_livestreams_for_livestream_id(
                livestream_id="livestream_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `livestream_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_active_livestreams_for_livestream_id(
                livestream_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_all_livestreams(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_all_livestreams(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LivestreamGetAllLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_all_livestreams_with_all_params(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_all_livestreams(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            exclude_meetings=True,
            page_no=0,
            per_page=0,
            sort_order="ASC",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="LIVE",
        )
        assert_matches_type(LivestreamGetAllLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_all_livestreams(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.livestreams.with_raw_response.get_all_livestreams(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamGetAllLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_all_livestreams(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.livestreams.with_streaming_response.get_all_livestreams(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamGetAllLivestreamsResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_all_livestreams(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_all_livestreams(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_all_livestreams(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_livestream_analytics_complete(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_livestream_analytics_complete(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LivestreamGetLivestreamAnalyticsCompleteResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_livestream_analytics_complete_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_livestream_analytics_complete(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(LivestreamGetLivestreamAnalyticsCompleteResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_livestream_analytics_complete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_analytics_complete(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamGetLivestreamAnalyticsCompleteResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_livestream_analytics_complete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.livestreams.with_streaming_response.get_livestream_analytics_complete(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamGetLivestreamAnalyticsCompleteResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_livestream_analytics_complete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_analytics_complete(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_analytics_complete(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_livestream_session_details_for_session_id(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_livestream_session_details_for_session_id(
            livestream_session_id="livestream-session-id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamGetLivestreamSessionDetailsForSessionIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_livestream_session_details_for_session_id(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_session_details_for_session_id(
                livestream_session_id="livestream-session-id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamGetLivestreamSessionDetailsForSessionIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_livestream_session_details_for_session_id(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with (
            async_client.realtime_kit.livestreams.with_streaming_response.get_livestream_session_details_for_session_id(
                livestream_session_id="livestream-session-id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(
                LivestreamGetLivestreamSessionDetailsForSessionIDResponse, livestream, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_livestream_session_details_for_session_id(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_session_details_for_session_id(
                livestream_session_id="livestream-session-id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_session_details_for_session_id(
                livestream_session_id="livestream-session-id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `livestream_session_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_session_details_for_session_id(
                livestream_session_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_livestream_session_for_livestream_id(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_livestream_session_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamGetLivestreamSessionForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_livestream_session_for_livestream_id_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_livestream_session_for_livestream_id(
            livestream_id="livestream_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            page_no=0,
            per_page=0,
        )
        assert_matches_type(LivestreamGetLivestreamSessionForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_livestream_session_for_livestream_id(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_session_for_livestream_id(
                livestream_id="livestream_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamGetLivestreamSessionForLivestreamIDResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_livestream_session_for_livestream_id(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with (
            async_client.realtime_kit.livestreams.with_streaming_response.get_livestream_session_for_livestream_id(
                livestream_id="livestream_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamGetLivestreamSessionForLivestreamIDResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_livestream_session_for_livestream_id(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_session_for_livestream_id(
                livestream_id="livestream_id",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_session_for_livestream_id(
                livestream_id="livestream_id",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `livestream_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_livestream_session_for_livestream_id(
                livestream_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_meeting_active_livestreams(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_meeting_active_livestreams(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamGetMeetingActiveLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_meeting_active_livestreams(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.livestreams.with_raw_response.get_meeting_active_livestreams(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamGetMeetingActiveLivestreamsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_meeting_active_livestreams(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.livestreams.with_streaming_response.get_meeting_active_livestreams(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamGetMeetingActiveLivestreamsResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_meeting_active_livestreams(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_meeting_active_livestreams(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_meeting_active_livestreams(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_meeting_active_livestreams(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_org_analytics(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(LivestreamGetOrgAnalyticsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_get_org_analytics_with_all_params(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            end_date="2022-09-22",
            start_date="2022-09-01",
        )
        assert_matches_type(LivestreamGetOrgAnalyticsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_get_org_analytics(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.livestreams.with_raw_response.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamGetOrgAnalyticsResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_get_org_analytics(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.livestreams.with_streaming_response.get_org_analytics(
            app_id="app_id",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamGetOrgAnalyticsResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_get_org_analytics(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_org_analytics(
                app_id="app_id",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.get_org_analytics(
                app_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_start_livestreaming_a_meeting(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.start_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamStartLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_start_livestreaming_a_meeting_with_all_params(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.start_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
            name="prdmmp-xhycsl",
            video_config={
                "height": 0,
                "width": 0,
            },
        )
        assert_matches_type(LivestreamStartLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_start_livestreaming_a_meeting(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.livestreams.with_raw_response.start_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamStartLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_start_livestreaming_a_meeting(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.livestreams.with_streaming_response.start_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamStartLivestreamingAMeetingResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_start_livestreaming_a_meeting(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.start_livestreaming_a_meeting(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.start_livestreaming_a_meeting(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.start_livestreaming_a_meeting(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_method_stop_livestreaming_a_meeting(self, async_client: AsyncCloudflare) -> None:
        livestream = await async_client.realtime_kit.livestreams.stop_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )
        assert_matches_type(LivestreamStopLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_raw_response_stop_livestreaming_a_meeting(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.realtime_kit.livestreams.with_raw_response.stop_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        livestream = await response.parse()
        assert_matches_type(LivestreamStopLivestreamingAMeetingResponse, livestream, path=["response"])

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_streaming_response_stop_livestreaming_a_meeting(self, async_client: AsyncCloudflare) -> None:
        async with async_client.realtime_kit.livestreams.with_streaming_response.stop_livestreaming_a_meeting(
            meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            livestream = await response.parse()
            assert_matches_type(LivestreamStopLivestreamingAMeetingResponse, livestream, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: HTTP 401 from prism, support api tokens")
    @parametrize
    async def test_path_params_stop_livestreaming_a_meeting(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.stop_livestreaming_a_meeting(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                app_id="app_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.stop_livestreaming_a_meeting(
                meeting_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `meeting_id` but received ''"):
            await async_client.realtime_kit.livestreams.with_raw_response.stop_livestreaming_a_meeting(
                meeting_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                app_id="app_id",
            )
