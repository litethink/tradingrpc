package main

import (
    "log"
    "net"
    "google.golang.org/grpc"
    pb "github.com/litethink/tradingrpc"
)

const (
    port = ":50000"
)
func main() {
    lis, err := net.Listen("tcp", port)
    if err != nil {
        log.Fatal("failed to listen: %v", err)
    }
    log.Println("RPC server listening at",port)

    s := grpc.NewServer()
    pb.RegisterRpcServiceServer(s, &pb.Server{})
    s.Serve(lis)

}
