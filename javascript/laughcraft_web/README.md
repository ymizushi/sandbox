# LAUGH CRAFT
under construction

### Initialize
```sh
git clone git@github.com:ymizushi/laughcraft_web.git
brew insall npm # install node.js package manager
npm install -g bower # install package manager for javascript with npm
bower install
./curl.sh
brew install activator
```

### Install javascript environment
```sh
brew install npm
npm install -g grunt-cli
npm install grunt
npm install grunt-contrib-concat
npm install grunt-contrib-uglify
grunt build
```

### initialize database server
```sh
brew install postgres
initdb pg
postgres -D pg &
createdb laughcraft
export DATABASE_URL=postgresql://localhost:5432/laughcraft
```

### Postgres client
```sh
psql laughcraft
postgres=> \d
```

### Run server
```sh
activator run
```

### Test
```sh
# initialize test library with pip.
pip install jasmine
```

# test command
```sh
jasmine
open http://localhost:8888
```
