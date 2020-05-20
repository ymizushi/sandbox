struct Point<T, U> {
    x: T,
    y: U,
}

impl<T,U> Point<T, U> {
    fn mixup<V, W>(& self, other: Point<V, W>) -> Point<&T, W> {
        Point {
            x: & self.x,
            y: other.y,
        }
    }
}

fn largest(list: &[i32]) -> i32 {
    let mut largest = list[0];
    for &item in list.iter() {
        if item > largest {
            largest = item;
        }
    }
    largest
}


fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

fn logest2<'a>(x: &str, y: &str) -> &'a str {
    let result = String::from("really long string");
    result.as_str();
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];
    println!("The largest number is {}", largest(&number_list));


    let p1 = Point { x:5, y: 10.4 };
    let p2 = Point { x: "Hello", y: 'c'};
    let p3 = p1.mixup(p2);
    println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
    println!("p1.x = {}", p1.x);

    {
        let r;
        let x = 5;
        r = &x;
        println!("r: {}", r);
    }

    { 
        let string1 = String::from("abcd");
        {
            let string2 = "xyz";

            let result = longest(string1.as_str(), string2);
            println!("the longest string is {}", result);
        }
    }
}
