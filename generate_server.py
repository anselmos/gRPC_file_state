from grpc_tools import protoc

protoc.main((
    '',
    '-I.',
    '--python_out=.',
    '--mypy_out=.',
    '--grpc_python_out=.',
    'file_state.proto',
))