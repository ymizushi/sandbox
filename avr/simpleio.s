.equ DDRB, 0x17

.org 0x00
reset:
rjmp main; // rjmp  .+2
rjmp defaultInt; // rjmp .+0

defaultInt:
reti; // 9518

main:
sbi DDRB, 0;// 9A b8 : sbi 0x17, 0
cbi DDRB, 0; // 98 b8 cbi 0x17, 0

hoge:
rjmp hoge; // rjmp   .-2

# rjmp  .-2

# :10 0000 00   0F C0 0D C0 0C C0 0B C0 0A C0 09 C0 08 C0 07 C0   9B
# :10 0010 00   06 C0 05 C0 04 C0 03 C0 02 C0 01 C0 00 C0 18 95   DE
# :06 0020 00   B8 9A B8 98 FF CF                                 6A
# :00 0000 01   FF

# :0C 0000 00   02 C0 00 C0 18 95 B8 9A B8 98 FF CF               55
# :00 0000 01   Fl

# :0A 0000 00   02 C0 00 C0 18 95 B8 9A B8 98                     25
# :00 0000 01   FF
