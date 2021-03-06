mod monkey;
use monkey::lang::{Parser, Token, TokenType};

use std::io;

fn main() {
    let tokens = [
        Token {
        token_type: TokenType::from_string(String::from("let")),
        value: None
    }; 1];

    let parser = &Parser {tokens:&tokens};
    parser.parse();

    let some_number = Some(5);
    let some_string = Some("a string");
    let absent_number: Option<i32> = Some(10);

    let r = match absent_number {
        Some(n) => n*n,
        None => 1,
    };
//    println!("{:?}!", r);

    let mut input = String::new();
    match io::stdin().read_line(&mut input) {
        Ok(n) => {
            println!("{} bytes read", n);
            println!("{}", input);
        }
        Err(error) => println!("error: {}", error),
    }
}
