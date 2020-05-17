fn variable_binding() {
    let x = 5;
    println!("{}", x);
    let (x, y) = (1, 2);
    println!("{}, {}", x, y);
    let x: i32 = 5;
    println!("{}", x);

    let z = 10;
    println!("{}", z);

    let x: i32 = 17;
    {
        let y: i32 = 3;
        println!("The value of x is {} and value of y is {}", x, y);
    }
    println!("The value of x is {} and value of y is {}", x, y);

    let mut x: i32 = 1;
    println!("{}, {}", x, y);
    x = 7;
    let x = x;
    let y = 4;
    println!("{}, {}", x, y);
    let y = "I can also be bound to text!";
    println!("{}, {}", x, y);
}


fn function() {
    foo();
    print_number(32);
    print_sum(32, 64);
}

fn foo() {

}

fn print_number(x: i32) {
    println!("x is: {}", x);
}

fn print_sum(x: i32, y: i32) {
    println!("sum is {}", x+y);
}

fn add_one(x: i32) -> i32 {
    x + 1
}

// fn diverges() -> ! {
//     panic!("This function never returns!");
// }

fn primitive() {
    let x = true;
    let y: bool = false;

    let x = 'x';
    let two_hearts = '♥';

    let a = [1, 2, 3];
    let mut m = [1, 2, 3];
    let a = [0; 20];
    println!("a has {} elements", a.len());

    let names = ["Graydon", "Brian", "Niko"];
    println!("The second name is: {}", names[1]);

    let a: [i32; 5] = [0, 1, 2, 3, 4];
    let complete: &[i32] = &a[..];
    let middle: &[i32] = &a[1..4];

    let x = (1, "hello");
    let x: (i32, &str) = (1, "hello");

    let mut x = (1, 2);
    let y = (2, 3);
    x = y;

    let (x, y, z) = (1, 2, 3);
    println!("x is {}", x);

    let tuple = (1, 2, 3);
    let x = tuple.0;
    let y = tuple.1;
    let z = tuple.2;

    println!("x is {}", x);
}

fn main() {
    variable_binding();
    function();
    add_one(20);
    let f: fn(i32) -> i32 = add_one;
    f(1);
    let f = add_one;
    f(1);
    // let six = f(5);

    // let x: i32 = diverges();

    primitive();

}

