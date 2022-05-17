import { configureStore } from '@reduxjs/toolkit'
import drawablesRedurcer from './drawable/drawablesSlice'

export const store = configureStore({
  reducer: {
    drawables: drawablesRedurcer
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch