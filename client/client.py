import grpc
import tradingrpc_pb2
import tradingrpc_pb2_grpc


channel = grpc.insecure_channel('localhost:50000')

stub = tradingrpc_pb2_grpc.RpcServiceStub(channel)
res = stub.Request(tradingrpc_pb2.DataRequest(Parameters={"name":"kline","period":"x","size":"y","symbol":"z"}))
any_data = tradingrpc_pb2.Klines()
#data = res.Data.Unpack(any_data)
#print(data)
res.Data.Unpack(any_data)
print(any_data)
print(any_data.Data[0].Close)
