import grpc
import file_state_pb2_grpc
import file_state_pb2


def run():
    channel = grpc.insecure_channel('localhost:50051')
    filestate = file_state_pb2_grpc.FileStateStub(channel)
    response = filestate.ExistsInState(file_state_pb2.ExistsInStateRequest(
        path='/home/anselmos/Documents/test.txt'
    ))
    print("File Exists?: ", response.exists)


if __name__ == '__main__':
    run()