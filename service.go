package tradingrpc

import (
    "context"
    "log"
    "github.com/golang/protobuf/ptypes"
)


type Server struct{}

func (s *Server) Request(ctx context.Context, in *DataRequest) (*DataResponse, error) {
    data,err := requestToMiddleware(in)
    if err != nil {
        return data,err
    }
    
    return  data,nil
}

func requestToMiddleware (in *DataRequest) (*DataResponse,error) {
    var queryMap = make(map[string]string)
    switch in.Parameters["name"] {
	case "kline":
	    queryMap["symbol"] = in.Parameters["symbol"]
	    queryMap["size"]   = in.Parameters["size"]
	    queryMap["period"] = in.Parameters["period"]
	    arr := []string{"symbol","size","period"}
	    for i:= 0;i<len(arr);i++ {
	        if queryMap[arr[i]] != "" {
	        } else{
	            e := ErrParameterUnfound()
	            data :=&DataResponse{
                       StatusCode : 0,
                       ErrorMsg   : e.msg,
	            }
	            return data,e.err
	        }
	    }
	    kline := GetKline(queryMap)
	    anyTypeData,err := ptypes.MarshalAny(kline)
	    if err != nil{
                log.Println(err)
	    }
            data := &DataResponse{
               StatusCode : 1,
               Msg        : "success",
               Data       : anyTypeData, 
            }
            return data,nil
	    
	case "history":
	    queryMap["symbol"] = in.Parameters["symbol"]
	    queryMap["size"]   = in.Parameters["size"]
	    arr := []string{"symbol","size"}
	    for i:= 0;i<len(arr);i++ {
	        if _, ok := queryMap[arr[i]]; ok {
	        } else{
	            e := ErrParameterUnfound()
	            data :=&DataResponse{
                       StatusCode : 0,
                       ErrorMsg   : e.msg, 
	       }
	       return data,e.err
	    }
	    history := GetHistory(queryMap)
	    anyTypeData,err := ptypes.MarshalAny(history)
	    if err != nil{
                log.Println(err)
	    }
            data := &DataResponse{
                StatusCode : 1,
               Msg         : "success",
               Data        : anyTypeData, 
            }
            
            return data,nil
            }
        }
    e := ErrQueryNameUnfound()
    data :=&DataResponse{
        StatusCode : 0,
        ErrorMsg   : e.msg,
    }
    
    return data,e.err  
}





