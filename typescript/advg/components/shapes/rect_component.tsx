import type { NextPage } from 'next'
import React, { useState, useEffect, useCallback, useRef } from 'react';
import {Rect} from '../../primitives/rect'

const RectComponent = (rect: Rect) => {
      <rect
        style={
          {
            fill: `pink`
          }
        }
        x={rect.start.x} 
        y={rect.start.y} 
        width={rect.size.width}
        height={rect.size.height}
      />
}