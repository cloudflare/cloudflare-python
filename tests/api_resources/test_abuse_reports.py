# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAbuseReports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_overload_3(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Cloudflare) -> None:
        response = client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Cloudflare) -> None:
        with client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_create_overload_3(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_overload_4(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Cloudflare) -> None:
        response = client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Cloudflare) -> None:
        with client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_create_overload_4(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_overload_5(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Cloudflare) -> None:
        response = client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Cloudflare) -> None:
        with client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_create_overload_5(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_overload_6(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Cloudflare) -> None:
        response = client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Cloudflare) -> None:
        with client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_create_overload_6(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_overload_7(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Cloudflare) -> None:
        response = client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Cloudflare) -> None:
        with client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_create_overload_7(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_overload_8(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Cloudflare) -> None:
        abuse_report = client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Cloudflare) -> None:
        response = client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Cloudflare) -> None:
        with client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    def test_path_params_create_overload_8(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )


class TestAsyncAbuseReports:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = await response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = await response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = await response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = await response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = await response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = await response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_create_overload_3(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = await response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = await response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_create_overload_4(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = await response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = await response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_create_overload_5(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = await response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = await response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_create_overload_6(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = await response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = await response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_create_overload_7(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncCloudflare) -> None:
        abuse_report = await async_client.abuse_reports.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
            address1="x",
            agent_name="x",
            agree=0,
            city="x",
            comments="x",
            company="x",
            country="x",
            destination_ips="destination_ips",
            host_notification="send",
            justification="x",
            ncmec_notification="send",
            ncsei_subject_representation=True,
            original_work="x",
            owner_notification="send",
            ports_protocols="ports_protocols",
            reported_country="xx",
            reported_user_agent="x",
            signature="signature",
            source_ips="source_ips",
            state="x",
            tele="x",
            title="x",
            trademark_number="x",
            trademark_office="x",
            trademark_symbol="x",
        )
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.abuse_reports.with_raw_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        abuse_report = await response.parse()
        assert_matches_type(str, abuse_report, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        async with async_client.abuse_reports.with_streaming_response.create(
            report_type="abuse_general",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            act="abuse_general",
            email="email",
            email2="email2",
            name="x",
            urls="urls",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            abuse_report = await response.parse()
            assert_matches_type(str, abuse_report, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate unauthorized HTTP response")
    @parametrize
    async def test_path_params_create_overload_8(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.abuse_reports.with_raw_response.create(
                report_type="abuse_general",
                account_id="",
                act="abuse_general",
                email="email",
                email2="email2",
                name="x",
                urls="urls",
            )
