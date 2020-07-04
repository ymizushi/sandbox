trait Renderer {
    fn render(&self);
}

impl Renderer for i32 {
    fn render(&self) {
        println!("{}", 3);
    }
}

impl Renderer for String {
    fn render(&self) {
        println!("{}",String::from("string"));
    }
}

fn return_result() -> impl Renderer {
    println!("select i32");
    10
}

fn main() {
    let result = return_result();
    result.render();
    20.render();
}
