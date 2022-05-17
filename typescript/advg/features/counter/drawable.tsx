import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { RootState } from '../store'
import { push, pop } from './drawablesSlice'
import { DrawablesState } from './drawablesSlice'
import { Drawable } from '../../primitives/drawable'

export function Counter() {
  const drawables = useSelector<RootState, Drawable[]>((state) => state.drawables.drawables )
  const dispatch = useDispatch()

  return (
    <div>
      <div>
        <button
          aria-label="Increment value"
          onClick={() => dispatch(increment())}
        >
          Increment
        </button>
        <span>{count}</span>
        <button
          aria-label="Decrement value"
          onClick={() => dispatch(decrement()) }
        >Decrement</button>
      </div>
    </div>
  )

}