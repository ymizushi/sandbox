#include <stdio.h>
#include <pcap.h>
#include <SDL.h>

int initializeSDL(int flags) {
    if (SDL_Init(flags) < 0) {
        fprintf(stderr, "%s\n", SDL_GetError());
        return 0;
    }
    atexit(SDL_Quit);
    return 1;
}

int initializeVideo(int width, int height, int flags) {
    if (0 == SDL_SetVideoMode(width, height, 0, flags)) {
        fprintf(stderr, "%s\n", SDL_GetError());
        return 0;
    }
    return 1;
}
int run() {
    if(!initializeSDL(SDL_INIT_VIDEO)) {
        return 1;
    }
    int tick = SDL_GetTicks();
    int fps = 0;
    while(1) {
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                return 0;
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_ESCAPE) {
                return 0;
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_LEFT) {
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_RIGHT) {
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_UP) {
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_DOWN) {
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_k ) {
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_j) {
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_h ) {
            }else if(event.type == SDL_KEYDOWN && event.key.keysym.sym == SDLK_l ) {
            }else{ }
        }
        if(SDL_GetTicks() < tick +1000) {
            fps++;
        } else {
            printf("fps=%d\n", fps);
            fps = 0;
            tick = SDL_GetTicks();
        }
        SDL_GL_SwapBuffers();
    }
}

int main(int argc, char *argv[]) {
    char *dev;
    pcap_t *handle;      /* Session handle */
    char errbuf[PCAP_ERRBUF_SIZE];   /* Error string */
    struct bpf_program fp;      /* The compiled filter expression */
    char filter_exp[] = "port 80";   /* The filter expression */
    bpf_u_int32 mask =0;      /* The netmask of our sniffing device */
    bpf_u_int32 net = 0;      /* The IP of our sniffing device */

    struct pcap_pkthdr header; /* The header that pcap gives us */
    const u_char *packet; /* The actual packet */

    dev = pcap_lookupdev(errbuf);
    dev = "en0";
    if (dev == NULL) {
        fprintf(stderr, "Couldn't find default device: %s\n", errbuf);
        return(2);
    }
    
    if (pcap_lookupnet(dev, &net, &mask, errbuf) == -1) {
        fprintf(stderr, "Can't get netmask for device %s\n", dev);
        fprintf(stderr, "errbuf %s\n", errbuf);
        net = 0;
        mask = 0;
    }
    handle = pcap_open_live(dev, BUFSIZ, 1, 1000, errbuf);
    if (handle == NULL) {
        fprintf(stderr, "Couldn't open device %s: %s\n", dev, errbuf);
        return(2);
    }
    if (pcap_compile(handle, &fp, filter_exp, 0, net) == -1) {
        fprintf(stderr, "Couldn't parse filter %s: %s\n", filter_exp, pcap_geterr(handle));
        return(2);
    }
    if (pcap_setfilter(handle, &fp) == -1) {
        fprintf(stderr, "Couldn't install filter %s: %s\n", filter_exp, pcap_geterr(handle));
        return(2);
    }

    /* Grab a packet */
    packet = pcap_next(handle, &header);
    /* Print its length */
    printf("Jacked a packet with length of [%d]\n", header.len);
    /* And close the session */
    pcap_close(handle);
    return(0);


    run();
    return(0);
}
