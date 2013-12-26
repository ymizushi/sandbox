(ns websocket-clj.core
  (:use lamina.core aleph.http aleph.formats))

(def broadcast-channel (channel))

(defn chat-handler [ch handshake]
  (receive ch
    (fn [name]
      (siphon (map* #(str name ": " %) ch) broadcast-channel)
      (siphon broadcast-channel ch))))

(defn -main [& args]
  (start-http-server chat-handler {:port 8080 :websocket true}))
