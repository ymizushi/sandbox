import { configureStore } from '@reduxjs/toolkit'
import counterRedurcer from './counter/counterSlice'

export const store = configureStore({
  reducer: {
    counter: counterRedurcer
  }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch