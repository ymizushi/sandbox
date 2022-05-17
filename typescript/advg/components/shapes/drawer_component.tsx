import type { NextPage } from 'next'
import React, { useState, useEffect, useCallback, useRef } from 'react';
import { Rect } from '../../primitives/rect';
import {Point} from '../../primitives/point';
import { Drawable } from '../../primitives/drawable';
import { RectComponent } from './rect_component';

export const DrawerComponent = ({drawables}: {drawables: Drawable[]}) => {
  return (
    <>
    {drawables.map(drawable => {
      if (drawable instanceof Rect) {
        return (
          <RectComponent rect={drawable} />
        )
      }
    })}
    </>
  )
}