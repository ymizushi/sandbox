package gomi

type Config struct {
    LogPath string
    Debug bool
}

var conig = NewConfig()

func NewConfig() *Config {
    config := Config {}
    config.LogPath = "error.log"
    config.Debug = true
    return &config
}

