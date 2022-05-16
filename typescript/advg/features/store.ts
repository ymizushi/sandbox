import { configureStore } from '@reduxjs/toolkit'
import counterRedurcer from './counter/counterSlice'

export default configureStore({
  reducer: {
    counter: counterRedurcer
  }
})