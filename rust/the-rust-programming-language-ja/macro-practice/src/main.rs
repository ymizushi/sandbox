#[macro_export]
macro_rules! vec {
    ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
            $(
                    temp_vec.push($x);
            )*
            temp_vec
        }
    };
}

#[macro_export]
macro_rules! adder {
    ( $( $x:expr ),* ) => {
        {
            let mut temp_sum = 0;
            $(
                temp_sum += $x;
            )*
            temp_sum
        }
    };
}




fn main() {
    let piyo: Vec<i32> = vec![1, 2];
    println!("Hello, world!{:?}", piyo);
    let fuga = adder!(1, 2, 3, 4, 5);
    println!("Hello, world!{:?}", fuga);
}
