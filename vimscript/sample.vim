"let i = 1
"while i < 5
"    echo "count is" i
"    let i += 1
"endwhile
"
"for i in range(1, 4)
"    echo "count is" i
"    echo 0x7f 036
"endfor

let s:count = 1
while s:count < 5
    source other.vim
    let s:count += 1
    echo s:count
endwhile

function! Min(num1, num2)
    if a:num1 < a:num2
        return a:num1
    endif
    return a:num2
endfunction

echo Min(40, 30)

let alist = ['app', 'name']
echo alist
call add(alist, 'hoge')
echo alist
let blist = add(alist, 'puyo')
echo  alist + blist + alist
