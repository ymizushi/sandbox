use std::cell::RefCell;

fn main() {
    let mut c = RefCell::new(5);
    // let five = c.into_inner();
    let five_2 = c.get_mut();
    println!("{}", five_2);
}
