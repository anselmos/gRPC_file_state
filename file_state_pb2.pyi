"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ExistsInStateRequest(google.protobuf.message.Message):
    """The request message containing file path"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PATH_FIELD_NUMBER: builtins.int
    path: builtins.str
    def __init__(
        self,
        *,
        path: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["path", b"path"]) -> None: ...

global___ExistsInStateRequest = ExistsInStateRequest

class ExistsInStateResponse(google.protobuf.message.Message):
    """The response message returning if file is present in"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXISTS_FIELD_NUMBER: builtins.int
    exists: builtins.bool
    def __init__(
        self,
        *,
        exists: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["exists", b"exists"]) -> None: ...

global___ExistsInStateResponse = ExistsInStateResponse
