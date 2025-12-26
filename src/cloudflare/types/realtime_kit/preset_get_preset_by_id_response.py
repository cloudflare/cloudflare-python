# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "PresetGetPresetByIDResponse",
    "Data",
    "DataConfig",
    "DataConfigMaxVideoStreams",
    "DataConfigMedia",
    "DataConfigMediaScreenshare",
    "DataConfigMediaVideo",
    "DataConfigMediaAudio",
    "DataUI",
    "DataUIDesignTokens",
    "DataUIDesignTokensColors",
    "DataUIDesignTokensColorsBackground",
    "DataUIDesignTokensColorsBrand",
    "DataPermissions",
    "DataPermissionsChat",
    "DataPermissionsChatPrivate",
    "DataPermissionsChatPublic",
    "DataPermissionsConnectedMeetings",
    "DataPermissionsMedia",
    "DataPermissionsMediaAudio",
    "DataPermissionsMediaScreenshare",
    "DataPermissionsMediaVideo",
    "DataPermissionsPlugins",
    "DataPermissionsPluginsConfig",
    "DataPermissionsPluginsConfigUnionMember1",
    "DataPermissionsPolls",
]


class DataConfigMaxVideoStreams(BaseModel):
    """Maximum number of streams that are visible on a device"""

    desktop: int
    """Maximum number of video streams visible on desktop devices"""

    mobile: int
    """Maximum number of streams visible on mobile devices"""


class DataConfigMediaScreenshare(BaseModel):
    """Configuration options for participant screen shares"""

    frame_rate: int
    """Frame rate of screen share"""

    quality: Literal["hd", "vga", "qvga"]
    """Quality of screen share"""


class DataConfigMediaVideo(BaseModel):
    """Configuration options for participant videos"""

    frame_rate: int
    """Frame rate of participants' video"""

    quality: Literal["hd", "vga", "qvga"]
    """Video quality of participants"""


class DataConfigMediaAudio(BaseModel):
    """Control options for Audio quality."""

    enable_high_bitrate: Optional[bool] = None
    """Enable High Quality Audio for your meetings"""

    enable_stereo: Optional[bool] = None
    """Enable Stereo for your meetings"""


class DataConfigMedia(BaseModel):
    """Media configuration options. eg: Video quality"""

    screenshare: DataConfigMediaScreenshare
    """Configuration options for participant screen shares"""

    video: DataConfigMediaVideo
    """Configuration options for participant videos"""

    audio: Optional[DataConfigMediaAudio] = None
    """Control options for Audio quality."""


class DataConfig(BaseModel):
    max_screenshare_count: int
    """Maximum number of screen shares that can be active at a given time"""

    max_video_streams: DataConfigMaxVideoStreams
    """Maximum number of streams that are visible on a device"""

    media: DataConfigMedia
    """Media configuration options. eg: Video quality"""

    view_type: Literal["GROUP_CALL", "WEBINAR", "AUDIO_ROOM"]
    """Type of the meeting"""


class DataUIDesignTokensColorsBackground(BaseModel):
    api_1000: str = FieldInfo(alias="1000")

    api_600: str = FieldInfo(alias="600")

    api_700: str = FieldInfo(alias="700")

    api_800: str = FieldInfo(alias="800")

    api_900: str = FieldInfo(alias="900")


class DataUIDesignTokensColorsBrand(BaseModel):
    api_300: str = FieldInfo(alias="300")

    api_400: str = FieldInfo(alias="400")

    api_500: str = FieldInfo(alias="500")

    api_600: str = FieldInfo(alias="600")

    api_700: str = FieldInfo(alias="700")


class DataUIDesignTokensColors(BaseModel):
    background: DataUIDesignTokensColorsBackground

    brand: DataUIDesignTokensColorsBrand

    danger: str

    success: str

    text: str

    text_on_brand: str

    video_bg: str

    warning: str


class DataUIDesignTokens(BaseModel):
    border_radius: Literal["rounded"]

    border_width: Literal["thin"]

    colors: DataUIDesignTokensColors

    logo: str

    spacing_base: float

    theme: Literal["dark"]


class DataUI(BaseModel):
    design_tokens: DataUIDesignTokens

    config_diff: Optional[object] = None


class DataPermissionsChatPrivate(BaseModel):
    can_receive: bool

    can_send: bool

    files: bool

    text: bool


class DataPermissionsChatPublic(BaseModel):
    can_send: bool
    """Can send messages in general"""

    files: bool
    """Can send file messages"""

    text: bool
    """Can send text messages"""


class DataPermissionsChat(BaseModel):
    """Chat permissions"""

    private: DataPermissionsChatPrivate

    public: DataPermissionsChatPublic


class DataPermissionsConnectedMeetings(BaseModel):
    can_alter_connected_meetings: bool

    can_switch_connected_meetings: bool

    can_switch_to_parent_meeting: bool


class DataPermissionsMediaAudio(BaseModel):
    """Audio permissions"""

    can_produce: Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]
    """Can produce audio"""


class DataPermissionsMediaScreenshare(BaseModel):
    """Screenshare permissions"""

    can_produce: Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]
    """Can produce screen share video"""


class DataPermissionsMediaVideo(BaseModel):
    """Video permissions"""

    can_produce: Literal["ALLOWED", "NOT_ALLOWED", "CAN_REQUEST"]
    """Can produce video"""


class DataPermissionsMedia(BaseModel):
    """Media permissions"""

    audio: DataPermissionsMediaAudio
    """Audio permissions"""

    screenshare: DataPermissionsMediaScreenshare
    """Screenshare permissions"""

    video: DataPermissionsMediaVideo
    """Video permissions"""


class DataPermissionsPluginsConfigUnionMember1(BaseModel):
    access_control: Literal["FULL_ACCESS", "VIEW_ONLY"]

    handles_view_only: bool


DataPermissionsPluginsConfig: TypeAlias = Union[str, DataPermissionsPluginsConfigUnionMember1]


class DataPermissionsPlugins(BaseModel):
    """Plugin permissions"""

    can_close: bool
    """Can close plugins that are already open"""

    can_edit_config: bool
    """Can edit plugin config"""

    can_start: bool
    """Can start plugins"""

    config: DataPermissionsPluginsConfig


class DataPermissionsPolls(BaseModel):
    """Poll permissions"""

    can_create: bool
    """Can create polls"""

    can_view: bool
    """Can view polls"""

    can_vote: bool
    """Can vote on polls"""


class DataPermissions(BaseModel):
    accept_waiting_requests: bool
    """Whether this participant can accept waiting requests"""

    can_accept_production_requests: bool

    can_change_participant_permissions: bool

    can_edit_display_name: bool

    can_livestream: bool

    can_record: bool

    can_spotlight: bool

    chat: DataPermissionsChat
    """Chat permissions"""

    connected_meetings: DataPermissionsConnectedMeetings

    disable_participant_audio: bool

    disable_participant_screensharing: bool

    disable_participant_video: bool

    hidden_participant: bool
    """Whether this participant is visible to others or not"""

    kick_participant: bool

    media: DataPermissionsMedia
    """Media permissions"""

    pin_participant: bool

    plugins: DataPermissionsPlugins
    """Plugin permissions"""

    polls: DataPermissionsPolls
    """Poll permissions"""

    recorder_type: Literal["RECORDER", "LIVESTREAMER", "NONE"]
    """Type of the recording peer"""

    show_participant_list: bool

    waiting_room_type: Literal["SKIP", "ON_PRIVILEGED_USER_ENTRY", "SKIP_ON_ACCEPT"]
    """Waiting room type"""

    is_recorder: Optional[bool] = None


class Data(BaseModel):
    """Data returned by the operation"""

    id: str
    """ID of the preset"""

    config: DataConfig

    name: str
    """Name of the preset"""

    ui: DataUI

    permissions: Optional[DataPermissions] = None


class PresetGetPresetByIDResponse(BaseModel):
    data: Data
    """Data returned by the operation"""

    success: bool
    """Success status of the operation"""
