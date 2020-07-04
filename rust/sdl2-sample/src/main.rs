use std::mem;
use std::os::raw::c_void;
use c_str_macro::c_str;
use cgmath::perspective;

use cgmath::preludate::SquareMatrix;

use gl::types::{GLfloat, GLSizai, GLsizeiptr};

use sdl2::event::Event;
use sdl2::keyboard::Keycode;
use sdl2::pixels::Color;
use std::time::Duration;

mod shader;
mod vertex;

use shader::Shader;
use vertex::Vertex;

#[allow(dead_code)]
type Point3 = cgmath::Point3<f32>;

#[allow(dead_code)]
type Vector3 = cgmath::Vector3<f32>;

#[allow(dead_code)]
type Matrix4 = cgmath::Matrix4<f32>;

const WINDOW_WIDTH: u32 = 640;
const WINDOW_HEIGHT: u32 = 480;

const FLOAT_NUM: usize = 3;
const VERTEX_NUM: usize = 3;
const BUF_LEN: usize = FLOAT_NUM * VERTEX_NUM;

fn main() {
    let sdl_context = sdl2::init().unwrap();
    let video_subsystem = sdl_context.video().unwrap();

    {
        let gl_attr = video_subsystem.gl_attr();

    let window = video_subsystem
        .window("SDL", 640, 480)
        .position_centered()
        .build()
        .unwrap();

    let mut canvas = window.into_canvas().build().unwrap();
    canvas.set_draw_color(Color::RGB(255, 255, 255));

    canvas.clear();
    canvas.present();

    let mut event_pump = sdl_context.event_pump().unwrap();

    'running: loop {
        for event in event_pump.poll_iter() {
            match event {
                Event::Quit { .. } | Event::KeyDown {
                    keycode: Some(Keycode::Escape),
                    ..
                    } => break 'running,
                _ => {}
            }
        }
        canvas.present();
        ::std::thread::sleep(Duration::new(0, 1_000_000_000u32 / 60));
    }
}
