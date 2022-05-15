import type { NextPage } from 'next'
import React, { useState, useEffect, useCallback, useRef } from 'react';
import Head from 'next/head'
import styles from '../styles/Home.module.css'
import { Provider } from 'react-redux'
import {store} from '../store'


type Margin = {
  top: number;
  left: number;
}
type Size = {
  width: number;
  height: number;
}

type Props = {
  margin: Margin;
  size: Size;
};

const Home: NextPage = () => {
  const margin = {top: 0, left: 0}
  const size = {width: 800, height: 800}

  return (
    <>
      <Head>
        <title>ymizushi</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <Provider store={store}>
        <svg width={size.width} height={size.height} xmlns="http://www.w3.org/2000/svg">
          <ADVGCanvas margin={margin} size={size}></ADVGCanvas>
        </svg>
      </Provider>
    </>
  )
}

const ADVGCanvas = ({margin, size}: Props) => {
  const [clickState, setClickState] = useState({
    startX: 0,
    startY: 0,
    endX: 0,
    endY: 0,
    mouseClicked: false
  });
  const mouseDown = useCallback(
    ( { clientX: startX, clientY: startY }: {clientX: number, clientY: number} ) => {
      console.log(`mouseDown: ${startX}, ${startY}`)
      setClickState(beforeState => {
        return {
          startX: startX,
          startY: startY,
          endX: startX,
          endY: startY,
          mouseClicked: true
        };
      })
    },
    []
  );

  const mouseUp = useCallback(
    ( { clientX: endX, clientY: endY }: {clientX: number, clientY: number} ) => {
      console.log(`mouseUp: ${endX}, ${endY}`)

      setClickState(beforeState => {
        return {
          startX: beforeState.startX,
          startY: beforeState.startY,
          endX: endX,
          endY: endY,
          mouseClicked: false
        };
      })
    },
    []
  );

  const mouseMove = useCallback(
    ( { clientX: x, clientY: y }: {clientX: number, clientY: number} ) => {
      console.log(`mouseMove: ${x}, ${y}`)

      setClickState(beforeState => {
        if (beforeState.mouseClicked) {
          return {
            startX: beforeState.startX,
            startY: beforeState.startY,
            endX: x,
            endY: y,
            mouseClicked: true
          };
        } else {
          return {
            startX: beforeState.startX,
            startY: beforeState.startY,
            endX: beforeState.endX,
            endY: beforeState.endY,
            mouseClicked: false
          };
        };
      })
    },
    []
  );

  useEffect(() => {
    // window.addEventListener("mousedown", mouseDown);
    // window.addEventListener("mouseup", mouseUp);

    // return () => {
    //   window.removeEventListener("mousedown", mouseDown);
    //   window.removeEventListener("mouseup", mouseUp);
    // };
  }, [clickState]);

  return (
    <g transform={`translate(${margin.left}, ${margin.top})`} onMouseDown={mouseDown} onMouseUp={mouseUp} onMouseMove={mouseMove}>
      <rect
        style={
          {
            fill: `pink`
          }
        }
        x={0} 
        y={0} 
        width={size.width}
        height={size.height}
      />

      <rect
        style={
          {
            fill: `white`,
            stroke: `black`
          }
        }
        x={25} 
        y={25} 
        width={size.width-50}
        height={size.height-50}
      />
      
      <rect
        style={
          {
            fill: `white`,
            stroke: `black`
          }
        }
        x={25} 
        y={25} 
        width={size.width-50}
        height={size.height-50}
      />

      <line x1={clickState.startX} y1={clickState.startY} x2={clickState.endX} y2={clickState.endY}
        style={
          {
            fill: `white`,
            stroke: `black`
          }
        }
      />
      
    </g>
  );
}

export default Home
