extern crate emola;

fn main() {
    // let inputs = "(def hoge 1)";
    // let mut tokens: Vec<emola::Token> = vec![];
    // let mut current_string: String = "".to_string();
    // let replaced_inputs = inputs.replace("(", " ( ").replace(")", " ) ");
    // let chars = replaced_inputs.chars();
    // for c in chars {
    //     let token: emola::Token = match c {
    //         '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' => {
    //             current_string.push(c);
    //             continue;
    //         },
    //         '(' => emola::Token::BracketStart,
    //         ')' => emola::Token::BracketEnd,
    //         '+' => emola::Token::Plus,
    //         '-' => emola::Token::Minus,
    //         ' ' => {
    //             if current_string.len() != 0 {
    //                 let num = current_string.parse().unwrap();
    //                 current_string.truncate(0);
    //                 emola::Token::Number(num)
    //             } else {
    //                 continue;
    //             }
    //         },
    //         _ => emola::Token::Unknown
    //     };
    //     println!("{}", token);
    //     tokens.push(token);
    // }
}
