struct Square<'a> {
    point: &'a Point,
    size: &'a Size
}

struct Size {
    width: i32,
    height: i32
}

struct Point {
    x: i32,
    y: i32
}

impl<'a> Square<'a> {
    fn new(size: &'a Size, point: &'a Point) -> Self {
        Square {
            point,
            size
        }
    }
}

fn main() {
    let size = &Size { width: 10, height: 10 };
    let point = &Point { x: 10, y: 20 };
    Square::new(size, point);
}
