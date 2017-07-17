mod monkey;

use monkey::lang::{Parser, Token, TokenType};

// Writing an interpreter in go.
fn main() {
    let token = Token {token_type: TokenType::LET};
    token.to_string();
    TokenType::from_string(String::from("LET"));
    let parser = Parser { };
    parser.println();

    let some_number = Some(5);
    let some_string = Some("a string");
    let absent_number: Option<i32> = Some(20);

    let r = match absent_number {
        Some(n) => n*n,
        None => 1,
    };
    println!("{:?}!", r);
}
