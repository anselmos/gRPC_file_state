import file_state_pb2_grpc
import file_state_pb2
import random
import grpc
from concurrent import futures


class FileState(file_state_pb2_grpc.FileStateServicer):
    def __init__(self):
        self.choices = [True, False]

    def ExistsInState(self, request, context):
        response = random.choice(self.choices)
        return file_state_pb2.ExistsInStateResponse(exists=response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_state_pb2_grpc.add_FileStateServicer_to_server(FileState(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
