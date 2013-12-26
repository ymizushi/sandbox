otonashi-clj
================================

Hub server to exchange music data.

## Requirements
- clojure 1.5 or later.
- leiningen 2.0 or later.
- overtone 0.8.1 or later.

These requirements are automatically installed by leiningen.

## Install
1. Mac OS X
 
 ```sh
brew install curl
brew install wget
brew install clojure
brew install leiningen
brew install rlwrap
```

## Usage

 ```sh
lein run
```

## Unit test

 ```sh
lein test
```

## Coverage

 ```sh
lein cloverage
```

Output files are located in ./target/coverage/ and open index.html.

## Auto compile ClojureScript

 ```sh
lein cljsbuild auto
```

## License
Copyright © 2013 ymizushi

Distributed under the Eclipse Public License, the same as Clojure.
