
package tradingrpc



//for test,
func GetKline(map[string]string) (*Klines){
    var klines Klines
    klines.Result = true
    klines.Data = append(klines.Data,&Kline{
    Id: 1,Ts: 2,Open: 1.2,Close: 1.4,High: 1.4,Low: 1.2,Amount: 1.7,Count: 1.9,Volume:        2.1111})
    return &klines   
}

func GetHistory(map[string]string) (*Historys){
    var historys Historys
    historys.Result = true
    historys.Data = append(historys.Data,&History{Id: 11,Ts: 222,Price: 11.2,Amount: 22.4,Direction: true})
    return &historys
}

