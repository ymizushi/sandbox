import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { RootState } from '../store'
import { push, pop } from './drawablesSlice'
import { Drawable } from '../../primitives/drawable'
import { Rect } from '../../primitives/rect'
import { Point } from '../../primitives/point'
import { Size } from '../../primitives/size'
import { DrawerComponent } from '../../components/shapes/drawer_component'

export function Drawable() {
  const drawables: Drawable[] = useSelector<RootState, Drawable[]>((state) => state.drawables.drawables )
  const dispatch = useDispatch()

  return (
    <div>
      <div>
        <button
          aria-label="Rect"
          onClick={() => dispatch(push(new Rect(new Point(10, 10), new Size(10, 20))))}
        >
          Increment
        </button>
        <span>

        <svg width={800} height={800} xmlns="http://www.w3.org/2000/svg">
          <DrawerComponent drawables={drawables} />
        </svg>
        </span>
        <button
          aria-label="Delete"
          onClick={() => dispatch(pop()) }
        >Decrement</button>
      </div>
    </div>
  )

}