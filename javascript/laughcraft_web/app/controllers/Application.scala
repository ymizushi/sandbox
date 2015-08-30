package controllers

import play.api._
import play.api.mvc._

object Application extends Controller {

  def index = Action {
    Ok(views.html.index("Your new application is ready."))
  }

  def projects(id: Long) = Action {
    val sampleJson = """{"synthList" : [{
             "synthDef": {
               "id": "carrier",
               "ugen": "flock.ugen.sin",
               "freq": 440,
               "mul": {
                 "id": "env",
                 "ugen": "flock.ugen.env.simpleASR",
                 "attack": 0.25,
                 "sustain": 1.0,
                 "release": 0.5
               }
             }
          }],
          "noteList" : [
      {
        "action": "noteOn",
        "noteName": "root",
        "change": {
          "carrier.freq": 440
        },
        "point" : [1,0,0],
        "synthIndex": 0

      },
      {
        "action": "noteOn",
        "noteName": "mediant",
        "change": {
            "carrier.freq": 880
        },
        "point" : [2,0,1],
        "synthIndex": 0
      },
      {
        "action": "noteOn",
        "noteName": "dominant",
        "change": {
            "carrier.freq": 660
        },
        "point" : [3,0,2],
        "synthIndex": 0
      },
      {
        "action": "noteOff",
        "noteName": "root",
        "point" : [4,0,3],
        "synthIndex": 0
      },
      {
        "action": "noteOff",
        "noteName": "mediant",
        "point" : [5,0,4],
        "synthIndex": 0
      },
      {
        "action": "noteOff",
        "noteName": "dominant",
        "point" : [6,0,5],
        "synthIndex": 0
      }
    ],

    "objectList" : [
        {"objectId":1, "point" : [0,0,0]},
        {"objectId":1, "point" : [1,0,0]},
        {"objectId":1, "point" : [2,0,1]},
        {"objectId":1, "point" : [3,0,3]},
        {"objectId":1, "point" : [4,0,0]},
        {"objectId":1, "point" : [5,0,1]},
        {"objectId":1, "point" : [6,0,3]},
        {"objectId":1, "point" : [7,0,5]},
        {"objectId":1, "point" : [8,0,5]},
        {"objectId":1, "point" : [9,0,5]},
        {"objectId":1, "point" : [10,0,5]},
        {"objectId":1, "point" : [11,0,6]},
        {"objectId":1, "point" : [12,0,9]},
        {"objectId":1, "point" : [13,0,9]},
        {"objectId":1, "point" : [14,0,6]},
        {"objectId":1, "point" : [15,0,6]},
        {"objectId":1, "point" : [15,1,6]},
        {"objectId":1, "point" : [15,2,6]},
        {"objectId":1, "point" : [15,3,6]},
        {"objectId":1, "point" : [16,0,8]},
        {"objectId":1, "point" : [17,0,6]},
        {"objectId":1, "point" : [18,0,2]},
        {"objectId":1, "point" : [19,0,6]}
    ],

    "keyframeList" : [
        {
            "camera" : {
                "type" : "linear",
                "frameNum" : 20,
                "position": [1000,1000,1000],
                "lookat" : [100,100,100]
            }
        },
        {
            "camera" : {
                "type" : "linear",
                "frameNum" : 20,
                "position": [2000,2000,2000],
                "lookat" : [200,200,200]
            }
        },
        {
            "camera" : {
                "type" : "linear",
                "frameNum" : 20,
                "position": [3000,3000,3000],
                "lookat" : [300,300,300]
            }
        }
    ]
}"""
    Ok(sampleJson).as("application/json;charset=utf-8")
  }

}
