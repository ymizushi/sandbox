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
    char *dev, errbuf[PCAP_ERRBUF_SIZE];

    run();
    dev = pcap_lookupdev(errbuf);
    if (dev == NULL) {
        fprintf(stderr, "Couldn't find default device: %s\n", errbuf);
        return(2);
    }
    printf("Device: %s\n", dev);
    return(0);
}
