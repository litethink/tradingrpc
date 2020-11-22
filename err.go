
package tradingrpc

import (
    "errors"
)

type Error struct {
    err error
    msg string
}


func (e *Error) Raise() error {
    return e.err
   
}    
   
func ErrParameterUnfound () *Error {
    e := &Error{err: errors.New("PARMETER_UNFOUND"),msg: "Parameter unfound!"}
    return e
}

func ErrQueryNameUnfound () *Error {
    e := &Error{err: errors.New("QUERYNAME_UNFOUND"),msg: "Query name unfound!"}
    return e
}

