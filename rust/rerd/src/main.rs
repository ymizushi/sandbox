use svg::Document;
use svg::node::element::Path;
use svg::node::element::Rectangle;
use svg::node::element::path::Data;


extern crate rustc_ap_graphviz;
use std::io::Write;
use graphviz as dot;

type Nd = isize;
type Ed = (isize,isize);
struct Edges(Vec<Ed>);

pub fn render_to<W: Write>(output: &mut W) {
    let edges = Edges(vec![(0,1), (0,2), (1,3), (2,3), (3,4), (4,4)]);
    dot::render(&edges, output).unwrap()
}

impl<'a> dot::Labeller<'a> for Edges {
    type Node = Nd;
    type Edge = Ed;
    fn graph_id(&'a self) -> dot::Id<'a> { dot::Id::new("example1").unwrap() }

    fn node_id(&'a self, n: &Nd) -> dot::Id<'a> {
        dot::Id::new(format!("N{}", *n)).unwrap()
    }
}

impl<'a> dot::GraphWalk<'a> for Edges {
    type Node = Nd;
    type Edge = Ed;
    fn nodes(&self) -> dot::Nodes<'a,Nd> {
        // (assumes that |N| \approxeq |E|)
        let &Edges(ref v) = self;
        let mut nodes = Vec::with_capacity(v.len());
        for &(s,t) in v {
            nodes.push(s); nodes.push(t);
        }
        nodes.sort();
        nodes.dedup();
        nodes.into()
    }

    fn edges(&'a self) -> dot::Edges<'a,Ed> {
        let &Edges(ref edges) = self;
        (&edges[..]).into()
    }

    fn source(&self, e: &Ed) -> Nd { let &(s,_) = e; s }

    fn target(&self, e: &Ed) -> Nd { let &(_,t) = e; t }
}

#[derive(Debug)]
struct Table<'a> {
    name: &'a str,
    relations: Vec<&'a Table<'a>>
}

impl<'a> Table<'a> {
    fn draw(&self) {
        self.drawRect();
    }

    fn drawRect(&self) {

    }

    fn drawName(&self) {

    }
}

#[derive(Debug)]
struct Point {
    x: i32,
    y: i32
}

impl Point {
    fn new(x: i32, y:i32) -> Point {
        Point {
            x,
            y
        }
    }
}
#[derive(Debug)]
struct Size {
    width: i32,
    height: i32
}


#[derive(Debug)]
struct Canvas {
    width: i32,
    height: i32,
}

impl Canvas {
    fn new(width: i32, height: i32) -> Canvas {
        Canvas {
            width,
            height
        }
    }

    fn draw_rect<'a>(&self, document: Document, start: Point, end: Point) -> Document {
        let rectangle = Rectangle::new()
            .set("x", start.x)
            .set("y", start.y)
            .set("width", end.x-start.x)
            .set("height", end.y-start.y)
            .set("fill", "none")
            .set("stroke", "black")
            .set("stroke-width", 3);
        document.add(rectangle)
    }

    fn draw_arrow(&self, document: Document, start: Point, end: Point) -> Document {
        let rectangle = Rectangle::new()
            .set("x", start.x)
            .set("y", start.y)
            .set("width", end.x-start.x)
            .set("height", end.y-start.y)
            .set("fill", "none")
            .set("stroke", "black")
            .set("stroke-width", 3);
        document.add(rectangle)
    }
}


fn calc_points(tables: Vec<Table>) -> Vec<(Table, Point, Size)> {
    vec![(
        Table { name: "Person", relations: vec![] },
        Point::new(0, 0),
        Size { width: 10, height: 10}
    )]
}

fn main() {
    let company = Table { name: "Person", relations: vec![] }; let person = Table { name: "Company", relations: vec![&company] };
    let tables = vec![&company, &person];
    let canvas = Canvas::new(100, 100);
    let document = Document::new()
        .set("viewBox", (0, 0, canvas.width, canvas.height));
    let returned_document = canvas.draw_rect(document, Point::new(0, 0), Point::new(100, 100));

    println!("{:?}", tables);

    svg::save("image.svg", &returned_document).unwrap();

    use std::fs::File;
    let mut f = File::create("example1.dot").unwrap();
    render_to(&mut f)
}
