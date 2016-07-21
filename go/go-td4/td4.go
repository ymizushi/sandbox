package main

import (
    "fmt"
    "os"
    "bytes"
    "encoding/binary")

type uint4 uint8

func (t uint4) add(target uint4) (uint4, uint4) {
    add_result := t + target
    carry := (add_result >> 4) & 1
    result := add_result & 15
    return result, carry
}

const (
   MOV_A_Im = 3
   MOV_B_Im = 7
   MOV_A_B = 1
   MOV_B_A = 4
   ADD_A_Im = 0
   ADD_B_Im = 5
   IN_A = 2
   IN_B = 6
   OUT_Im = 11
   OUT_B = 9
   JMP_Im =15
   JNC_Im =14
)

type TD4 struct {
    a uint4
    b uint4
    carry uint4
    in uint4
    out uint4
    pc uint4
}

func (t *TD4) exec(command uint8) {
    op := (uint4)(command & 240) >> 4
    im := (uint4)(command & 15)

    switch op {
        case MOV_A_Im:
            t.a = im
            t.carry = 0
        case MOV_B_Im:
            t.b = im
            t.carry = 0
        case MOV_A_B:
            t.a = t.b
            t.carry = 0
        case MOV_B_A:
            t.b = t.a
            t.carry = 0
        case ADD_A_Im:
            result, carry := t.a.add(im)
            t.a = result
            t.carry = carry
        case ADD_B_Im:
            result, carry := t.b.add(im)
            t.b = result
            t.carry = carry
        case IN_A:
            t.a = t.in
            t.carry = 0
        case IN_B:
            t.b = t.in
            t.carry = 0
        case OUT_Im:
            t.out = im
            t.carry = 0
        case OUT_B:
            t.out = im
            t.carry = 0
        case JMP_Im:
            t.pc = im
            t.carry = 0
            return
        case JNC_Im:
            if t.carry == 0 {
                t.pc = im
            }
            t.carry = 0
            return
    }
    t.pc += 1
    return 
}

func (t *TD4) mainExec(commandArray []uint8) {
    for ;; {
        t.exec(commandArray[t.pc])
        fmt.Printf("td4: %v\n", t)
        if int(t.pc) == len(commandArray) {
            break
        }
    }
}



func main() {
    td4 := &TD4{
        a: 0,
        b: 0,
        carry: 0,
        in: 0, 
        out: 0,
        pc: 0,
    }

    // read file
    file, err := os.Open("test.bin")
    if err != nil {
        fmt.Println("err:", err)
        return
    }

    b := make([]uint8, 1)
    array := make([]uint8, 0)
    var r error
    for r=nil;r==nil;_, r = file.Read(b) {
        var val uint8
        convertError := binary.Read(bytes.NewBuffer(b), binary.BigEndian, &val)
        if convertError != nil {
            fmt.Println("convertError:", convertError)
            return
        }
        // 初回にゴミデータが取得されてしまうので、直しておく
        array = append(array, val)
    }
    td4.mainExec(array)

    // result, carry := td4.a.add(15)
    // fmt.Printf("result: %v\n", result)
    // fmt.Printf("carry: %v\n", carry)
}
