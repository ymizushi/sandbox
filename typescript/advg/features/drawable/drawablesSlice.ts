import { createSlice } from "@reduxjs/toolkit";

import { Drawable } from "../../primitives/drawable";

type ClickState = {
    startX: number,
    startY: number,
    endX: number,
    endY: number,
    mouseClicked: boolean
}

export interface DrawablesState {
  drawables: Drawable[]
  clickState: ClickState
}
const initialState = {drawables: []} as DrawablesState


export const drawablesSlice = createSlice({
  name: 'drawable',  
  initialState,
  reducers: {
    push: (state, action) => {
      state.drawables.push(action.payload) ;
      return state
    },
    pop: (state) => {
      state.drawables.pop();
      return state
    }
  },
})

export const { push, pop } = drawablesSlice.actions

export default drawablesSlice.reducer