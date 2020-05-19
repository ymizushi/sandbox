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
    println!("{}, {}", x, y);
    let y = "I can also be bound to text!";
    println!("{}, {}", x, y);
}


fn function() {
    print_number(32);
    print_sum(32, 64);
}

fn ownership()  {
   let _s = "hello";
   let mut s = String::from("hello");
   s.push_str(", world!");
   println!("{}", s);

   let x = 5;
   let _y = x;

   let s1 = String::from("hello");
   let s2 = s1.clone();

   println!("s1 = {}, s2 = {}", s1, s2);

   let x = 5;
   let y = x;

   println!("x = {}, y = {}", x, y);
   let mut s = "some_string".to_string();
   s = takes_ownership(s);
   takes_ownership(s);

   let x = 5;
   make_copy(x);

   let _s1 = gives_ownership();
   let s2 = "hello".to_string();
   let _s3 = takes_and_gives_back(s2);

    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);

    {
        let mut s = String::from("hello");
        {
            let _r1 = &s;
            let _r2 = &s;
            println!("{}", _r1);
            println!("{}", _r2);
        }
        let _r3 = &mut s;
        println!("{}", _r3);
    }

    {
        let _reference_to_nothing = dangle();
    }
}

fn dangle() -> String {
    let s = String::from("hello");
    s
}

fn takes_ownership(some_string: String) -> String {
    println!("{}", some_string);
    some_string
}

fn gives_ownership() -> String {
    let some_string = String::from("hello");
    some_string
}

fn takes_and_gives_back(a_string: String) -> String {
    a_string
}

fn make_copy(some_integer: i32) {
    println!("{}", some_integer);

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

fn calculate_length(s: &String) -> usize {
    s.len()
}

fn primitive() {
    let _x = true;
    let _y: bool = false;

    let _x = 'x';
    let _two_hearts = '♥';

    let _a = [1, 2, 3];
    let mut _m = [1, 2, 3];
    let a = [0; 20];
    println!("a has {} elements", a.len());

    let names = ["Graydon", "Brian", "Niko"];
    println!("The second name is: {}", names[1]);

    let a: [i32; 5] = [0, 1, 2, 3, 4];
    let _complete: &[i32] = &a[..];
    let _middle: &[i32] = &a[1..4];

    let _x = (1, "hello");
    let _x: (i32, &str) = (1, "hello");

    let mut _x = (1, 2);
    let y = (2, 3);
    _x = y;

    let (x, _y, _z) = (1, 2, 3);
    println!("x is {}", x);

    let tuple = (1, 2, 3);
    let x = tuple.0;
    let _y = tuple.1;
    let _z = tuple.2;

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

    ownership();
}

