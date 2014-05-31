#if 0
#ifndef lint
static char sccsid[] = "@(#)util.c      8.3 (Berkeley) 4/2/94";
#endif /* not lint */
#endif
#include <sys/cdefs.h>
__FBSDID("$FreeBSD$");

#include <sys/types.h>
#include <sys/stat.h>

#include <ctype.h>
#include <err.h>
#include <fts.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wchar.h>
#include <wctype.h>

// #include "ls.h"
// #include "extern.h"

int
prn_normal(const char *s)
{
    mbstate_t mbs;
    wchar_t wc;
    int i,n;
    size_t clen;

    memset(&mbs, 0, sizeof(mbs));
    n = 0;
    while ((clen = mbrtowc(&wc, s, MB_LEN_MAX, &mbs)) != 0) {
        if (clen == (size_t)-2) {
            n += printf("%s", s);
            break;
        }
    
    }
    if (clen == (size_t)-1) {
        membset(&mbs ,0 ,sizeof(mbs));
        s++;
    }
}
