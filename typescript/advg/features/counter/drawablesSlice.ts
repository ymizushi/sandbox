import { createSlice } from "@reduxjs/toolkit";

import { Drawable } from "../../primitives/drawable";

export interface DrawablesState {
  drawables: Drawable[]
}
const initialState = {drawables: []} as DrawablesState

export const drawablesSlice = createSlice({
  name: 'drawable',  
  initialState,
  reducers: {
    push: (state, action) => {
      state.drawables.push(action.payload) ;
    },
    pop: (state) => {
      state.drawables.pop();
    }
  },
})

export const { push, pop } = drawablesSlice.actions

export default drawablesSlice.reducer